#!/bin/bash
sed -i "s/HOSTNAME/${HOSTNAME}/g" /etc/nginx/conf.d/default.conf
sed -i "s/PROXY_HOST/${PROXY_HOST}/g" /etc/nginx/conf.d/default.conf
/usr/sbin/nginx -g 'daemon off;'
