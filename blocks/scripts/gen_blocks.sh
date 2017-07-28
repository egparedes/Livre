#!/bin/bash

start=${1:-0}
end=${2:-64}

rm *.obj 
cat ../*.log |  sed -n -e "s/^.*\[SORT-LAST\] //p" | sed -e 's/[\t ]\+/ /g' > blocks.txt
./gen_blocks_objs.py blocks.txt $start $end
