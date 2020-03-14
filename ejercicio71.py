from numpy import arange
import numpy as np
import math as mt
from math import sin,pi
from pylab import plot, show, grid
from DFT2 import DFT2


x=np.arange(-50,50,0.1)
cuadrado=[]
sierra=[]
msin=[]
N=len(x)

for i in x:

	
	if (i < -1/2 or i > 1/2)  :
		cuadrado.append(0)
	else:
		cuadrado.append(1)

	
	dec,ent=mt.modf(i)
	if (i > 0):
		sierra.append(i-ent)
	else:
		sierra.append(0)


	msin.append(sin(pi*i/N)*sin(20*pi*i/N))


mydft=DFT2()

a,fr=mydft.dft(sierra,x)
ck=list(map(abs,a))

#plot(x,sierra)
#plot(x,cuadrado)
#plot(x,msin)

plot (fr,ck)
show()

