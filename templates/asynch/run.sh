#!/bin/bash

# Conduct 3 concurrent random searches
python main.py 1.option_random &
python main.py 2.option_random &
python main.py 3.option_random &
wait

# Merge the results to a single file
cat 1.res.json 2.res.json 3.res.json > 123.res.json

# Conduct the Bayesian optimization
python main.py 4.option_bayes
