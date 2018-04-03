# imports
import autograd.numpy as agnp
from autograd import grad
from autograd import jacobian
import sys
import time
def karumoto(x):
		return (1/12-1/3*(agnp.sin(x[0]-x[1])+agnp.sin(x[0])))**2+(-1/12-1/3*(agnp.sin(x[1]-x[0])+agnp.sin(x[1])))**2
def bvp(x):
	eq0 = -(1/20)**2*1.2*(1+x[1]**4)-(x[2]-2*x[1]+x[0]);
	eq1 = -(1/20)**2*1.2*(1+x[2]**4)-(x[3]-2*x[2]+x[1]);
	eq2 = -(1/20)**2*1.2*(1+x[3]**4)-(x[4]-2*x[3]+x[2]);
	eq3 = -(1/20)**2*1.2*(1+x[4]**4)-(x[5]-2*x[4]+x[3]);
	eq4 = -(1/20)**2*1.2*(1+x[5]**4)-(x[6]-2*x[5]+x[4]);
	eq5 = -(1/20)**2*1.2*(1+x[6]**4)-(x[7]-2*x[6]+x[5]);
	eq6 = -(1/20)**2*1.2*(1+x[7]**4)-(x[8]-2*x[7]+x[6]);
	eq7 = -(1/20)**2*1.2*(1+x[8]**4)-(x[9]-2*x[8]+x[7]);
	eq8 = -(1/20)**2*1.2*(1+x[9]**4)-(x[10]-2*x[9]+x[8]);
	eq9 = -(1/20)**2*1.2*(1+x[10]**4)-(x[11]-2*x[10]+x[9]);
	eq10 = -(1/20)**2*1.2*(1+x[11]**4)-(x[12]-2*x[11]+x[10]);
	eq11 = -(1/20)**2*1.2*(1+x[12]**4)-(x[13]-2*x[12]+x[11]);
	eq12 = -(1/20)**2*1.2*(1+x[13]**4)-(x[14]-2*x[13]+x[12]);
	eq13 = -(1/20)**2*1.2*(1+x[14]**4)-(x[15]-2*x[14]+x[13]);
	eq14 = -(1/20)**2*1.2*(1+x[15]**4)-(x[16]-2*x[15]+x[14]);
	eq15 = -(1/20)**2*1.2*(1+x[16]**4)-(x[17]-2*x[16]+x[15]);
	eq16 = -(1/20)**2*1.2*(1+x[17]**4)-(x[18]-2*x[17]+x[16]);
	eq17 = -(1/20)**2*1.2*(1+x[18]**4)-(x[19]-2*x[18]+x[17]);
	eq18 = -(1/20)**2*1.2*(1+x[19]**4)-(x[20]-2*x[19]+x[18]);
	eq19 = x[20];
	eq20 = -1/40*(x[2]-4*x[1]+3*x[0]);
	return eq0**2+eq1**2+eq2**2+eq3**2+eq4**2+eq5**2+eq6**2+eq7**2+eq8**2+eq9**2+eq10**2+eq11**2+eq12**2+eq13**2+eq14**2+eq15**2+eq16**2+eq17**2+eq18**2+eq19**2+eq20**2
