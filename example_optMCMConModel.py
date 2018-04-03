# Imports
import sys,os
sys.path.insert(0, '/home/tang/Documents/tulipBIN/py')
# Import UQ Library
import tulipUQ as uq
# Import Computational Model Library
import tulipCM as cm
# Import Data Library
import tulipDA as da
# Import Action Library
import tulipAC as ac
# Import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
import time
from parsion_sol import regmat
t1=time.process_time()
# MAIN FUNCTION
def main(fileName,power,metric):

  # Set Model
  model = cm.cmBertiniSolverModel(fileName)
  modelType = fileName.split("_")[1]
  print(modelType)
  # SEt power
  model.setExponent(1)
  # add solution
  #sol=uq.stdVec()

  # for loopA in range(9):
  #   sol.push_back(0.0)
  # model.addSolution(sol)
  
  # Set Optimizer Parameters
  # Convergence Tolerance
  convTol = 1.0e-10
  # Check Convergence every convUpdateIt iterations
  convUpdateIt = 1
  # Maximum Iterations
  maxOptIt = 5000
  # Coefficient for Step increments
  stepCoefficient = 0.01
  # Init Nelder-Mead Optimizer
  nm = ac.acActionOPT_NM(convTol,convUpdateIt,maxOptIt,stepCoefficient)
  # Set Model for Nelder-Mead Optimizer
  nm.setModel(model)

  # Total Number of iterations
  totInitialGuess = 100
  totRestarts     = 20

  # Read MCMC Samples and sub-samples using totInitialGuess
  #data = np.loadtxt('paramTraces.txt',skiprows=1)
  data = np.loadtxt('Datafiles/paramTraces_' + str(modelType),skiprows=1)
  # SubSample
  dist = np.exp(data[:,1])/np.sum(np.exp(data[:,1]))
  print(np.random.choice(data.shape[0], totInitialGuess,p=dist))
  if metric == 1:
    data = data[np.random.choice(data.shape[0], totInitialGuess),2:]
  else:
    data = data[np.random.choice(data.shape[0], totInitialGuess,p=dist),2:]

  # Loop over the randomly selected initial guess
  results = np.zeros((totInitialGuess,model.getParameterTotal()))
  Var = np.zeros(totInitialGuess)
  for loopA in range(totInitialGuess):
    # Get Model Limits
    x0 = data[loopA,:]
    np.savetxt('optParams.txt',x0)

    # Set Initial Guess Parameters
    useStartingParameterFromFile = True
    startFromCentre = False
    startParameterFile = 'optParams.txt'
    nm.setInitialParamGuess(useStartingParameterFromFile,startFromCentre,startParameterFile)

    # Nelder-Mead Optimiation with restart
    for loopB in range(totRestarts):      
      # Start Optimization    
      nm.go()
      # Restart
      if(loopB == 0):
        nm.setInitialPointFromFile(True)
        nm.setInitialPointFile('optParams.txt')

    # Read Optimal Parameters From File
    results[loopA,:] = np.loadtxt('optParams.txt')
    Var[loopA] = np.loadtxt("optValue.txt")

  # Save Final Result
  np.savetxt('Datafiles/OptimalPoints_' + str(modelType),results)
  np.savetxt('Datafiles/OptimalValue_' + str(modelType),Var)

  #calculate cpu time
  cputime = time.process_time()-t1
  nsol = regmat(modelType)
  print(cputime)
  file = "cputime_sol.txt"
  if os.path.exists(file):
    append_write = 'a' # append if already exists
  else:
    append_write = 'w' # make a new file if not
  cpu = open(file,append_write)
  cpu.write("%s %d %.f %.5f %d \n" %(modelType,metric,power,cputime,nsol))
  cpu.close() 
# ====
# MAIN
# ====
if __name__ == "__main__":
	
  main(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
  
