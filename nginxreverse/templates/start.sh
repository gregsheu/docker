#!/bin/bash
sed -i "s/REPLACEME_NGINX/${HOST_NAME}/g" /etc/nginx/conf.d/default.conf
sed -i "s/REPLACEME_APACHE/${APACHE_HOST}/g" /etc/nginx/conf.d/default.conf
/usr/sbin/nginx -g 'daemon off;'