def R3R5P(x):
	eq0= (360068103073497*x[0])/562949953421312 - (646699436464773*x[1])/4503599627370496 - (6801955882546187*x[2])/9007199254740992 + x[6] - x[7]*((4011421025109373*x[21])/9007199254740992 + (3917882588037335*x[22])/4503599627370496 + (953798181242695*x[23])/4503599627370496) + x[4]*x[8] - x[5]*x[7] + x[8]*((5643401973270251*x[21])/9007199254740992 - (2124708325674519*x[22])/4503599627370496 + (2793926927604289*x[23])/4503599627370496) - 4678477199325511/562949953421312-((2745778666230729*x[1])/9007199254740992 - (3848861997237677*x[0])/9007199254740992 - (1916647451415159*x[2])/2251799813685248 + x[9] + x[11]*((1030466759136781*x[22])/2251799813685248 - (6467692325071979*x[21])/9007199254740992 + (2361609965354677*x[23])/4503599627370496) + x[4]*x[11] - x[5]*x[10] + x[10]*((2474108714284419*x[21])/4503599627370496 + (3761666852663765*x[22])/4503599627370496 + (105157783549861*x[23])/4503599627370496) - 595490718158377/70368744177664)
	eq1= (360068103073497*x[0])/562949953421312 - (646699436464773*x[1])/4503599627370496 - (6801955882546187*x[2])/9007199254740992 + x[6] - x[7]*((4011421025109373*x[21])/9007199254740992 + (3917882588037335*x[22])/4503599627370496 + (953798181242695*x[23])/4503599627370496) + x[4]*x[8] - x[5]*x[7] + x[8]*((5643401973270251*x[21])/9007199254740992 - (2124708325674519*x[22])/4503599627370496 + (2793926927604289*x[23])/4503599627370496) - 4678477199325511/562949953421312-(x[12] - (4486461901231217*x[1])/18014398509481984 - (4259418556632645*x[2])/4503599627370496 - (939011121326619*x[0])/4503599627370496 + x[4]*x[14] - x[5]*x[13] + x[14]*((8474315113308399*x[21])/18014398509481984 + (925812279892051*x[22])/1125899906842624 - (5768853634492921*x[23])/18014398509481984) - x[13]*((576104064033825*x[22])/1125899906842624 - (1930821824706939*x[21])/2251799813685248 + (244506939647561*x[23])/4503599627370496) - 577963622217163/70368744177664)
	eq2= (360068103073497*x[0])/562949953421312 - (646699436464773*x[1])/4503599627370496 - (6801955882546187*x[2])/9007199254740992 + x[6] - x[7]*((4011421025109373*x[21])/9007199254740992 + (3917882588037335*x[22])/4503599627370496 + (953798181242695*x[23])/4503599627370496) + x[4]*x[8] - x[5]*x[7] + x[8]*((5643401973270251*x[21])/9007199254740992 - (2124708325674519*x[22])/4503599627370496 + (2793926927604289*x[23])/4503599627370496) - 4678477199325511/562949953421312-((149274648555043*x[0])/562949953421312 - (1247527883733793*x[1])/2251799813685248 - (888502933164431*x[2])/1125899906842624 + x[15] - x[16]*((7197095429335159*x[21])/18014398509481984 + (7277931406853001*x[22])/9007199254740992 - (487528960626565*x[23])/1125899906842624) + x[17]*((1976038730956279*x[21])/2251799813685248 - (1805585700077849*x[22])/9007199254740992 + (3923497627643163*x[23])/9007199254740992) + x[4]*x[17] - x[5]*x[16] - 7442297553493539/1125899906842624)
	eq3= (360068103073497*x[0])/562949953421312 - (646699436464773*x[1])/4503599627370496 - (6801955882546187*x[2])/9007199254740992 + x[6] - x[7]*((4011421025109373*x[21])/9007199254740992 + (3917882588037335*x[22])/4503599627370496 + (953798181242695*x[23])/4503599627370496) + x[4]*x[8] - x[5]*x[7] + x[8]*((5643401973270251*x[21])/9007199254740992 - (2124708325674519*x[22])/4503599627370496 + (2793926927604289*x[23])/4503599627370496) - 4678477199325511/562949953421312-((1227582497165281*x[0])/2251799813685248 + (2441596289730149*x[1])/4503599627370496 - (5759577071777535*x[2])/9007199254740992 + x[18] + x[19]*((7105171699475349*x[21])/9007199254740992 - (664227429813961*x[22])/1125899906842624 + (776127648771713*x[23])/4503599627370496) + x[4]*x[20] - x[5]*x[19] + x[20]*((5112663859404875*x[21])/18014398509481984 + (2694781606089567*x[22])/4503599627370496 + (3374441207755167*x[23])/4503599627370496) - 2110676164742821/281474976710656)
	eq4=  (5643401973270251*x[0])/9007199254740992 - (2124708325674519*x[1])/4503599627370496 + (2793926927604289*x[2])/4503599627370496 + x[7] + x[6]*((4011421025109373*x[21])/9007199254740992 + (3917882588037335*x[22])/4503599627370496 + (953798181242695*x[23])/4503599627370496) - x[3]*x[8] + x[5]*x[6] + x[8]*((646699436464773*x[22])/4503599627370496 - (360068103073497*x[21])/562949953421312 + (6801955882546187*x[23])/9007199254740992) + 8979997143696505/4503599627370496-((1030466759136781*x[1])/2251799813685248 - (6467692325071979*x[0])/9007199254740992 + (2361609965354677*x[2])/4503599627370496 + x[10] - x[3]*x[11] + x[5]*x[9] - x[9]*((2474108714284419*x[21])/4503599627370496 + (3761666852663765*x[22])/4503599627370496 + (105157783549861*x[23])/4503599627370496) + x[11]*((3848861997237677*x[21])/9007199254740992 - (2745778666230729*x[22])/9007199254740992 + (1916647451415159*x[23])/2251799813685248) - 8803061991350585/2251799813685248)
	eq5=  (5643401973270251*x[0])/9007199254740992 - (2124708325674519*x[1])/4503599627370496 + (2793926927604289*x[2])/4503599627370496 + x[7] + x[6]*((4011421025109373*x[21])/9007199254740992 + (3917882588037335*x[22])/4503599627370496 + (953798181242695*x[23])/4503599627370496) - x[3]*x[8] + x[5]*x[6] + x[8]*((646699436464773*x[22])/4503599627370496 - (360068103073497*x[21])/562949953421312 + (6801955882546187*x[23])/9007199254740992) + 8979997143696505/4503599627370496-((8474315113308399*x[0])/18014398509481984 + (925812279892051*x[1])/1125899906842624 - (5768853634492921*x[2])/18014398509481984 + x[13] + x[14]*((939011121326619*x[21])/4503599627370496 + (4486461901231217*x[22])/18014398509481984 + (4259418556632645*x[23])/4503599627370496) - x[3]*x[14] + x[5]*x[12] + x[12]*((576104064033825*x[22])/1125899906842624 - (1930821824706939*x[21])/2251799813685248 + (244506939647561*x[23])/4503599627370496) - 5315294649462349/1125899906842624)
	eq6=  (5643401973270251*x[0])/9007199254740992 - (2124708325674519*x[1])/4503599627370496 + (2793926927604289*x[2])/4503599627370496 + x[7] + x[6]*((4011421025109373*x[21])/9007199254740992 + (3917882588037335*x[22])/4503599627370496 + (953798181242695*x[23])/4503599627370496) - x[3]*x[8] + x[5]*x[6] + x[8]*((646699436464773*x[22])/4503599627370496 - (360068103073497*x[21])/562949953421312 + (6801955882546187*x[23])/9007199254740992) + 8979997143696505/4503599627370496-((1976038730956279*x[0])/2251799813685248 - (1805585700077849*x[1])/9007199254740992 + (3923497627643163*x[2])/9007199254740992 + x[16] + x[15]*((7197095429335159*x[21])/18014398509481984 + (7277931406853001*x[22])/9007199254740992 - (487528960626565*x[23])/1125899906842624) - x[3]*x[17] + x[5]*x[15] + x[17]*((1247527883733793*x[22])/2251799813685248 - (149274648555043*x[21])/562949953421312 + (888502933164431*x[23])/1125899906842624) + 8814605716093933/9007199254740992)
	eq7=  (5643401973270251*x[0])/9007199254740992 - (2124708325674519*x[1])/4503599627370496 + (2793926927604289*x[2])/4503599627370496 + x[7] + x[6]*((4011421025109373*x[21])/9007199254740992 + (3917882588037335*x[22])/4503599627370496 + (953798181242695*x[23])/4503599627370496) - x[3]*x[8] + x[5]*x[6] + x[8]*((646699436464773*x[22])/4503599627370496 - (360068103073497*x[21])/562949953421312 + (6801955882546187*x[23])/9007199254740992) + 8979997143696505/4503599627370496-((5112663859404875*x[0])/18014398509481984 + (2694781606089567*x[1])/4503599627370496 + (3374441207755167*x[2])/4503599627370496 + x[19] - x[20]*((1227582497165281*x[21])/2251799813685248 + (2441596289730149*x[22])/4503599627370496 - (5759577071777535*x[23])/9007199254740992) - x[18]*((7105171699475349*x[21])/9007199254740992 - (664227429813961*x[22])/1125899906842624 + (776127648771713*x[23])/4503599627370496) - x[3]*x[20] + x[5]*x[18] + 2659496305705689/1125899906842624)
	eq8=  (4011421025109373*x[0])/9007199254740992 + (3917882588037335*x[1])/4503599627370496 + (953798181242695*x[2])/4503599627370496 + x[8] + x[3]*x[7] - x[4]*x[6] - x[6]*((5643401973270251*x[21])/9007199254740992 - (2124708325674519*x[22])/4503599627370496 + (2793926927604289*x[23])/4503599627370496) - x[7]*((646699436464773*x[22])/4503599627370496 - (360068103073497*x[21])/562949953421312 + (6801955882546187*x[23])/9007199254740992) - 5095425119119635/1125899906842624-(x[11] - (3761666852663765*x[1])/4503599627370496 - (105157783549861*x[2])/4503599627370496 - (2474108714284419*x[0])/4503599627370496 - x[9]*((1030466759136781*x[22])/2251799813685248 - (6467692325071979*x[21])/9007199254740992 + (2361609965354677*x[23])/4503599627370496) + x[3]*x[10] - x[4]*x[9] - x[10]*((3848861997237677*x[21])/9007199254740992 - (2745778666230729*x[22])/9007199254740992 + (1916647451415159*x[23])/2251799813685248) - 4257470286518229/1125899906842624)
	eq9=  (4011421025109373*x[0])/9007199254740992 + (3917882588037335*x[1])/4503599627370496 + (953798181242695*x[2])/4503599627370496 + x[8] + x[3]*x[7] - x[4]*x[6] - x[6]*((5643401973270251*x[21])/9007199254740992 - (2124708325674519*x[22])/4503599627370496 + (2793926927604289*x[23])/4503599627370496) - x[7]*((646699436464773*x[22])/4503599627370496 - (360068103073497*x[21])/562949953421312 + (6801955882546187*x[23])/9007199254740992) - 5095425119119635/1125899906842624-((576104064033825*x[1])/1125899906842624 - (1930821824706939*x[0])/2251799813685248 + (244506939647561*x[2])/4503599627370496 + x[14] - x[13]*((939011121326619*x[21])/4503599627370496 + (4486461901231217*x[22])/18014398509481984 + (4259418556632645*x[23])/4503599627370496) + x[3]*x[13] - x[4]*x[12] - x[12]*((8474315113308399*x[21])/18014398509481984 + (925812279892051*x[22])/1125899906842624 - (5768853634492921*x[23])/18014398509481984) - 8583953429733309/4503599627370496)
	eq10=  (4011421025109373*x[0])/9007199254740992 + (3917882588037335*x[1])/4503599627370496 + (953798181242695*x[2])/4503599627370496 + x[8] + x[3]*x[7] - x[4]*x[6] - x[6]*((5643401973270251*x[21])/9007199254740992 - (2124708325674519*x[22])/4503599627370496 + (2793926927604289*x[23])/4503599627370496) - x[7]*((646699436464773*x[22])/4503599627370496 - (360068103073497*x[21])/562949953421312 + (6801955882546187*x[23])/9007199254740992) - 5095425119119635/1125899906842624-((7197095429335159*x[0])/18014398509481984 + (7277931406853001*x[1])/9007199254740992 - (487528960626565*x[2])/1125899906842624 + x[17] - x[15]*((1976038730956279*x[21])/2251799813685248 - (1805585700077849*x[22])/9007199254740992 + (3923497627643163*x[23])/9007199254740992) + x[3]*x[16] - x[4]*x[15] - x[16]*((1247527883733793*x[22])/2251799813685248 - (149274648555043*x[21])/562949953421312 + (888502933164431*x[23])/1125899906842624) - 8931778261037253/1125899906842624)
	eq11=  (4011421025109373*x[0])/9007199254740992 + (3917882588037335*x[1])/4503599627370496 + (953798181242695*x[2])/4503599627370496 + x[8] + x[3]*x[7] - x[4]*x[6] - x[6]*((5643401973270251*x[21])/9007199254740992 - (2124708325674519*x[22])/4503599627370496 + (2793926927604289*x[23])/4503599627370496) - x[7]*((646699436464773*x[22])/4503599627370496 - (360068103073497*x[21])/562949953421312 + (6801955882546187*x[23])/9007199254740992) - 5095425119119635/1125899906842624-((664227429813961*x[1])/1125899906842624 - (7105171699475349*x[0])/9007199254740992 - (776127648771713*x[2])/4503599627370496 + x[20] + x[19]*((1227582497165281*x[21])/2251799813685248 + (2441596289730149*x[22])/4503599627370496 - (5759577071777535*x[23])/9007199254740992) + x[3]*x[19] - x[4]*x[18] - x[18]*((5112663859404875*x[21])/18014398509481984 + (2694781606089567*x[22])/4503599627370496 + (3374441207755167*x[23])/4503599627370496) + 2613587444270205/4503599627370496)
	eq12=  x[3]*x[6]+x[4]*x[7]+x[5]*x[8]-(x[3]*x[9]+x[4]*x[10]+x[5]*x[11])
	eq13=  x[3]*x[6]+x[4]*x[7]+x[5]*x[8]-(x[3]*x[12]+x[4]*x[13]+x[5]*x[14])
	eq14=  x[3]*x[6]+x[4]*x[7]+x[5]*x[8]-(x[3]*x[15]+x[4]*x[16]+x[5]*x[17])
	eq15=  x[3]*x[6]+x[4]*x[7]+x[5]*x[8]-(x[3]*x[18]+x[4]*x[19]+x[5]*x[20])
	eq16=  x[6]**2+x[7]**2+x[8]**2-(x[9]**2+x[10]**2+x[11]**2)
	eq17=  x[6]**2+x[7]**2+x[8]**2-(x[12]**2+x[13]**2+x[14]**2)
	eq18=  x[6]**2+x[7]**2+x[8]**2-(x[15]**2+x[16]**2+x[17]**2)
	eq19=  x[6]**2+x[7]**2+x[8]**2-(x[18]**2+x[19]**2+x[20]**2)
	eq20=  x[22]*((646699436464773*x[6])/4503599627370496 + (2124708325674519*x[7])/4503599627370496 - (3917882588037335*x[8])/4503599627370496) - x[21]*((360068103073497*x[6])/562949953421312 + (5643401973270251*x[7])/9007199254740992 + (4011421025109373*x[8])/9007199254740992) - x[23]*((2793926927604289*x[7])/4503599627370496 - (6801955882546187*x[6])/9007199254740992 + (953798181242695*x[8])/4503599627370496)-(x[21]*((3848861997237677*x[9])/9007199254740992 + (6467692325071979*x[10])/9007199254740992 + (2474108714284419*x[11])/4503599627370496) + x[23]*((1916647451415159*x[9])/2251799813685248 - (2361609965354677*x[10])/4503599627370496 + (105157783549861*x[11])/4503599627370496) - x[22]*((2745778666230729*x[9])/9007199254740992 + (1030466759136781*x[10])/2251799813685248 - (3761666852663765*x[11])/4503599627370496))
	eq21=  x[22]*((646699436464773*x[6])/4503599627370496 + (2124708325674519*x[7])/4503599627370496 - (3917882588037335*x[8])/4503599627370496) - x[21]*((360068103073497*x[6])/562949953421312 + (5643401973270251*x[7])/9007199254740992 + (4011421025109373*x[8])/9007199254740992) - x[23]*((2793926927604289*x[7])/4503599627370496 - (6801955882546187*x[6])/9007199254740992 + (953798181242695*x[8])/4503599627370496)-(x[21]*((939011121326619*x[12])/4503599627370496 - (8474315113308399*x[13])/18014398509481984 + (1930821824706939*x[14])/2251799813685248) + x[23]*((4259418556632645*x[12])/4503599627370496 + (5768853634492921*x[13])/18014398509481984 - (244506939647561*x[14])/4503599627370496) - x[22]*((925812279892051*x[13])/1125899906842624 - (4486461901231217*x[12])/18014398509481984 + (576104064033825*x[14])/1125899906842624))
	eq22=  x[22]*((646699436464773*x[6])/4503599627370496 + (2124708325674519*x[7])/4503599627370496 - (3917882588037335*x[8])/4503599627370496) - x[21]*((360068103073497*x[6])/562949953421312 + (5643401973270251*x[7])/9007199254740992 + (4011421025109373*x[8])/9007199254740992) - x[23]*((2793926927604289*x[7])/4503599627370496 - (6801955882546187*x[6])/9007199254740992 + (953798181242695*x[8])/4503599627370496)-(x[22]*((1247527883733793*x[15])/2251799813685248 + (1805585700077849*x[16])/9007199254740992 - (7277931406853001*x[17])/9007199254740992) - x[21]*((149274648555043*x[15])/562949953421312 + (1976038730956279*x[16])/2251799813685248 + (7197095429335159*x[17])/18014398509481984) + x[23]*((888502933164431*x[15])/1125899906842624 - (3923497627643163*x[16])/9007199254740992 + (487528960626565*x[17])/1125899906842624))
	eq23=  x[22]*((646699436464773*x[6])/4503599627370496 + (2124708325674519*x[7])/4503599627370496 - (3917882588037335*x[8])/4503599627370496) - x[21]*((360068103073497*x[6])/562949953421312 + (5643401973270251*x[7])/9007199254740992 + (4011421025109373*x[8])/9007199254740992) - x[23]*((2793926927604289*x[7])/4503599627370496 - (6801955882546187*x[6])/9007199254740992 + (953798181242695*x[8])/4503599627370496)-(x[23]*((5759577071777535*x[18])/9007199254740992 - (3374441207755167*x[19])/4503599627370496 + (776127648771713*x[20])/4503599627370496) - x[21]*((1227582497165281*x[18])/2251799813685248 + (5112663859404875*x[19])/18014398509481984 - (7105171699475349*x[20])/9007199254740992) - x[22]*((2441596289730149*x[18])/4503599627370496 + (2694781606089567*x[19])/4503599627370496 + (664227429813961*x[20])/1125899906842624))

	#return eq0**2+eq1**2+eq2**2+eq3**2+eq4**2+eq5**2+eq6**2+eq7**2+eq8**2+eq9**2+eq10**2+eq11**2+eq12**2+eq13**2+eq14**2+eq15**2+eq16**2+eq17**2+eq18**2+eq19**2+eq20**2+eq21**2+eq22**2+eq23**2
	return agnp.array([eq0,eq1,eq2,eq3,eq4,eq5,eq6,eq7,eq8,eq9,eq10,eq11,eq12,eq13,eq14,eq15,eq16,eq17,eq18,eq19,eq20,eq21,eq22,eq23])

