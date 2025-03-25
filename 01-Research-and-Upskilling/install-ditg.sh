#! /bin/bash

sudo dnf upgrade -y
sudo dnf install -y gcc-c++ libpcap-devel
git clone https://github.com/jbucar/ditg.git
cd ditg/src
make
sudo make install