#!/bin/bash

PACKAGES="d-itg libsctp1 frr frr-pythontools libcares2 libyang2t64"

if [[ ! -d ubuntu_packages ]]; do
	mkdir -p ubuntu_packages
fi
pushd ubuntu_packages

for pkg in $PACKAGES; do
  apt-get download ${pkg}
done

popd