def adam(alp,b1,b2,model,init):
	eps  =  1.0e-8
	m=0;
	u=0;
	t=0;
	tol = 10;
	gradi=grad(model)
	x = agnp.float64(init)
	accf = model(x)

<<<<<<< HEAD
	while (tol > 1.0e-3) | (accf > 8e-8):
=======
	while (tol > 1.0e-3) | (accf > 1e-5):
>>>>>>> 3cab1c1147f7a3ae1718174a07ca93f7871363f7
		t += 1;
		g = gradi(x)
		m = b1*m+(1-b1)*g
		u = b2*u+(1-b2)*g**2
		a_t = alp*agnp.sqrt(1-b2**t)/(1-b1**t)
		xn = x -  a_t*m/(agnp.sqrt(u)+accf*eps)
		tol = agnp.linalg.norm(xn-x)
		x = xn
		accf = model(x)
	return (x, accf)

if __name__ == '__main__':
	# Record the cputime for optimizing one point
	t1=time.process_time()
<<<<<<< HEAD
	model =karumoto
	#data = agnp.loadtxt('paramTraces_3R5P.txt',skiprows=1)
	#init =  data[agnp.random.choice(1),2:]
	init=[0.0,0.0]

	t,accf=adam(0.001,0.9,0.999,model,init)
	#One true solution
	# tt=agnp.array([2.46372917,  2.27559646  ,2.0060732  , 1.70833523 , 1.46246037 , 1.32661059,
 #  1.31520979 , 1.4052676  , 1.52220994  ,1.59441577  ,1.56800426 , 1.48610163,
 #  1.45399811  ,1.5690482   ,1.8111774   ,2.1323249  , 2.2147605   ,1.7708001,
 #  0.83824345  ,0.12272874 ,-0.30528073])
	# tt=	agnp.array([-2.65466227e-01,  1.12015874e+00 ,-5.89020322e-01, -8.53806091e+04,
 # -1.13841792e+05 ,-1.42301658e+05, -9.55796021e-03,  5.94840094e-02,
 #  1.28835432e-01 ,-8.35001001e-02,  6.28708420e-02, -9.85938780e-02,
 # -1.14471103e-01 , 9.86363674e-02,  1.20769572e-02, -7.26872919e-02,
 #  9.40279011e-02 , 8.39337514e-02,  4.14991238e-02,  1.43177362e-01,
 #  9.04064038e-04 ,-5.97670165e+05, -6.26130740e+05, -6.54591364e+05])

 	# One adam convergent solution
	# tt=agnp.array([ 2.77452690e+01, -2.31730463e+01, -2.55689758e+00 , 2.85845903e+00,
 # -1.71685402e+00,  2.99819214e-01,  2.03663785e+01, -1.02446737e+01,
 #  1.36174705e+01 , 2.35463908e+01, -8.82810893e+00, -8.53264649e+00,
 #  2.62512201e+01, -2.08685610e+00,  3.42315608e+00,  2.06091653e+01,
 # -9.89000273e+00 , 1.35133412e+01,  2.60128621e+01, -2.51400853e+00,
 #  4.70808068e+00 ,-2.13399244e-02, -9.26407023e-03,  8.32235696e-02]) 
	gradi=jacobian(model)
	print(agnp.linalg.norm(gradi(t))/(agnp.linalg.norm(model(t))/agnp.linalg.norm(t)))
	cputime = time.process_time()-t1
	print(t,accf,model(t),cputime)
=======

	# Set the model type and initial poitn
	model = 'bvp'
	data = agnp.loadtxt('paramTraces_'+str(model)+'.txt',skiprows=1)
	init =  data[agnp.random.choice(1),2:]
	# Run the adam method on the model
	t,accf=adam(0.001,0.9,0.999,eval(model),init)
	cputime = time.process_time()-t1
	print(t,accf,bvp(t),cputime)
	# compute and show the gradient of the optimal point if needed
	gradi=grad(bvp)
	print(gradi(t))
>>>>>>> 3cab1c1147f7a3ae1718174a07ca93f7871363f7
