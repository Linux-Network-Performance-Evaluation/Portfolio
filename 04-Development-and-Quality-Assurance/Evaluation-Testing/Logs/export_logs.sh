#!/bin/bash

LOG_DIR="logs"
OUT_DIR="decoded_logs"
MAX_PARALLEL_JOBS=12

mkdir -p "$OUT_DIR"

job_count=0

for logfile in ${LOG_DIR}/ip*.log; do
    echo "Decoding $logfile..."
    ITGDec "$logfile" > "${OUT_DIR}/$(basename "$logfile" .log).txt" &

    ((job_count++))

    if [[ $job_count -ge $MAX_PARALLEL_JOBS ]]; then
        wait
        job_count=0
    fi
done

wait
echo "All logs decoded to ${OUT_DIR}"
