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
main.py optimizes a generic objective function (objective.py).
The parameters for the first (second) optimization are in 1(2).option.
