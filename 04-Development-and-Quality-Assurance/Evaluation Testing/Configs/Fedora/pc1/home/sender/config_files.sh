#!/bin/bash

PACKET_SIZE=(128 256 384 512 640 768 896 1024 1152 1280 1408 1536)
PROTOCOL=("TCP" "UDP")
DEST_IP=("192.168.30.2" "fd00:0:0:30::2")
RATE=120000       # packets per second per flow
DURATION=10000
CONFIG_DIR=configs

if [[ ! -d "$CONFIG_DIR" ]]; then
  mkdir -p "$CONFIG_DIR"
fi

for ip in "${DEST_IP[@]}"; do
  for prtcl in "${PROTOCOL[@]}"; do
    for size in "${PACKET_SIZE[@]}"; do
      pushd ./${CONFIG_DIR}
      CONFIG_FILE=flow_${prtcl,,}_${ip,,}_${size}.txt
      # Generate multi-flow config
      > "$CONFIG_FILE"
      for run in {1..10}; do
          echo "-a $DEST_IP -T $prtcl -c $size -C $RATE -t $DURATION" >> "$CONFIG_FILE" 
      done
      sleep 2
      echo "Running ITGSend for $CONFIG_FILE config file"
      ITGSend ${CONFIG_FILE} -x logs/${ip,,}_${prtcl,,}_${size}.log
      echo "Completed ${ip,,} ${prtcl,,} for size ${size}"
      sleep 2
      popd

    done
  done
done
