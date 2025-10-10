for i in 192.168.30.2*.log; do suffix="${i#192.168.30.2}"; mv "$i" "ipv4${suffix}"; done
