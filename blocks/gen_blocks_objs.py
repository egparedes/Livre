#!/usr/bin/env python3

import sys

# usage: ./gen_blocks_objs.py blocks.txt start_frame end_frame

argc = len(sys.argv)
assert argc == 4
input_file = sys.argv[1]
start_frame = int(sys.argv[2])
end_frame = int(sys.argv[3])

color_maps = [ 'red', 'green', 'blue', 'grey', 'pink', 'purple', 'orange' ]

outputs = dict()
channel_colors = dict()

with open(sys.argv[1], 'r') as f_input:
    for line in f_input:
        fields = line.split()
        print('fields', fields)
        assert len(fields) == 13

        channel_id = fields[0].replace("'", "")
        frame_id = fields[1]
        box_type = fields[2] + 's'
        key = channel_id + '_' + box_type + '.f' + frame_id       
        if int(frame_id) < start_frame or int(frame_id) > end_frame:
            print('Skipping box for frame', frame_id)
            continue

        if key in outputs:
            f_output = outputs[key][0]
        else:
            if channel_id not in channel_colors:
                channel_colors[channel_id] = color_maps[len(channel_colors)]

            f_output = open(key + '.obj', 'w')
            outputs[key] = [f_output, channel_colors[channel_id], 0]
            obj_name = channel_id + '.' + box_type
            print('mtllib colormaps.mtl', file=f_output)
            print('o {0}'.format(obj_name), file=f_output)
            print('', file=f_output)

        color_map = outputs[key][1]
        box_count = outputs[key][2]
        outputs[key][2] = outputs[key][2] + 1
        #print('channel = ', channel_id)
        #print('frame = ', frame_id)
        #print('color_map = ', color_map)

        corners = [ fields[4], fields[5], fields[6], 
                    fields[9], fields[10], fields[11] ]
        #print('corners', corners)

        print('# ---- box {0} ----'.format(box_count), file=f_output)
        print('usemtl mtl_{0}_{1}'.format(color_map, min(box_count, 127)), file=f_output)
        print('v', corners[0], corners[1], corners[2], file=f_output)
        print('v', corners[3], corners[1], corners[2], file=f_output)
        print('v', corners[0], corners[4], corners[2], file=f_output)
        print('v', corners[3], corners[4], corners[2], file=f_output)
        print('v', corners[0], corners[1], corners[5], file=f_output)
        print('v', corners[3], corners[1], corners[5], file=f_output)
        print('v', corners[0], corners[4], corners[5], file=f_output)
        print('v', corners[3], corners[4], corners[5], file=f_output)

        base = 8 * box_count + 1
        print('', file=f_output)
        print('g box_{0}'.format(box_count), file=f_output)
        print('f', base, base+1, base+2, file=f_output)   # front
        print('f', base+1, base+3, base+2, file=f_output)
        print('f', base+4, base+5, base+6, file=f_output)   # back
        print('f', base+5, base+7, base+6, file=f_output)
        print('f', base, base+4, base+2, file=f_output)   # left
        print('f', base+4, base+6, base+2, file=f_output)
        print('f', base+1, base+5, base+3, file=f_output)   # right
        print('f', base+5, base+7, base+3, file=f_output)
        print('f', base+2, base+3, base+6, file=f_output)   # top 
        print('f', base+3, base+7, base+6, file=f_output)
        print('f', base, base+1, base+4, file=f_output)   # bottom
        print('f', base+1, base+5, base+4, file=f_output)
        print('', file=f_output)
