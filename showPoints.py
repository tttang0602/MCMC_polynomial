# Imports
import sys,os
sys.path.insert(0,'/home/tang/Documents/tulipBin/py')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

def plotGraphs():

  # Set Number of Samples
  totSamples = 20000
  levels = np.array([0.0,0.01,0.2,0.4,0.6])

  # # Read MCMC Sample Data
  # data1 = np.loadtxt('paramTraces_01.txt',skiprows=1)
  # data1 = data1[:totSamples,2:]
  # data2 = np.loadtxt('paramTraces_02.txt',skiprows=1)
  # data2 = data2[:totSamples,2:]
  # data3 = np.loadtxt('paramTraces_03.txt',skiprows=1)
  # data3 = data3[:totSamples,2:]
  # data8 = np.loadtxt('paramTraces_08.txt',skiprows=1)
  # data8 = data8[:totSamples,4:]
  # print(data8.shape)
  
  #  ReadOptimal Points
  opt8 = np.loadtxt('Datafiles/OptimalPoints_refKuromoto.txt')
  # opt2 = np.loadtxt('OptimalPoints_02.txt')
  # opt3 = np.loadtxt('OptimalPoints_03.txt')
  # opt8 = np.loadtxt('OptimalPoints_08.txt')
  # opt8 = opt8[:totSamples,:]



  # Create Exact Surfaces
  delta = 0.025
  x = np.arange(-3.0, 3.0, delta)
  y = np.arange(-3.0, 3.0, delta)
  X, Y = np.meshgrid(x, y)
  Z1 = np.power(Y**2 + X**2*(X-1.0)*(X-2.0),5)
  Z2 = np.power(Y**2 - X**2*(X+1.0),5.0)
  t1 = np.arange(0.0, 2.0*np.pi, delta)
  t2 = np.arange(0.0, 2.0*np.pi, delta)
  T1, T2 = np.meshgrid(t1, t2)
  Z3 = np.power(np.abs(1.0/12.0 - 1.0/3.0*(np.sin(T1-T2)+np.sin(T1-0))) \
    + np.abs(-1.0/12.0-1.0/3.0*(np.sin(T2-T1)+np.sin(T2-0.0))),1/3.0)
  x8 = np.arange(-1,1,delta)
  X8, Y8 = np.meshgrid(x8,x8)
  Z8 = np.abs(1/12.0-1/3.0*(np.sqrt(1-X8**2)*Y8-np.sqrt(1-Y8**2)*X8+np.sqrt(1-X8**2))) \
      +np.abs(-1/12.0-1/3.0*(-np.sqrt(1-X8**2)*Y8+np.sqrt(1-Y8**2)*X8+np.sqrt(1-Y8**2))) \


 #  plt.figure(figsize=(8,6))
 #  ax = plt.subplot(2,3,1)
 #  ax.plot(data1[:,0],data1[:,1],'bo',markersize=1,alpha=0.5)
 #  ax.contour(X, Y, Z1, levels)
 #  ax.set_title('First Curve')
 #  ax.set_xlim([-3.0,3.0])
 #  ax.set_ylim([-3.0,3.0])

 #  ax = plt.subplot(2,3,2)
 #  ax.plot(data2[:,0],data2[:,1],'bo',markersize=1,alpha=0.5)
 #  ax.contour(X, Y, Z2, levels)
 #  ax.set_title('Alpha Curve')
 #  ax.set_xlim([-3.0,3.0])
 #  ax.set_ylim([-3.0,3.0])

 #  ax = plt.subplot(2,3,3)
 #  ax.plot(data3[:,0],data3[:,1],'bo',markersize=1,alpha=0.5)
 #  ax.contour(t1, t2, Z3, levels)
 #  ax.set_title('Kuramoto')
 #  ax.set_xlim([0,2*np.pi])
 #  ax.set_ylim([0,2*np.pi])

 #  ax = plt.subplot(2,3,4)
 #  ax.plot(opt1[:,0],opt1[:,1],'ro',markersize=4,alpha=0.6)
 #  ax.contour(X, Y, Z1, levels)
 #  ax.set_xlim([-3.0,3.0])
 #  ax.set_ylim([-3.0,3.0])

 #  ax = plt.subplot(2,3,5)
 #  ax.plot(opt2[:,0],opt2[:,1],'ro',markersize=4,alpha=0.6)
 #  ax.contour(X, Y, Z2, levels)
 #  ax.set_xlim([-3.0,3.0])
 #  ax.set_ylim([-3.0,3.0])

  ax = plt.subplot(2,3,6)
 
  #ax.plot(np.sin(opt3[:,0]),np.sin(opt3[:,1]),'ro',markersize=4,alpha=0.6)
  ax.plot((opt8[:,0]),(opt8[:,1]),'go',markersize=4,alpha=0.6)
  ax.contour(t1, t2, Z3, levels)
 
 # ax.set_xlim([0,2*np.pi])
 # ax.set_ylim([0,2*np.pi])
  ax.set_xlim([-1,1])
  ax.set_ylim([-1,1])

  plt.tight_layout()
  #plt.savefig('sample_Distribution.pdf')
  
  
  #sys.exit(-1)
  
  fig1 =plt.figure()
  # ax = fig1.add_subplot(2,1,1)
  # ax.plot(data8[:,0],data8[:,1],'bo',markersize=2,alpha=0.6)
  # ax.set_xlim([-1,1])
  # ax.set_ylim([-1,1])
  
  ax = fig1.add_subplot(2,1,2)
  ts1=opt8[:,0]**2+opt8[:,2]**2
  ts2=opt8[:,1]**2+opt8[:,3]**2
  ts3=abs(1/12-1/3*(opt8[:,0]*opt8[:,3]-opt8[:,1]*opt8[:,2]+opt8[:,0]))
  ts4=abs(-1/12-1/3*(-opt8[:,0]*opt8[:,3]+opt8[:,1]*opt8[:,2]+opt8[:,1]))
  print(ts3.shape)
  print(np.min(ts1[:]))
  print(np.min(ts2[:]))
  #sys.exit(-1)
  ax.plot(opt8[:,2],opt8[:,3],'ro')
  #ax.plot(ts3,ts4,'ro')
  #ax.contour(X8,Y8,Z8,levels)
  ax.set_xlim([-1,1])
  ax.set_ylim([-1,1])
  #ax.set_zlim([-5,0]) 
  plt.show()
  #plt.savefig('sample_Distribution_kKuReform.pdf')
# =============
# MAIN FUNCTION
# =============
if __name__ == "__main__":
  plotGraphs()
