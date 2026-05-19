#!/bin/bash

SUBNET="192.168.1"
seq 1 254 | xargs -I{} -P 50 bash -c '
IP="'$SUBNET'.{}"

if ping -c 1 -W 1 "$IP" >/dev/null 2>&1; then
    echo "$IP is Up"
fi
'

# for i in {1..254}; do
# (
#     IP="$SUBNET.$i"

#     if ping -c 1 -W 1 "$IP" >/dev/null 2>&1; then
#         echo "$IP is UP"
#     fi
# ) &
# done
# wait