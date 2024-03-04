import sys
import time
x = float(sys.argv[1])
y = float(sys.argv[2])
p1 = float(sys.argv[3])
p2 = float(sys.argv[4])
file = sys.argv[5]
time.sleep(1)
with open (file,'w') as foo:
   res = -x ** 2 - (y - p1) ** 2 + p2
   foo.write("%15.7f" % (res))
