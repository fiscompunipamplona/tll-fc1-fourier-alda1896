from DFT2 import DFT2
from numpy import loadtxt
from pylab import plot, show, grid,yscale
data = loadtxt("co2_mm_gl.txt",float)
y= data[:,3]
t= data[:,2]

#print(type(rawdata))

#plot(t,y)


mydft=DFT2()

a,fr=mydft.dft(y,t)
Ck=list(map(abs,a))
plot(fr,Ck, 'o')
yscale('log')
grid()
show()
