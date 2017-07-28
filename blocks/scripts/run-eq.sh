#!/bin/sh

cfg="$1"
bin_dir="${PWD}/build-debug/bin"
model="/media/henrique/DATA/Modelos/meshes/dragon.ply"

kill -9 $( ps -o pid,cmd -e | grep eqServer | sort | head -n 1 | cut -f 1 -d " ")
pkill -9 eqPly
rm *.log
export EQ_LOG_LEVEL=3
#export  EQ_LOG_TOPICS=ALL

echo "starting server..."
${bin_dir}/eqServer $cfg > node-server.log 2>&1 &
server_pid=$!
sleep 1

echo "starting clients..."
${bin_dir}/eqPly --eq-client --eq-listen 127.0.0.1:4702 > node1.log 2>&1 &
sleep 1
${bin_dir}/eqPly --eq-client --eq-listen 127.0.0.1:4703 > node2.log 2>&1 &
sleep 1
${bin_dir}/eqPly --eq-client --eq-listen 127.0.0.1:4704 > node3.log 2>&1 &
sleep 1
${bin_dir}/eqPly --eq-client --eq-listen 127.0.0.1:4705 > node4.log 2>&1 &
sleep 1

echo "listening process..."
netstat -tulp

echo "starting app node..."
${bin_dir}/eqPly -m $model --eq-server  127.0.0.1:4700 --eq-listen 127.0.0.1:4701 > node-app.log 2>&1 &
sleep 1
render_pid=$( pgrep eqPly | sort | head -n 1 )

echo "PIDS..."
echo "server_pid = $server_pid"
echo "render_pid = $render_pid"
#sleep 3
#qtcreator -debug $render_pid
#sleep 1

