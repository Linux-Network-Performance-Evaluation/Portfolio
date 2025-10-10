#!/bin/bash

# Move to logs directory
pushd logs

if [[ ! -d delay ]]; then
	mkdir -vp delay
fi

if [[ ! -d jitter ]]; then
	mkdir -vp jitter
fi

if [[ ! -d packetloss ]]; then
	mkdir -vp packetloss
fi

if [[ ! -d throughput ]]; then
	mkdir -vp throughput
fi

for i in *.log; do
	echo "Exporting IPv4 TCP logs ${run} of 10"
	echo "Exporting TXT"
	ITGDec ${i} -l ${i%%.*}.txt;
	echo "Exporting DAT"
	ITGDec ${i} -o ${i%%.*}.dat;
	ITGDec ${i} -d 100 delay/${i%%.*}_delay.dat;
	ITGDec ${i} -j 100 jitter/${i%%.*}_jitter.dat;
	ITGDec ${i} -p 100 packetloss/${i%%.*}_packetloss.dat;
	ITGDec ${i} -b 100 throughput/${i%%.*}_throughput.dat;
done

# Return to origin directory
popd
