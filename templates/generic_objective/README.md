# Generic Objective
Template for serial optimization of a generic objective function

# Author
- Dr. Aristotelis P. Sgouros (arissgouros@gmail.com)

# Organization
The folder includes the following files and directories:
 - README       -> current file
 - objective.py -> implementation of the objective function
 - i.bound      -> bounds of the optimization
 - main.py      -> configuration of the optimizer
 - 1.option     -> first optimization parameters
 - 1.res.json   -> first optimization results
 - 1.log        -> first optimization log
 - 2.option     -> second optimization parameters
 - 2.res.json   -> second optimization results
 - 2.log        -> second optimization log
 - clean.sh     -> bash script for cleaning logs
 - run.sh       -> bash script for executing the optimization

# Notes
Optimize an objective function (OF) with arbitrary implementation (objective.py).
The OF constants are initialized before the optimization.

The parameters and bounds regarding the first (second) optimization are
in files 1(2).option and 1(2).bound, respectively.

First optimization:
   the OF is evaluated 5 times (randomly) within the specified bounds
   the OF is subjected to Bayesian Optimization for additional 5 steps
   the results are exported to file 1.res.json

Second optimization:
   the results of the first optimization are imported from file 1.res.json
   the OF is subjected to Bayesian Optimization for 10 steps
