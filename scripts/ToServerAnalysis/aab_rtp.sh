#!/bin/bash


set -ex

# usage
USAGETXT=\
"
  Usage: $0 [options] <tpot script> <rtp file> <link type>
"
if [ $# -ne 32 ]; then
  abort "This script expects 2 arguments"
fi

if [ ! -f $1 ]; then
  abort "The first argument needs to be an existing file"
fi

if [ ! -f $2 ]; then
  abort "The first argument needs to be an existing file"
fi


# run
python $1 -f $2

