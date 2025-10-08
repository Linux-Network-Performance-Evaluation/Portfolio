#!/bin/bash

# Full Test just for TCP

PACKET_SIZE=( 128 256 384 512 640 768 896 1024 1152 1280 1408 1536 )
PROTOCOL=("TCP" "UDP")


for prtcl in ${PROTOCOL[@]}; do
    for size in ${PACKET_SIZE[@]}; do
 		for run in {1..10}; do
 			echo "Evaluating IPv4 on ${prtcl}, ${size} bytes, run ${run} of 10"
 			ITGSend -a 192.168.30.2 -T ${prtcl} -c ${size} -C 1000000 -t 10000 -x logs/ipv4_${prtcl,,}_${size}_${run}.log
 			sleep 2
 		done
 	done
 done

PACKET_SIZE=( 128 256 384 512 640 768 896 1024 1152 1280 1408 1536 )
PROTOCOL=("TCP")


for prtcl in ${PROTOCOL[@]}; do
    for size in ${PACKET_SIZE[@]}; do
 		for run in {1..10}; do
 			echo "Evaluating IPv4 on ${prtcl}, ${size} bytes, run ${run} of 10"
 			ITGSend -a 192.168.30.2 -T ${prtcl} -c ${size} -C 10000000 -t 10000 -x logs/ipv4_${prtcl,,}_${size}_${run}.log
 		done
        wait
 	done
 done

# ONLY Test for TCP

# PACKET_SIZE=( 128 256 384 512 640 768 896 1024 1152 1280 1408 1536 )
# PROTOCOL=("TCP")

# for prtcl in ${PROTOCOL[@]}; do
# 	for size in ${PACKET_SIZE[@]}; do
# 		for run in {1..10}; do
# 			echo "Evaluating IPv4 on ${prtcl}, ${size} bytes, run ${run} of 10"
# 			ITGSend -a 192.168.30.2 -T ${prtcl} -c ${size} -C 1000000 -t 10000 -x logs/ipv4_${prtcl,,}_${size}_${run}.log
# 			sleep 2
# 		done
# 	done
# done