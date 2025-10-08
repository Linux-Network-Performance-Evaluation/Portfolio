#!/bin/bash

PACKET_SIZE=( 128 256 384 512 640 768 896 1024 1152 1280 1408 1536 )
PROTOCOL=("TCP" "UDP")

# Create logs directory if it doesn't exist
if [[ ! -d logs ]]; then
	mkdir -vp logs
fi

# Move to logs directory
pushd logs

for prtcl in ${PROTOCOL[@]}; do
	for size in ${PACKET_SIZE[@]}; do
		for run in {1..10}; do
			echo "Evaluating IPv6 on ${prtcl}, ${size} bytes, run ${run} of 10"
			ITGSend -a fd00:0:0:30::2 -T ${prtcl} -c ${size} -t 30000 -m rttm -l ipv6_${prtcl,,}_${size}_${run}_send.log -x ipv6_${prtcl,,}_${size}_${run}_recv.log
			sleep 2
		done
	done
done

# Return to origin directory
popd
