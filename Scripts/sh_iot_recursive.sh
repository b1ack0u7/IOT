#!/bin/sh
PATH=/opt/someApp/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
sleep 1
while true
do
    nohup python3 /home/pi/Documents/IOT/recursive_time.py > /dev/null 2>&1 &
    sleep 15m
done

