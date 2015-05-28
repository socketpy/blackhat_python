#!/usr/bin/python

import sys, os, binascii

str_file = "sec_bin.txt"
output_file = "sec_bin.bin"

fd = open(str_file, "rt")
raw_str = fd.read()
fd.close()

fd = open(output_file, "wb")
for c in raw_str.split():
    c = binascii.unhexlify(c)
    fd.write(c)

fd.close()

