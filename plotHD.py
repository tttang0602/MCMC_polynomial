import matplotlib.pyplot as plt
import numpy as np 
import os
import math
def plothd(model,frame):
	data = np.loadtxt('OptimalPoints_'+str(model)+'.txt',skiprows=0)
	val =  np.loadtxt('OptimalValue_'+str(model)+'.txt',skiprows=0)
	#data =  np.loadtxt('sol_3R5P.txt')
	#data = data[:30000,2:]
	if os.path.isfile(str(model)+'.txt'):
		sol = np.loadtxt(str(model)+'.txt')
	nvar = data.shape[1]
	fig = plt.figure(figsize=(int(nvar/frame),frame))
	print(data.shape)
	for i in range(int(nvar/2)):
		ax =  plt.subplot(frame,int(math.ceil(nvar/(2*frame))),i+1)
		ax.plot(data[:,2*i],data[:,2*i+1],'bo',alpha=0.5)
		if 'sol' in locals():
			ax.plot(sol[2*i,:],sol[2*i+1,:],'r*',alpha=0.5)
	#	ax.set_xlabel('x%i' %(2*i+1))
	#	ax.set_ylabel('x%i' %(2*i+2))
	plt.tight_layout()
	#plt.savefig('Compare_3R5P_5.pdf')
	#plt.savefig('Opt_3R5P.pdf')
	plt.show()
if __name__ == '__main__':
	model = 'bvp'
	frame = 3
	#plothd(model,int(frame))
	data = np.loadtxt('paramTraces_bvp.txt',skiprows=1)
	data = data[1:100,2:]
	print(data.shape)
	fig = plt.figure()
	ax =  plt.subplot(1,1,1)
	x=np.linspace(0,1,21)
	for i in range(data.shape[0]):
		
		ax.plot(x,data[i,:])
	plt.show()
