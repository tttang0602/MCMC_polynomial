#!/bin/bash


# for i in 1 2 4 6 8 10 12 14 16 18 20
# do 
	
# 	mpiexec -n 3 python3 example_runMCMConModel.py input_pcurve.txt $((i))
# 	# Run Optimization with smaple method 1
# 	python3 example_optMCMConModel.py input_pcurve.txt $((i)) 1
# 	# save metric
# 	python3 ExponentMetric.py pcurve $((i)) 1
# 	# Run Optimization with sample method 2
# 	python3 example_optMCMConModel.py input_pcurve.txt $((i)) 2
	
# 	# save metric
# 	python3 ExponentMetric.py pcurve $((i)) 2
# done

# for i in 1 2 4 6 8 10 12 14 16 18 20
# do 
	
# 	mpiexec -n 3 python3 example_runMCMConModel.py input_karumoto.txt $((i))
# 	# Run Optimization with smaple method 1
# 	python3 example_optMCMConModel.py input_karumoto.txt $((i)) 1
# 	# save metric
# 	python3 ExponentMetric.py karumoto $((i)) 1
# 	# Run Optimization with smaple method 2
# 	python3 example_optMCMConModel.py input_karumoto.txt $((i)) 2
# 	# save metric
# 	python3 ExponentMetric.py karumoto $((i)) 2
# done

# for i in 1 2 4 6 8 10 12 14 16 18 20
# do 
	
# 	mpiexec -n 3 python3 example_runMCMConModel.py input_kseller.txt $((i))
# 	# Run Optimization with smaple method 1
# 	python3 example_optMCMConModel.py input_kseller.txt $((i)) 1
# 	# save metric
# 	python3 ExponentMetric.py kseller $((i)) 1
# 	# Run Optimization with smaple method 2
# 	python3 example_optMCMConModel.py input_kseller.txt $((i)) 2
# 	# save metric
# 	python3 ExponentMetric.py kseller $((i)) 2
# done

# for i in 1 2 4 6 8 10 12 14 16 18 20
# do 
	
# 	mpiexec -n 3 python3 example_runMCMConModel.py input_refKuromoto.txt $((i))
# 	# Run Optimization
# 	python3 example_optMCMConModel.py input_refKuromoto.txt $((i)) 1
# 	# save metric
# 	python3 ExponentMetric.py refKuromoto $((i)) 1
# 	# Run Optimization
# 	python3 example_optMCMConModel.py input_refKuromoto.txt $((i)) 2
# 	# save metric
# 	python3 ExponentMetric.py refKuromoto $((i)) 2
# done

# for i in 1 2 4 6 8 10 12 14 16 18 20
# do 
	
# 	mpiexec -n 3 python3 example_runMCMConModel.py input_alpcurve.txt $((i))
# 	# Run Optimization
# 	python3 example_optMCMConModel.py input_alpcurve.txt $((i)) 1
# 	# save metric
# 	python3 ExponentMetric.py alpcurve $((i)) 1	
# 	# Run Optimization
# 	python3 example_optMCMConModel.py input_alpcurve.txt $((i)) 2
# 	# save metric
# 	python3 ExponentMetric.py alpcurve $((i)) 2

# done

# for i in 3 4 5
# do 
	
# 	mpiexec -n 3 python3 example_runMCMConModel.py input_EL.txt $((i))
# 	# Run Optimization
# 	python3 example_optMCMConModel.py input_EL.txt $((i)) 1
# 	# save metric
# 	python3 ExponentMetric.py EL $((i)) 1
# 	# Run Optimization
# 	python3 example_optMCMConModel.py input_EL.txt $((i)) 2
# 	# save metric
# 	python3 ExponentMetric.py EL $((i)) 2
# done

for i in 3 
do 
	
	#mpiexec -n 3 python3 example_runMCMConModel.py input_3R5P_opt.txt $((i))
	# Run Optimization
	python3 example_optMCMConModel.py input_3R5P_opt.txt $((i)) 2
	# save metric
	python3 ExponentMetric.py 3R5P $((i)) 2
done

# Plot Results for 2D Problems
# python3 showPoints2D.py

# Plot Results for 3D Problems
# python3 showPoints3D.py
