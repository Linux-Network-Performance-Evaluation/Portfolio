#!/bin/bash

PACKET_SIZE=(128 256 384 512 640 768 896 1024 1152 1280 1408 1536)
PROTOCOL=("TCP")
DEST_IP="192.168.30.2"
RATE=100000       # packets per second per flow
DURATION=10000      
LOG_DIR="logs"

mkdir -p "$LOG_DIR"

for prtcl in "${PROTOCOL[@]}"; do
    for size in "${PACKET_SIZE[@]}"; do
        echo "Running 10 simultaneous ${prtcl} flows for packet size ${size} bytes..."

        CONFIG_FILE="flow_tmp_${prtcl,,}_${size}.txt"
        LOG_FILE="${LOG_DIR}/ipv4_${prtcl,,}_${size}_multi.log"

        # Generate multi-flow config
        > "$CONFIG_FILE"
        for run in {1..10}; do
            echo "-a $DEST_IP -T $prtcl -c $size -C $RATE -t $DURATION" >> "$CONFIG_FILE"
        done

        # Run all 10 flows simultaneously
        ITGSend -f "$CONFIG_FILE" -x "$LOG_FILE"

        # Optional: pause between runs if needed
        sleep 2
    done
done
