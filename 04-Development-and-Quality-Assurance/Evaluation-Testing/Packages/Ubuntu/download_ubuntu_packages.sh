#!/bin/bash

PACKAGES="d-itg libsctp1 chrony"

for pkg in $PACKAGES; do
  apt-get download -o APT::Architecture=amd64 ${pkg}:amd64
done
