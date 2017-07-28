#!/bin/bash

echo ""
echo "script_name.sh [frame_id]"
echo ""

node_id=1
frame_id=${1:-ALL}
for f in $(ls *.log); do
	echo "Generating blocks.${node_id}_${frame_id}.txt ..."
	cat $f | grep "Convex subset (frame $1" | sed -e 's/[^[]*//' -e 's/[^0-9]\+/\t/g' > blocks.${node_id}_${frame_id}.txt
    (( node_id=node_id+1 ))
done

