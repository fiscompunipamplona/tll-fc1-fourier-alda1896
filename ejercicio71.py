from numpy import arange
import numpy as np
from pylab import plot, show, grid
from DFT2 import DFT2


x=np.arange(-2,2,0.01)
cuadrado=[]
cierra=[]

for i in x:
	if (i < -1/2 or i > 1/2)  :
		cuadrado.append(0)
	else:
		cuadrado.append(1)


mydft=DFT2()

a,fr=mydft.dft(cuadrado,x)
ck=list(map(abs,a))

plot (fr,ck)
show()

