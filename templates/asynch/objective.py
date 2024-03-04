import os
import sys
import time
p1 = None
p2 = None
file = None

# Initialize contant parameters of the objective function
def Init(pp):
   global p1
   global p2
   global file
   p1, p2 = 1.0, 1.0
   file = pp['flag']
   return

def Function(**xx):
   check_every = 0.25
   os.system('nohup python simulate.py %f %f %f %f %s &' % (xx['x'], xx['y'], p1, p2, file))
   while True:
      time.sleep(check_every)
      if not os.path.isfile(file):
         print('   waiting sim %s ..' % (file))
         continue
      time.sleep(0.05)
      with open(file, 'r') as foo:
         res = float(foo.readline().split()[0])
      break
   os.system('rm %s' % (file))
   return res
