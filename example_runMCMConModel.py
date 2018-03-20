# Imports
import sys,os
# Set library path
#sys.path.insert(0, '/afs/crc.nd.edu/group/tulip/01_code/01_tulip/tulipBIN/py')
sys.path.insert(0,'/home/tang/Documents/tulipBIN/py')
# Import UQ Library
import tulipUQ as uq
# Import Computational Model Library
import tulipCM as cm
# Import Data Library
import tulipDA as da
# Import Action Library
import tulipAC as ac
# Import Mat File From MATLAB
import scipy.io
import shutil
import numpy as np
from mpi4py import MPI

import time

t1=time.process_time()
# MAIN FUNCTION
def main(fileName,power,comm):
  
  # MPI Init
  rank = comm.Get_rank()
  size = comm.Get_size()

  # Set Model
  model = cm.cmBertiniSolverModel(fileName)

  modelType = fileName.split("_")[1]
  # SEt power
  model.setExponent(1/power)
  # add solution
  sol=uq.stdVec()
  
  # for loopA in range(9):
  #   sol.push_back(0.0)
  # model.addSolution(sol) # Set DREAM Parameters
 
  totChains         = size
  totGenerations    = 30000
  totalCR           = 3
  totCrossoverPairs = 5
  dreamGRThreshold  = 1.2
  dreamJumpStep     = 10
  dreamGRPrintStep  = 10

  # Set OUTPUT Files
  dreamChainFileName = 'chain_GR_000000.txt'
  dreamGRFileName    = 'gr_GR.txt'

  # Set Restart File
  # No restart Simulation
  dreamRestartReadFileName = '';
  # string dreamRestartReadFileName = "restart_read_GR.txt";
  # Write restart file just in case
  dreamRestartWriteFileName = 'restart_write_GR.txt'

  # Set Prior Information
  usePriorFromFile = False
  priorFileName = ''
  priorModelType = 0

  # Initialize DREAM Action
  dream = ac.acActionDREAM(totChains,
                           totGenerations,
                           totalCR,
                           totCrossoverPairs,
                           dreamChainFileName,
                           dreamGRFileName,
                           dreamGRThreshold,
                           dreamJumpStep,
                           dreamGRPrintStep,
                           dreamRestartReadFileName,
                           dreamRestartWriteFileName,
                           usePriorFromFile,
                           priorFileName,
                           priorModelType)

  # Set Model
  dream.setModel(model)

  # Run MCMC Simulation
  dream.go()

  # Add Barrier
  comm.Barrier()

  # Post Process the Results
  if(rank == 0):
    debugMode = False
    burnInPercent = 0.1
    dream.postProcess(debugMode,burnInPercent);
     # Rename File
    shutil.move('paramTraces.txt','Datafiles/paramTraces_' + str(modelType))


# ====
# MAIN
# ====
if __name__ == "__main__":

  # Init MPI
  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()
  size = comm.Get_size()

  # Run Main Function
  main(sys.argv[1],int(sys.argv[2]),comm)
  print(time.process_time()-t1)
