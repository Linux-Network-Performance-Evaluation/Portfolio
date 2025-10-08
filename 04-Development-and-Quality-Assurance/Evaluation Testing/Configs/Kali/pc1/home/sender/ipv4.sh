#!/bin/bash

PACKET_SIZE=( 128 256 384 512 640 768 896 1024 1152 1280 1408 1536 )

for size in ${PACKET_SIZE[@]}; do
	config_file=./flow_tcp_${size}.txt

	if [[ -f "$config_file" ]]; then
		echo "Running ITGSend for $config_file config file"
		ITGSend $config_file -x logs/ipv4_tcp_${size}.log
		echo "Completed size $size."
		sleep 2
	else
		echo "Config file $config_file not found." 
	fi
done
