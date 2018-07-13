#!/usr/bin/env bash

# Only run if not already running
procnum=$(ps -ef | grep "altered.py" | grep -v grep | wc -l)
if [ $procnum -ge 1 ];
then
    exit 0
fi

RC=1

echo $continue
while [ $RC == 1 ]
do
    echo "Altered starting..."
    python3 -m Altered.altered
    RC=$?
done

