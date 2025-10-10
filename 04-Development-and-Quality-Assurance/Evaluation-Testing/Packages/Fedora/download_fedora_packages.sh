#!/bin/bash

PACKAGES="nano netplan netplan-default-backend-networkd chrony"

for pkg in $PACKAGES; do
  dnf download --resolve ${pkg}
done