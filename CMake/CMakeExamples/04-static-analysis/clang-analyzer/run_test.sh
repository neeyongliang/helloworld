#!/bin/bash

# sudo apt install clang-tools-9

get_clang_tools=$(dpkg --get-selections | grep clang-tools-9)

if test -z "$get_clang_tools"; then
    echo "Current system cannot find clang-tools"
    exit 0;
else
    echo "Installed clang-tools"
fi

set -e

   mkdir -p build \
&& cd build \
&& scan-build-9 -o scanbuildout cmake .. \
&& scan-build-9 -o scanbuildout make