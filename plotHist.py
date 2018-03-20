#imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from res_3R5P import eval
def plotres():
	#load data
	x = np.loadtxt('paramTraces_bvp.txt',skiprows=1)
	res = np.empty([x.shape[0],24])
	for i in range(x.shape[0]):
		res[i,:]=eval(x[i,2:])
	num_bins = 100

	# the histogram of the data
	plt.figure(figsize=(12,8))
	for i in range(24):

		ax = plt.subplot(4,6,i+1)
		n, bins, patches = ax.hist(res[:,i], num_bins, normed=1, facecolor='blue', alpha=0.5)
		# Tweak spacing to prevent clipping of ylabel

		plt.subplots_adjust(left=0.15)

	 
	plt.title(r'Histogram of function residue')
	plt.tight_layout() 
	plt.show()
def plotfval():
	x = np.loadtxt('paramTraces_bvp.txt',skiprows=1)
	x = x[:,1]
	num_bins =100
	n,bins,patches = plt.hist(x,num_bins,normed=1,facecolor = 'blue',alpha=0.5)
	plt.subplots_adjust(left = 0.15)
	plt.title('Histogram of function value')
	plt.show()

if __name__ == '__main__':
	plotfval()
