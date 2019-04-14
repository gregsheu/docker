#!/bin/bash
echo "export GPSD_HOST=$GPSD_HOST" >> /etc/environment
cron -f
