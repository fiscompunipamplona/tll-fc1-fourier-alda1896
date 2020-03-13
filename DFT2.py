from numpy import zeros
from cmath import exp,pi

class DFT2:
	def __init__(self):
		self.c=[]
		self.fr=[]

	def dft (self,y,x):
		N=len(y)
		self.c= zeros(N//2+1,complex)
		for k in range (N//2+1):
			for i in range (N):
				self.c[k] += y[i]*exp(-2j*pi*k*i/N)

			self.fr.append(k/N)
		return(self.c,self.fr)
