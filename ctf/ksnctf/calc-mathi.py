#! /usr/bin/python
from mathivar import *
import math
print n
print n * e

phi = (p - 1) * (q - 1)
d = invmodp(e, phi)
m = pow(c, d, n)

print("%0512x" %m).decode("hex")
