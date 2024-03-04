import sys
import argparse
import numpy as np
from bayes_opt import BayesianOptimization
from bayes_opt.logger import JSONLogger
from bayes_opt.event import Events
from bayes_opt.util import load_logs
from bayes_opt import UtilityFunction
import objective as obj

parser = argparse.ArgumentParser()
parser.add_argument('options', type=str, help='Path of the parameter file')

def ParseOptions(file):
   options = {}
   with open(file, 'r') as foo:
      while True:
         line = foo.readline()
         if not line: break
         if line[0] == '#': continue
         tmp = line.split()
         options[tmp[0]] = tmp[1]
   return options

def ParseBound(file):
   bounds = {}
   with open(file, 'r') as foo:
      while True:
         line = foo.readline()
         if not line: break
         lst = line.split()
         key, min_, max_ = lst[0], float(lst[1]), float(lst[2])
         bounds[key] = (min_, max_)

   # assign the proper variable types
   pp['seed'] = int(pp['seed'])
   pp['verbose'] = int(pp['verbose'])
   pp['xi'] = float(pp['xi'])
   pp['kappa'] = float(pp['kappa'])
   pp['alpha'] = float(pp['alpha'])
   pp['nsearch'] = int(pp['nsearch'])
   pp['nbayes'] = int(pp['nbayes'])
   return bounds

if __name__ == "__main__":
   pp = ParseOptions(parser.parse_args().options)
   print("Optimization parameters:")
   for key in pp:
      print("   ", key, pp[key])
        
   print("Reading bounds from: %s" % (pp['bounds']))
   pbounds = ParseBound(pp['bounds'])

   print("Objective function initialization..")
   obj.Init(pp)

   optimizer = BayesianOptimization(
      f=None,
      pbounds=pbounds,
      verbose=pp['verbose'],
      random_state=pp['seed'],
   )

   utility = UtilityFunction(kind=pp['kind'], kappa=pp['kappa'], xi=pp['xi'])

   # Export log
   if 'log_out' in pp:
      print('Exporting to %s:' % (pp['log_out']))
      logger = JSONLogger(path=pp['log_out'])
      optimizer.subscribe(Events.OPTIMIZATION_STEP, logger)

   # Import log
   if 'log_in' in pp:
      print('Importing from %s:' % (pp['log_in']))
      load_logs(optimizer, logs=[pp['log_in']]);

   # search section
   print('Random search for %d steps:' % (pp['nsearch']))
   np.random.seed(pp['seed'])
   for ii in range(pp['nsearch']):
      probe = {}
      for key in pbounds:
         min_ = pbounds[key][0]
         max_ = pbounds[key][1]
         probe[key] = np.random.uniform(min_, max_)
      target = obj.Function(**probe)
      optimizer.register(
         params=probe,
         target=target,
      )
      print('  ', probe, target)

   # optimization section
   print('Bayesian optimization for %d steps:' % (pp['nbayes']))
   for step in range(pp['nbayes']):
      probe = optimizer.suggest(utility)
      target = obj.Function(**probe)
      optimizer.register(
         params=probe,
         target=target,
      )
      print('  ', probe, target)

   probe, target = optimizer.max['params'], optimizer.max['target']
   print('Optimum probe:')
   for key in probe:
      print('   %s %f' % (key, probe[key]))
   print('Optimum value:\n  ', target)
