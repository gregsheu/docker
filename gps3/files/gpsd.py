from gps3 import gps3
from time import sleep
import os
import socket
gps_socket = gps3.GPSDSocket()
h = os.environ["GPSD_HOST"]
ip = socket.gethostbyname(h)
data_stream = gps3.DataStream()
gps_socket.connect(ip, "2947")
#gps_socket.connect()
gps_socket.watch()
sleep(10)
for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        v = data_stream.TPV['speed']
        w = data_stream.TPV['alt']
        x = data_stream.TPV['time']
        y = data_stream.TPV['lat']
        z = data_stream.TPV['lon']
    if x != "n/a":
        print('Speed = %s' % v)
        print('Altitude = %s' % w)
        print('Time = %s' % x)
        print('Latitude = %s' % y)
        print('Longitude = %s' % z)
        f = open("coords.txt", "a")
        f.write("At time %s, Latitude %s, Longitude %s, Altitude %s, Speed %s\n" % (x, y, z, w, v))
        sleep(1)
        break
