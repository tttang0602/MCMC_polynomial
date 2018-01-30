#!/bin/bash

# Run MCMC
mpiexec -n 3 python3 example_runMCMConModel.py 0
mpiexec -n 3 python3 example_runMCMConModel.py 1
mpiexec -n 3 python3 example_runMCMConModel.py 2
mpiexec -n 3 python3 example_runMCMConModel.py 7


# Run Optimization
python3 example_optMCMConModel.py 0
python3 example_optMCMConModel.py 1
python3 example_optMCMConModel.py 2
python3 example_optMCMConModel.py 7


# Plot Results
python3 showPoints.py
