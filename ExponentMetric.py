import os,sys

import numpy as np
import matplotlib.pyplot as plt
def main(modelname,power,metric):
	print("%f" % power)
	#sys.exit(-1)
	fileName = "ExpMetric"+str(modelname)+str(metric)+".txt"
	data = np.loadtxt("paramTraces_"+str(modelname)+".txt",skiprows =1)
	data = -data[:,1]
	dataov = np.loadtxt("OptimalValue_"+str(modelname)+'.txt')
	var = np.power(dataov,1)/np.std(np.power(data,power))
	if os.path.exists(fileName):
		append_write = 'a' # append if already exists
	else:
		append_write = 'w' # make a new file if not
	metric = open(fileName,append_write)
	metric.write("%i %5.6e %5.6e %.6e %.6e\n" %(power,np.max(var),np.min(var), np.std(data),np.std(dataov)))
	metric.close()

def plotGp():
	data1 = np.loadtxt('ExpMetricpcurve.txt')
	data2 = np.loadtxt('ExpMetricalpcurve.txt')
	data3 = np.loadtxt('ExpMetrickarumoto.txt')
	data4 = np.loadtxt('ExpMetrickseller.txt')
	data5 = np.loadtxt('ExpMetricEL.txt')
	data6 = np.loadtxt('ExpMetricrefKuromoto.txt')
	fig =plt.figure(figsize =(12,9))
	ax = plt.subplot(2,3,1)
	ax.plot(data1[:,0],data1[:,1],'bo',markersize = 3)
	ax.set_xlabel('Power')
	ax.set_ylabel('max', color = 'b')
	ax.set_title('pcurve')

	ax1=ax.twinx()
	ax1.plot(data1[:,0],data1[:,2],'r^',markersize = 3)
	ax1.set_xlabel('Power')
	ax1.set_ylabel('min',color='r')

	ax = plt.subplot(2,3,2)
	ax.plot(data2[:,0],data2[:,1],'bo',markersize = 3)
	ax.set_xlabel('Power')
	ax.set_ylabel('max', color = 'b')
	ax.set_title('alpcurve')

	ax1=ax.twinx()
	ax1.plot(data2[:,0],data2[:,2],'r^',markersize = 3)
	ax1.set_xlabel('Power')
	ax1.set_ylabel('min',color='r')

	ax = plt.subplot(2,3,3)
	ax.plot(data3[:,0],data3[:,1],'bo',markersize = 3)
	ax.set_xlabel('Power')
	ax.set_ylabel('max', color = 'b')
	ax.set_title('karumoto')

	ax1=ax.twinx()
	ax1.plot(data3[:,0],data3[:,2],'r^',markersize = 3)
	ax1.set_xlabel('Power')
	ax1.set_ylabel('min',color='r')

	ax = plt.subplot(2,3,4)
	ax.plot(data4[:,0],data4[:,1],'bo',markersize = 3)
	ax.set_xlabel('Power')
	ax.set_ylabel('max', color = 'b')
	ax.set_title('kseller')

	ax1=ax.twinx()
	ax1.plot(data4[:,0],data4[:,2],'r^',markersize = 3)
	ax1.set_xlabel('Power')
	ax1.set_ylabel('min',color='r')

	ax = plt.subplot(2,3,5)
	ax.plot(data5[:,0],data5[:,1],'bo',markersize = 3)
	ax.set_xlabel('Power')
	ax.set_ylabel('max', color = 'b')
	ax.set_title('EL')

	ax1=ax.twinx()
	ax1.plot(data5[:,0],data5[:,2],'r^',markersize = 3)
	ax1.set_xlabel('Power')
	ax1.set_ylabel('min',color='r')

	ax = plt.subplot(2,3,6)
	ax.plot(data6[:,0],data6[:,1],'bo',markersize = 3)
	ax.set_xlabel('Power')
	ax.set_ylabel('max')
	ax.set_title('Reform Karumote')

	ax1=ax.twinx()
	ax1.plot(data6[:,0],data6[:,2],'r^',markersize = 3)
	ax1.set_xlabel('Power')
	ax1.set_ylabel('min',color='r')

	plt.tight_layout()
	plt.savefig('Metric.pdf')
	plt.show()
if __name__ == '__main__':
	main(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
	
	#plotGp()    
