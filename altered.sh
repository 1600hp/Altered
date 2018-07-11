#!/usr/bin/env bash

RC=1

echo $continue
while [ $RC == 1 ]
do
    echo "Altered starting..."
    ./altered.py
    RC=$?
done

