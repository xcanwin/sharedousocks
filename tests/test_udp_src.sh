#!/bin/bash

PYTHON="coverage run -a"

mkdir -p tmp

$PYTHON sharedousocks/local.py -c tests/aes.json -v &
LOCAL=$!

$PYTHON sharedousocks/server.py -c tests/aes.json --forbidden-ip "" -v &
SERVER=$!

sleep 3

python tests/test_udp_src.py
r=$?

kill -s SIGINT $LOCAL
kill -s SIGINT $SERVER

sleep 2

exit $r
