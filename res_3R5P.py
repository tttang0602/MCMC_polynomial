#imports
import sys
import numpy as np
def eval(x):
#x= [-9.1211,-63.1593, 11.2619 ,-6.7541,-10.6480,-7.7532 , -0.4275, 3.2653,-4.2770  , -4.4717, 2.9986,-0.3877 , -4.8099, 1.5482, 1.8989 , -4.0426,-0.1579, 3.5735 , -3.9427, 3.4069,-1.4092 , 11.1844,-0.3805, 0.2417 ]
	eq0=(360068103073497*x[0])/562949953421312 - (646699436464773*x[1])/4503599627370496 - (6801955882546187*x[2])/9007199254740992 + x[6] - x[7]*((4011421025109373*x[21])/9007199254740992 + (3917882588037335*x[22])/4503599627370496 + (953798181242695*x[23])/4503599627370496) + x[4]*x[8] - x[5]*x[7] + x[8]*((5643401973270251*x[21])/9007199254740992 - (2124708325674519*x[22])/4503599627370496 + (2793926927604289*x[23])/4503599627370496) - 4678477199325511/562949953421312-((2745778666230729*x[1])/9007199254740992 - (3848861997237677*x[0])/9007199254740992 - (1916647451415159*x[2])/2251799813685248 + x[9] + x[11]*((1030466759136781*x[22])/2251799813685248 - (6467692325071979*x[21])/9007199254740992 + (2361609965354677*x[23])/4503599627370496) + x[4]*x[11] - x[5]*x[10] + x[10]*((2474108714284419*x[21])/4503599627370496 + (3761666852663765*x[22])/4503599627370496 + (105157783549861*x[23])/4503599627370496) - 595490718158377/70368744177664);
	eq1 =  (360068103073497*x[0])/562949953421312 - (646699436464773*x[1])/4503599627370496 - (6801955882546187*x[2])/9007199254740992 + x[6] - x[7]*((4011421025109373*x[21])/9007199254740992 + (3917882588037335*x[22])/4503599627370496 + (953798181242695*x[23])/4503599627370496) + x[4]*x[8] - x[5]*x[7] + x[8]*((5643401973270251*x[21])/9007199254740992 - (2124708325674519*x[22])/4503599627370496 + (2793926927604289*x[23])/4503599627370496) - 4678477199325511/562949953421312-(x[12] - (4486461901231217*x[1])/18014398509481984 - (4259418556632645*x[2])/4503599627370496 - (939011121326619*x[0])/4503599627370496 + x[4]*x[14] - x[5]*x[13] + x[14]*((8474315113308399*x[21])/18014398509481984 + (925812279892051*x[22])/1125899906842624 - (5768853634492921*x[23])/18014398509481984) - x[13]*((576104064033825*x[22])/1125899906842624 - (1930821824706939*x[21])/2251799813685248 + (244506939647561*x[23])/4503599627370496) - 577963622217163/70368744177664);
	eq2 =  (360068103073497*x[0])/562949953421312 - (646699436464773*x[1])/4503599627370496 - (6801955882546187*x[2])/9007199254740992 + x[6] - x[7]*((4011421025109373*x[21])/9007199254740992 + (3917882588037335*x[22])/4503599627370496 + (953798181242695*x[23])/4503599627370496) + x[4]*x[8] - x[5]*x[7] + x[8]*((5643401973270251*x[21])/9007199254740992 - (2124708325674519*x[22])/4503599627370496 + (2793926927604289*x[23])/4503599627370496) - 4678477199325511/562949953421312-((149274648555043*x[0])/562949953421312 - (1247527883733793*x[1])/2251799813685248 - (888502933164431*x[2])/1125899906842624 + x[15] - x[16]*((7197095429335159*x[21])/18014398509481984 + (7277931406853001*x[22])/9007199254740992 - (487528960626565*x[23])/1125899906842624) + x[17]*((1976038730956279*x[21])/2251799813685248 - (1805585700077849*x[22])/9007199254740992 + (3923497627643163*x[23])/9007199254740992) + x[4]*x[17] - x[5]*x[16] - 7442297553493539/1125899906842624);
	eq3 =  (360068103073497*x[0])/562949953421312 - (646699436464773*x[1])/4503599627370496 - (6801955882546187*x[2])/9007199254740992 + x[6] - x[7]*((4011421025109373*x[21])/9007199254740992 + (3917882588037335*x[22])/4503599627370496 + (953798181242695*x[23])/4503599627370496) + x[4]*x[8] - x[5]*x[7] + x[8]*((5643401973270251*x[21])/9007199254740992 - (2124708325674519*x[22])/4503599627370496 + (2793926927604289*x[23])/4503599627370496) - 4678477199325511/562949953421312-((1227582497165281*x[0])/2251799813685248 + (2441596289730149*x[1])/4503599627370496 - (5759577071777535*x[2])/9007199254740992 + x[18] + x[19]*((7105171699475349*x[21])/9007199254740992 - (664227429813961*x[22])/1125899906842624 + (776127648771713*x[23])/4503599627370496) + x[4]*x[20] - x[5]*x[19] + x[20]*((5112663859404875*x[21])/18014398509481984 + (2694781606089567*x[22])/4503599627370496 + (3374441207755167*x[23])/4503599627370496) - 2110676164742821/281474976710656);
	eq4 =   (5643401973270251*x[0])/9007199254740992 - (2124708325674519*x[1])/4503599627370496 + (2793926927604289*x[2])/4503599627370496 + x[7] + x[6]*((4011421025109373*x[21])/9007199254740992 + (3917882588037335*x[22])/4503599627370496 + (953798181242695*x[23])/4503599627370496) - x[3]*x[8] + x[5]*x[6] + x[8]*((646699436464773*x[22])/4503599627370496 - (360068103073497*x[21])/562949953421312 + (6801955882546187*x[23])/9007199254740992) + 8979997143696505/4503599627370496-((1030466759136781*x[1])/2251799813685248 - (6467692325071979*x[0])/9007199254740992 + (2361609965354677*x[2])/4503599627370496 + x[10] - x[3]*x[11] + x[5]*x[9] - x[9]*((2474108714284419*x[21])/4503599627370496 + (3761666852663765*x[22])/4503599627370496 + (105157783549861*x[23])/4503599627370496) + x[11]*((3848861997237677*x[21])/9007199254740992 - (2745778666230729*x[22])/9007199254740992 + (1916647451415159*x[23])/2251799813685248) - 8803061991350585/2251799813685248);
	eq5 =   (5643401973270251*x[0])/9007199254740992 - (2124708325674519*x[1])/4503599627370496 + (2793926927604289*x[2])/4503599627370496 + x[7] + x[6]*((4011421025109373*x[21])/9007199254740992 + (3917882588037335*x[22])/4503599627370496 + (953798181242695*x[23])/4503599627370496) - x[3]*x[8] + x[5]*x[6] + x[8]*((646699436464773*x[22])/4503599627370496 - (360068103073497*x[21])/562949953421312 + (6801955882546187*x[23])/9007199254740992) + 8979997143696505/4503599627370496-((8474315113308399*x[0])/18014398509481984 + (925812279892051*x[1])/1125899906842624 - (5768853634492921*x[2])/18014398509481984 + x[13] + x[14]*((939011121326619*x[21])/4503599627370496 + (4486461901231217*x[22])/18014398509481984 + (4259418556632645*x[23])/4503599627370496) - x[3]*x[14] + x[5]*x[12] + x[12]*((576104064033825*x[22])/1125899906842624 - (1930821824706939*x[21])/2251799813685248 + (244506939647561*x[23])/4503599627370496) - 5315294649462349/1125899906842624);
	eq6 =   (5643401973270251*x[0])/9007199254740992 - (2124708325674519*x[1])/4503599627370496 + (2793926927604289*x[2])/4503599627370496 + x[7] + x[6]*((4011421025109373*x[21])/9007199254740992 + (3917882588037335*x[22])/4503599627370496 + (953798181242695*x[23])/4503599627370496) - x[3]*x[8] + x[5]*x[6] + x[8]*((646699436464773*x[22])/4503599627370496 - (360068103073497*x[21])/562949953421312 + (6801955882546187*x[23])/9007199254740992) + 8979997143696505/4503599627370496-((1976038730956279*x[0])/2251799813685248 - (1805585700077849*x[1])/9007199254740992 + (3923497627643163*x[2])/9007199254740992 + x[16] + x[15]*((7197095429335159*x[21])/18014398509481984 + (7277931406853001*x[22])/9007199254740992 - (487528960626565*x[23])/1125899906842624) - x[3]*x[17] + x[5]*x[15] + x[17]*((1247527883733793*x[22])/2251799813685248 - (149274648555043*x[21])/562949953421312 + (888502933164431*x[23])/1125899906842624) + 8814605716093933/9007199254740992);
	eq7 =   (5643401973270251*x[0])/9007199254740992 - (2124708325674519*x[1])/4503599627370496 + (2793926927604289*x[2])/4503599627370496 + x[7] + x[6]*((4011421025109373*x[21])/9007199254740992 + (3917882588037335*x[22])/4503599627370496 + (953798181242695*x[23])/4503599627370496) - x[3]*x[8] + x[5]*x[6] + x[8]*((646699436464773*x[22])/4503599627370496 - (360068103073497*x[21])/562949953421312 + (6801955882546187*x[23])/9007199254740992) + 8979997143696505/4503599627370496-((5112663859404875*x[0])/18014398509481984 + (2694781606089567*x[1])/4503599627370496 + (3374441207755167*x[2])/4503599627370496 + x[19] - x[20]*((1227582497165281*x[21])/2251799813685248 + (2441596289730149*x[22])/4503599627370496 - (5759577071777535*x[23])/9007199254740992) - x[18]*((7105171699475349*x[21])/9007199254740992 - (664227429813961*x[22])/1125899906842624 + (776127648771713*x[23])/4503599627370496) - x[3]*x[20] + x[5]*x[18] + 2659496305705689/1125899906842624);
	eq8 =   (4011421025109373*x[0])/9007199254740992 + (3917882588037335*x[1])/4503599627370496 + (953798181242695*x[2])/4503599627370496 + x[8] + x[3]*x[7] - x[4]*x[6] - x[6]*((5643401973270251*x[21])/9007199254740992 - (2124708325674519*x[22])/4503599627370496 + (2793926927604289*x[23])/4503599627370496) - x[7]*((646699436464773*x[22])/4503599627370496 - (360068103073497*x[21])/562949953421312 + (6801955882546187*x[23])/9007199254740992) - 5095425119119635/1125899906842624-(x[11] - (3761666852663765*x[1])/4503599627370496 - (105157783549861*x[2])/4503599627370496 - (2474108714284419*x[0])/4503599627370496 - x[9]*((1030466759136781*x[22])/2251799813685248 - (6467692325071979*x[21])/9007199254740992 + (2361609965354677*x[23])/4503599627370496) + x[3]*x[10] - x[4]*x[9] - x[10]*((3848861997237677*x[21])/9007199254740992 - (2745778666230729*x[22])/9007199254740992 + (1916647451415159*x[23])/2251799813685248) - 4257470286518229/1125899906842624);
	eq9 =   (4011421025109373*x[0])/9007199254740992 + (3917882588037335*x[1])/4503599627370496 + (953798181242695*x[2])/4503599627370496 + x[8] + x[3]*x[7] - x[4]*x[6] - x[6]*((5643401973270251*x[21])/9007199254740992 - (2124708325674519*x[22])/4503599627370496 + (2793926927604289*x[23])/4503599627370496) - x[7]*((646699436464773*x[22])/4503599627370496 - (360068103073497*x[21])/562949953421312 + (6801955882546187*x[23])/9007199254740992) - 5095425119119635/1125899906842624-((576104064033825*x[1])/1125899906842624 - (1930821824706939*x[0])/2251799813685248 + (244506939647561*x[2])/4503599627370496 + x[14] - x[13]*((939011121326619*x[21])/4503599627370496 + (4486461901231217*x[22])/18014398509481984 + (4259418556632645*x[23])/4503599627370496) + x[3]*x[13] - x[4]*x[12] - x[12]*((8474315113308399*x[21])/18014398509481984 + (925812279892051*x[22])/1125899906842624 - (5768853634492921*x[23])/18014398509481984) - 8583953429733309/4503599627370496);
	eq10 =   (4011421025109373*x[0])/9007199254740992 + (3917882588037335*x[1])/4503599627370496 + (953798181242695*x[2])/4503599627370496 + x[8] + x[3]*x[7] - x[4]*x[6] - x[6]*((5643401973270251*x[21])/9007199254740992 - (2124708325674519*x[22])/4503599627370496 + (2793926927604289*x[23])/4503599627370496) - x[7]*((646699436464773*x[22])/4503599627370496 - (360068103073497*x[21])/562949953421312 + (6801955882546187*x[23])/9007199254740992) - 5095425119119635/1125899906842624-((7197095429335159*x[0])/18014398509481984 + (7277931406853001*x[1])/9007199254740992 - (487528960626565*x[2])/1125899906842624 + x[17] - x[15]*((1976038730956279*x[21])/2251799813685248 - (1805585700077849*x[22])/9007199254740992 + (3923497627643163*x[23])/9007199254740992) + x[3]*x[16] - x[4]*x[15] - x[16]*((1247527883733793*x[22])/2251799813685248 - (149274648555043*x[21])/562949953421312 + (888502933164431*x[23])/1125899906842624) - 8931778261037253/1125899906842624);
	eq11 =   (4011421025109373*x[0])/9007199254740992 + (3917882588037335*x[1])/4503599627370496 + (953798181242695*x[2])/4503599627370496 + x[8] + x[3]*x[7] - x[4]*x[6] - x[6]*((5643401973270251*x[21])/9007199254740992 - (2124708325674519*x[22])/4503599627370496 + (2793926927604289*x[23])/4503599627370496) - x[7]*((646699436464773*x[22])/4503599627370496 - (360068103073497*x[21])/562949953421312 + (6801955882546187*x[23])/9007199254740992) - 5095425119119635/1125899906842624-((664227429813961*x[1])/1125899906842624 - (7105171699475349*x[0])/9007199254740992 - (776127648771713*x[2])/4503599627370496 + x[20] + x[19]*((1227582497165281*x[21])/2251799813685248 + (2441596289730149*x[22])/4503599627370496 - (5759577071777535*x[23])/9007199254740992) + x[3]*x[19] - x[4]*x[18] - x[18]*((5112663859404875*x[21])/18014398509481984 + (2694781606089567*x[22])/4503599627370496 + (3374441207755167*x[23])/4503599627370496) + 2613587444270205/4503599627370496);
	eq12 =   x[3]*x[6]+x[4]*x[7]+x[5]*x[8]-(x[3]*x[9]+x[4]*x[10]+x[5]*x[11]);
	eq13 =   x[3]*x[6]+x[4]*x[7]+x[5]*x[8]-(x[3]*x[12]+x[4]*x[13]+x[5]*x[14]);
	eq14 =   x[3]*x[6]+x[4]*x[7]+x[5]*x[8]-(x[3]*x[15]+x[4]*x[16]+x[5]*x[17]);
	eq15 =   x[3]*x[6]+x[4]*x[7]+x[5]*x[8]-(x[3]*x[18]+x[4]*x[19]+x[5]*x[20]);
	eq16 =   x[6]**2+x[7]**2+x[8]**2-(x[9]**2+x[10]**2+x[11]**2);
	eq17 =   x[6]**2+x[7]**2+x[8]**2-(x[12]**2+x[13]**2+x[14]**2);
	eq18 =   x[6]**2+x[7]**2+x[8]**2-(x[15]**2+x[16]**2+x[17]**2);
	eq19 =   x[6]**2+x[7]**2+x[8]**2-(x[18]**2+x[19]**2+x[20]**2);
	eq20 =   x[22]*((646699436464773*x[6])/4503599627370496 + (2124708325674519*x[7])/4503599627370496 - (3917882588037335*x[8])/4503599627370496) - x[21]*((360068103073497*x[6])/562949953421312 + (5643401973270251*x[7])/9007199254740992 + (4011421025109373*x[8])/9007199254740992) - x[23]*((2793926927604289*x[7])/4503599627370496 - (6801955882546187*x[6])/9007199254740992 + (953798181242695*x[8])/4503599627370496)-(x[21]*((3848861997237677*x[9])/9007199254740992 + (6467692325071979*x[10])/9007199254740992 + (2474108714284419*x[11])/4503599627370496) + x[23]*((1916647451415159*x[9])/2251799813685248 - (2361609965354677*x[10])/4503599627370496 + (105157783549861*x[11])/4503599627370496) - x[22]*((2745778666230729*x[9])/9007199254740992 + (1030466759136781*x[10])/2251799813685248 - (3761666852663765*x[11])/4503599627370496));
	eq21 =   x[22]*((646699436464773*x[6])/4503599627370496 + (2124708325674519*x[7])/4503599627370496 - (3917882588037335*x[8])/4503599627370496) - x[21]*((360068103073497*x[6])/562949953421312 + (5643401973270251*x[7])/9007199254740992 + (4011421025109373*x[8])/9007199254740992) - x[23]*((2793926927604289*x[7])/4503599627370496 - (6801955882546187*x[6])/9007199254740992 + (953798181242695*x[8])/4503599627370496)-(x[21]*((939011121326619*x[12])/4503599627370496 - (8474315113308399*x[13])/18014398509481984 + (1930821824706939*x[14])/2251799813685248) + x[23]*((4259418556632645*x[12])/4503599627370496 + (5768853634492921*x[13])/18014398509481984 - (244506939647561*x[14])/4503599627370496) - x[22]*((925812279892051*x[13])/1125899906842624 - (4486461901231217*x[12])/18014398509481984 + (576104064033825*x[14])/1125899906842624));
	eq22 =   x[22]*((646699436464773*x[6])/4503599627370496 + (2124708325674519*x[7])/4503599627370496 - (3917882588037335*x[8])/4503599627370496) - x[21]*((360068103073497*x[6])/562949953421312 + (5643401973270251*x[7])/9007199254740992 + (4011421025109373*x[8])/9007199254740992) - x[23]*((2793926927604289*x[7])/4503599627370496 - (6801955882546187*x[6])/9007199254740992 + (953798181242695*x[8])/4503599627370496)-(x[22]*((1247527883733793*x[15])/2251799813685248 + (1805585700077849*x[16])/9007199254740992 - (7277931406853001*x[17])/9007199254740992) - x[21]*((149274648555043*x[15])/562949953421312 + (1976038730956279*x[16])/2251799813685248 + (7197095429335159*x[17])/18014398509481984) + x[23]*((888502933164431*x[15])/1125899906842624 - (3923497627643163*x[16])/9007199254740992 + (487528960626565*x[17])/1125899906842624));
	eq23=  x[22]*((646699436464773*x[6])/4503599627370496 + (2124708325674519*x[7])/4503599627370496 - (3917882588037335*x[8])/4503599627370496) - x[21]*((360068103073497*x[6])/562949953421312 + (5643401973270251*x[7])/9007199254740992 + (4011421025109373*x[8])/9007199254740992) - x[23]*((2793926927604289*x[7])/4503599627370496 - (6801955882546187*x[6])/9007199254740992 + (953798181242695*x[8])/4503599627370496)-(x[23]*((5759577071777535*x[18])/9007199254740992 - (3374441207755167*x[19])/4503599627370496 + (776127648771713*x[20])/4503599627370496) - x[21]*((1227582497165281*x[18])/2251799813685248 + (5112663859404875*x[19])/18014398509481984 - (7105171699475349*x[20])/9007199254740992) - x[22]*((2441596289730149*x[18])/4503599627370496 + (2694781606089567*x[19])/4503599627370496 + (664227429813961*x[20])/1125899906842624));

	e=[eq0,eq1,eq2,eq3,eq4,eq5,eq6,eq7,eq8,eq9,eq10,eq11,eq12,eq13,eq14,eq15,eq16,eq17,eq18,eq19,eq20,eq21,eq22,eq23]
	return e
def eval_model():
	data = np.loadtxt('r3R5P.txt',skiprows=0)
	data = np.transpose(data)
	res = np.empty([np.shape(data)[0],np.shape(data)[1]])
	for i in range(data.shape[0]):
		res[i,:]=np.abs(eval(data[i,:]))
	n_res=np.max(res,axis=0)
	print(n_res)
	
def dist_sol(x):
	exact=data = np.loadtxt('r3R5P.txt',skiprows=0)
	data = np.transpose(data[:,:-1])
	rdist=np.empty(x.shape[0])
	dist = np.empty(24)
	for i in range(x.shape[1]):
		for j in range(24):
			dist[j] =  np.linalg.norm(x[i,:]-data[j,:])
		rdist[i]=np.min(dist)
	return rdist	



if __name__ == '__main__':
	extsol = np.loadtxt('r3R5P.txt')
	res =eval(extsol[:,25])
	#n_range = np.min(extsol[:,:-1],axis =1)
	print(res,extsol[:,25])
	sys.exit(-1)
	eval_model()