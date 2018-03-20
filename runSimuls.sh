#!/bin/bash

# Run MCMC
#mpiexec -n 3 python3 example_runMCMConModel.py input.txt

# Run Optimization
#python3 example_optMCMConModel.py input.txt


# for i in 2 4 8 16
# do 
	
# 	mpiexec -n 3 python3 example_runMCMConModel.py input_kseller.txt $((i))
# 	# Run Optimization
# 	python3 example_optMCMConModel.py input_kseller.txt $((i))
# 	# save metric
# 	python3 ExponentMetric.py kseller $((i))
# 	#echo 4/$i
# done

for i in 2 4 8 16
do 
	
	mpiexec -n 3 python3 example_runMCMConModel.py input_refKuromoto.txt $((i))
	# Run Optimization
	python3 example_optMCMConModel.py input_refKuromoto.txt $((i))
	# save metric
	python3 ExponentMetric.py refKuromoto $((i))
	#echo 4/$i
done

for i in 2 4 8 16
do 
	
	mpiexec -n 3 python3 example_runMCMConModel.py input_alpcurve.txt $((i))
	# Run Optimization
	python3 example_optMCMConModel.py input_alpcurve.txt $((i))
	# save metric
	python3 ExponentMetric.py alpcurve $((i))
	#echo 4/$i
done


# Plot Results for 2D Problems
# python3 showPoints2D.py

# Plot Results for 3D Problems
# python3 showPoints3D.py
