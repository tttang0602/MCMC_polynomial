# Imports
import sys
#sys.path.insert(0,'/home/tang/Documents/tulipBin/py')
import numpy as np
import matplotlib.pyplot as plt

def evalFunction(dim,first,second,X,Y,ex):

  res = np.zeros((dim,X.shape[0],X.shape[1]))
  var = [i for i in range(dim)]
  var[first] = X
  var[second] = Y
  for loopA in range(dim):
    if((loopA != first)and(loopA != second)):
      var[loopA] = ex[loopA,0]
      # var[loopA] = ex[loopA,1]
      # var[loopA] = 0.0

  res[0] = var[0]**(3.0)/10.0 + 2*var[0] - var[1] - var[2] - var[3] - var[6]
  res[1] = var[1]**(3.0)/10.0 + 2*var[1] - var[0] - var[2] - var[4] - var[7]
  res[2] = var[2]**(3.0)/10.0 + 2*var[2] - var[0] - var[1] - var[5] - var[8]
  res[3] = var[3]**(3.0)/10.0 + 2*var[3] - var[0] - var[4] - var[5] - var[6]
  res[4] = var[4]**(3.0)/10.0 + 2*var[4] - var[1] - var[3] - var[5] - var[7]
  res[5] = var[5]**(3.0)/10.0 + 2*var[5] - var[2] - var[3] - var[4] - var[8]
  res[6] = var[6]**(3.0)/10.0 + 2*var[6] - var[0] - var[3] - var[7] - var[8]
  res[7] = var[7]**(3.0)/10.0 + 2*var[7] - var[1] - var[4] - var[6] - var[8]
  res[8] = var[8]**(3.0)/10.0 + 2*var[8] - var[2] - var[5] - var[6] - var[7]

  result = np.power(np.sum(np.abs(res),axis=0),1.0)

  print(np.max(result))
  print(np.min(result))

  return result

def plotGraphs():

  # Set Number of Samples
  totSamples = 30000
  levels = np.array([0.0,1.0,10.0,100.0,500.0])

  # Read MCMC Sample Data
  data = np.loadtxt('Datafiles/paramTraces_EL.txt',skiprows=1)
  print(data.shape)
  data = data[:totSamples,2:11]

  #  Read Optimal Points
  opt = np.loadtxt('Datafiles/OptimalPoints_EL.txt')

  # Get Dimensions
  totDims = data.shape[1]

  exSol = np.zeros((totDims,2))
  exSol[:,0] = np.sqrt(20.0)
  exSol[:,1] = -np.sqrt(20.0)

  # Create Exact Surfaces
  delta = 0.025
  x = np.arange(-10.0, 10.0, delta)

  count = 0
  plt.figure(figsize=(7,7))
  for loopA in range(totDims-1):
    for loopB in range(loopA+1,totDims):
      count += 1

      X, Y = np.meshgrid(x, x)
      print(X.shape)
      print(Y.shape)      
      Z = evalFunction(totDims,loopA,loopB,X,Y,exSol)

      # Plot Figure
      #ax = plt.subplot(6,6,count)
      ax = plt.subplot(1,1,1)
      titleString = 'Slice for variables %d - %d' % (loopA,loopB)
      # ax.set_title(titleString)
      # ax.plot(data[:,loopA],data[:,loopB],'bo',markersize=1,alpha=0.5)
      ax.plot(opt[:,loopA],opt[:,loopB],'ro',markersize=3.5,alpha=0.5)
      ax.plot(np.sqrt(20),np.sqrt(20),'go',markersize=2,alpha=0.5)
      ax.plot(-np.sqrt(20),-np.sqrt(20),'go',markersize=2,alpha=0.5)
      cs = ax.contour(X, Y, Z, levels)
      ax.set_xlim([-10.0,10.0])
      ax.set_ylim([-10.0,10.0])
      plt.colorbar(cs)

      plt.show()
      sys.exit(-1)


  plt.tight_layout()
  plt.savefig('Graphes\sample_Distribution_randp.pdf')
  #plt.show()

# =============
# MAIN FUNCTION
# =============
if __name__ == "__main__":
  plotGraphs()