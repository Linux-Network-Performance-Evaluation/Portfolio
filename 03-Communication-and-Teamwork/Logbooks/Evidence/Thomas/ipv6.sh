#!/bin/bash

PACKET_SIZE=( 128 256 384 512 640 768 896 1024 1152 1280 1408 1536 )
PROTOCOL=("TCP" "UDP")

for prtcl in ${PROTOCOL[@]}; do
	for size in ${PACKET_SIZE[@]}; do
		for run in {1..12}; do
			echo "Evaluating IPv6 on ${prtcl}, ${size} bytes, run ${run} of 12"
			ITGSend -a fd00:0:0:30::2 -T ${prtcl} -c ${size} -t 31000 -x logs/ipv6_${prtcl,,}_${size}_${run}.log
			sleep 2
		done
	done
done
