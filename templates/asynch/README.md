# Generic Objective
Template for parallel initial search and serial Bayesian optimization of a generic objective function

# Author
- Dr. Aristotelis P. Sgouros (arissgouros@gmail.com)

# Organization
The folder includes the following files and directories:
 - README              -> current file
 - objective.py        -> objective function
 - simulate.py         -> evaluation of the objective function
 - i.bound             -> bounds of the optimization
 - main.py             -> configuration of the optimizer
 - 1/2/3.option_random -> optimization parameter from init search 1/2/3
 - 1/2/3.res.json      -> results from init search 1/2/3
 - 123.res.json        -> results from init searches 1, 2 and 3
 - 4.option_bayes      -> parameters of the Bayesian optimization
 - 4.res.json          -> results from the Bayesian optimization
 - clean.sh            -> bash script for cleaning logs
 - run.sh              -> bash script for executing the optimization


# Notes
Concurrently conduct three random searches and subsequently perform Bayesian optimization.

Concurrent search:

 - Parameters for the three instances are in files 1/2/3.option_random.
 - Instances run in parallel (see run.sh).
 - Upon objective function evaluation, the simulate function is triggered.
 - After a brief delay, the simulate function exports the result to a specified file.
 - The objective function periodically checks for the file's presence; if it exists, it reads its content and retrieves the result for further processing.
Second optimization:

 - Merge results from the three concurrent searches into a single file.
 - Use the merged file as a starting point for the second Bayesian optimization.
