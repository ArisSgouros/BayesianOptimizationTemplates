import numpy as np
import os
import sys
import json

def ParseBound(file):
   bounds = {}
   with open(file, 'r') as foo:
      while True:
         line = foo.readline()
         if not line: break
         lst = line.split()
         key, min_, max_ = lst[0], float(lst[1]), float(lst[2])
         bounds[key] = (min_, max_)
   return bounds

if __name__ == "__main__":

   # Optionaly read bounds and print results within this range
   bounds = {}
   if len(sys.argv) > 1:
      bounds = ParseBound(sys.argv[1])
      for key in bounds:
         print(key, bounds[key][0], bounds[key][1])
   bound_constrain = bool(bounds)

   # Merge the outputs to a single file and read
   file_res_all = 'tmp'
   os.system('cat *.json > ' + file_res_all)
   with open(file_res_all, 'r') as foo:
      lines = foo.readlines()
   os.system('rm tmp')

   # Read and filter the results
   results = {}
   for line in lines:
      js = json.loads(line)

      # Filter the cases outside the bounds
      if bound_constrain:
         skip = False
         for pkey in js['params']:
            if not (bounds[pkey][0] < js['params'][pkey] < bounds[pkey][1]):
               skip = True
         if skip:
            continue

      # Filter duplicates by setting key to target
      res_key = js['target']
      results[res_key] = js

   # Export the results
   for result in results.values():
      print(result)
