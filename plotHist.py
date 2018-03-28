#imports
import os,sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from res_3R5P import eval
import pandas
import seaborn as sns

def plotres():
	#load data
	x = np.loadtxt('Datafiles/paramTraces_3R5P.txt',skiprows=1)
	res = np.empty([x.shape[0],24])
	for i in range(x.shape[0]):
		res[i,:]=eval(x[i,2:])
	num_bins = 100

	# the histogram of the data
	plt.figure(figsize=(12,8))
	for i in range(24):

		ax = plt.subplot(4,6,i+1)
		n, bins, patches = ax.hist(res[:,i], num_bins, normed=0, facecolor='blue', alpha=0.5)
		# Tweak spacing to prevent clipping of ylabel

		plt.subplots_adjust(left=0.15)

	 
	plt.title(r'Histogram of function residue')
	plt.tight_layout() 
	plt.show()
def plotfval(model):
	path = str(os.getcwd())+'/Graphes'
	x = np.loadtxt('Datafiles/paramTraces_'+str(model)+'.txt',skiprows=1)
	x = x[:,1]
	num_bins =100
	n,bins,patches = plt.hist(x,num_bins,normed=1,facecolor = 'blue',alpha=0.5)
	plt.subplots_adjust(left = 0.15)
	plt.title('Histogram of function value')
	plt.savefig('Graphes/Distribution_%s.pdf' %model)
	plt.show()
def plotbox(res,var):
	#load data
	# x = np.loadtxt('Datafiles/paramTraces_3R5P.txt',skiprows=1)
	
	# res = np.empty([x.shape[0],24])
	# for i in range(x.shape[0]):
	# 	res[i,:]=eval(x[i,2:])
	#Create data frame
	resdf = pandas.DataFrame(res)
	#colname =["e1","e2","e3","e4","e5","e6","e7","e8","e9",'e10',"e11","e12","e13","e14","e15","e16","e17","e18","e19",'e20','e21','e22','e23','e24']
	colname =["e1","e2","e3","e4","e5","e6","e7","e8","e9",'e10',"e11","e12","e13","e14","e15","e16","e17","e18","e19",'e20','e21','e22','e23','e24']
	resdf.columns = colname
	sns.set_style("whitegrid")
	ax = sns.boxplot(data = resdf)
	ax.set(xlabel='equation',ylabel='residue',title="Residue Distribution %d" %var)
	plt.savefig('Graphes/Res_3R5P_%d.pdf' %var)

	#plt.show()

# if __name__ == '__main__':
# 	#plotfval('alpcurve')
# 	#plotres()
# 	plotbox()
