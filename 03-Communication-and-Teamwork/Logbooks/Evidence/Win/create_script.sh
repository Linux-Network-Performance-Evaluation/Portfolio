#!/bin/bash

PACKET_SIZE=(128 256 384 512 640 768 896 1024 1152 1280 1408 1536)
PROTOCOL=("TCP")
DEST_IP="192.168.30.2"
RATE=100000
DURATION=10000

CONFIG_DIR="configs"
mkdir -p "$CONFIG_DIR"

for prtcl in "${PROTOCOL[@]}"; do
    for size in "${PACKET_SIZE[@]}"; do
        echo "Generating config for 10 ${prtcl} flows, packet size ${size} bytes..."

        CONFIG_FILE="${CONFIG_DIR}/flow_tmp_${prtcl,,}_${size}.txt"
        > "$CONFIG_FILE"

        for run in {1..10}; do
            echo "-a $DEST_IP -T $prtcl -c $size -C $RATE -t $DURATION >> "$CONFIG_FILE"
        done
    done
done
