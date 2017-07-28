#!/bin/bash

configs_dir=${1:-examples/configs}
echo "configs_dir = '$configs_dir'"

echo "" > tested-configs.txt
for eqc in $(ls ${configs_dir}/*.eqc)
do 
	echo "$eqc" >> tested-configs.txt
	build-debug/bin/eqPly -m ../dragon.ply --eq-config="$eqc"
	pkill eqPly
	pkill eqServer
	sleep 1
done
