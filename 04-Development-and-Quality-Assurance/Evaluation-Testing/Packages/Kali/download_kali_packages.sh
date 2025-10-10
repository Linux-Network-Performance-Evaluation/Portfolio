#!/bin/bash

PACKAGES="chrony netplan.io ethtool libglib2.0-0t64 libglib2.0-data libnetplan1 netplan-generator libatomic1 libglib2.0-data libyaml-0-2 python3-cffi-backend python3-linkify-it python3-markdown-it python3-mdurl python3-netplan python3-pygments python3-rich"

for pkg in $PACKAGES; do
  apt-get download -o APT::Architecture=amd64 ${pkg}:amd64
done