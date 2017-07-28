#!/usr/bin/env python3

import sys

assert len(sys.argv) == 2

boxes = []
input_file = sys.argv[1]
with open(sys.argv[1], 'r') as f:
    for line in f:
        box = []
        corners = line.split()
        assert len(corners) == 6
        box.append([corners[0], corners[1], corners[2]])
        box.append([corners[3], corners[1], corners[2]])
        box.append([corners[0], corners[4], corners[2]])
        box.append([corners[3], corners[4], corners[2]])
        box.append([corners[0], corners[1], corners[5]])
        box.append([corners[3], corners[1], corners[5]])
        box.append([corners[0], corners[4], corners[5]])
        box.append([corners[3], corners[4], corners[5]])
        boxes.append(box)

n_verts = 8 * len(boxes)
n_faces = 12 * len(boxes)
n_edges = 18 * len(boxes)

print('OFF')
print(n_verts, n_faces, n_edges, '# NVertices NFaces NEdges')
print('')

max_coord = 65536
i = 0
for box in boxes:
    assert len(box) == 8
    #print('# ---- Box ', i, '---- ')
    for v in box:
        assert len(v) == 3
        print(int(v[0]) / max_coord, int(v[1]) / max_coord, int(v[2]) / max_coord)
    print('')
    i += 1

i = 0
color_step = 1 / (len(boxes) / 3)
for box in boxes:
    assert len(box) == 8
    print('# ---- Box ', i, '---- ')
    base = 8*i
    c = ( i / 3) * color_step
    reduction = 0.5 * c
    red = c - (reduction * (i%3 == 0))
    green = c - (reduction * (i%3 == 1))
    blue = c - (reduction * (i%3 == 2))
    color = '{0} {1} {2}'.format(red, green, blue)
    print('3', base, base+1, base+2, color)   # front
    print('3', base+1, base+3, base+2, color)
    print('3', base+4, base+5, base+6, color)   # back
    print('3', base+5, base+7, base+6, color)
    print('3', base, base+4, base+2, color)   # left
    print('3', base+4, base+6, base+2, color)
    print('3', base+1, base+5, base+3, color)   # right
    print('3', base+5, base+7, base+3, color)
    print('3', base+2, base+3, base+6, color)   # top 
    print('3', base+3, base+7, base+6, color)
    print('3', base, base+1, base+4, color)   # bottom
    print('3', base+1, base+5, base+4, color)
    print('')
    i += 1
