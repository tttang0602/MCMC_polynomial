# Imports
import sys,os
sys.path.insert(0,'/home/tang/Documents/tulipBin/py')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import pandas
import seaborn as sns


def cuberoot(x):
  if x>0:
    return math.pow(x,float(1)/3)
  elif x<0:
    return -math.pow(abs(x),float(1)/3)
  else:
    return 0
def plotGraphs():

  # Set Number of Samples
  totSamples = 20000
  
   # Read MCMC Sample Data
  data7 = np.loadtxt('paramTraces_07.txt',skiprows=1)
  data7 = data7[:totSamples,5:8]


  #  Read Optimal Points
  opt7 = np.loadtxt('OptimalPoints_07.txt')
  opt7s = opt7[:totSamples,0:3]
  opt7df = pandas.DataFrame(opt7)
  colname =["x1","x2","x3","x4","x5","x6","x7","x8","x9"]
  opt7df.columns = colname
  sns.set_style("whitegrid")
  ax = sns.stripplot(data = opt7df)
  ax.set(xlabel='variables',ylabel='solutions',title="M:50, MCMC_P:0.2, OPT_P:5")
  plt.show()
  sys.exit(-1) 
  fig = plt.figure()

  ax = fig.add_subplot(2,1,1,projection = '3d')
  ax.scatter(data7[:,0],data7[:,1],data7[:,2],c = 'b',marker = 'o')
  ax.set_xlim([-10,10])
  ax.set_ylim([-10,10])
  ax.set_zlim([-10,10])  
  ax.set_xlabel('x7')
  ax.set_ylabel('x8')
  ax.set_zlabel('x9') 

  ax = fig.add_subplot(2,1,2,projection = '3d')
  ax.scatter(opt7[:,0],opt7[:,1],opt7[:,2],c = 'r',marker = 'o')
  ax.set_xlim([-5,5])
  ax.set_ylim([-5,5])
  ax.set_zlim([-5,5])  
  ax.set_xlabel('x7')
  ax.set_ylabel('x8')
  ax.set_zlabel('x9') 

  plt.tight_layout()
  plt.show()
  #plt.savefig('sample_Distribution_Energy.pdf')
# =============
# MAIN FUNCTION
# =============
if __name__ == "__main__":
  plotGraphs()
