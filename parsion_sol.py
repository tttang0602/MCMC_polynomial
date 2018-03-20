 #imports 

import sys, os
#sys.path.insert(0, '/afs/crc.nd.edu/group/tulip/01_code/01_tulip/tulipBIN/py')
import numpy as np


def regdis(ndata):
	# resolution parameters
	res = 1.0e-3

	mind = 1.0e-2

	# fidn range of data

	d = np.ptp(ndata)
	xmin_out = []
	xmax_out = []
	xcent = []
	if d < mind:
		return np.mean(ndata)
	else:
		# determine whether to divide further ornot
		while d > mind:
			xmin = np.min(ndata)
			xmax = np.max(ndata)
			xmin_data = ndata[ndata < xmin + 2*res]
			xmax_data = ndata[ndata > xmax - 2*res]
			xmin_out.append(np.mean(xmin_data))
			xmax_out.append(np.mean(xmax_data)) 
			ndata = ndata[(ndata < xmax - 2*res) & (ndata > xmin + 2*res)]
			if ndata.shape[0] > 0:
				d = np.ptp(ndata)
				if d < mind:
					xcent.append(np.mean(ndata))
				else:
					continue
			else:
				break
		dif_norm = np.hstack((xmin_out,xcent,xmax_out)).ravel()
		return (dif_norm, dif_norm.shape[0])

def delpt(point, fileName,res):
	flag = False
	if os.path.isfile(str(fileName)):

		ex_sol=np.loadtxt(str(fileName))
		nesol = len(open(str(fileName)).readlines())
		for  i in range(nesol):
			if nesol==1:
				sol1=ex_sol
			else:
				sol1 = ex_sol[i,:]
			if np.linalg.norm(point-sol1)<res:
				#print(np.linalg.norm(point-sol1))
				flag = True
				break
			else:
				continue
	return flag



def regmat(modeltype):
	fileName = 'sol_'+str(modeltype)
	#load optimal points
	data = np.loadtxt('Datafiles/OptimalPoints_'+str(modeltype))
	data_v = np.loadtxt('Datafiles/OptimalValue_'+str(modeltype)) 
	

	#data = np.loadtxt('r3R5P.txt')
	#data = np.transpose(data)
	# find norm of each point
	ndata = np.sum(data**2,axis=1)
	#nx, N = regdis(ndata)
	
	N=1
	res = 1.0e-2
	for i in range(N):
		#xdata = data[abs(ndata-nx[i])<*res,:]
		#xdata_v= data_v[abs(ndata-nx[i])<*res]
		#d1nx = regdis(xdata[:,0])
		xdata = data
		#xdata_v =  data_v
		Nx=xdata.shape[0]
		count =0
		while Nx>0:
			ind = [0]
			#ind=[np.argmin(xdata_v)];
			pt = xdata[ind,:]
			dpt = 0
			while delpt(pt,fileName,res):
				dpt += 1
				#print(pt)
				xdata = np.delete(xdata, ind,0)
				#xdata_v = np.delete(xdata_v,ind)

				Nx = xdata.shape[0]
				if Nx == 0:
					break
				#ind = [np.argmin(xdata_v)]
				ind =[0]
				pt = xdata[ind,:]
			print(dpt)	
			if Nx==0:
				continue

			for j in [n for n in range(Nx) if n!=ind]:
				if np.linalg.norm(xdata[j,:]-pt)< res:
					ind.append(j)
				else:
					continue
			#print(np.mean(xdata[ind,:],0))
			
			count += 1
			if os.path.exists(fileName):
				append_write = 'a'
			else:
				append_write = 'w'
			sol = open(fileName,append_write)
			np.savetxt(sol,np.mean(xdata[ind,:],0), fmt = '%.6e',newline = ' ')
			sol.write('\n')
			sol.close()
			xdata = np.delete(xdata,ind,0)
			#xdata_v = np.delete(xdata_v,ind)
			Nx=xdata.shape[0]
			#print(xdata.shape)
		print(count)
		try:
			os.remove(fileName)
		except OSError:
			pass
		return count

if __name__ == '__main__':
	
	regmat('3R5P.txt')


