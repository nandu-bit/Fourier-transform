from matplotlib import pyplot as plt
import numpy as np
w=np.arange(-np.pi,np.pi,0.01*np.pi)
t=np.arange(0,500)
F=250
fs=10000
x=0.5*np.cos(2*np.pi*F/fs*t+np.pi/2) 
l=len(x)
N=l
for k in range(0,(l)):
	s=0
	for n in range(0,len(x)):
		s=s+x[n]*np.e**(-1*1j*(2*np.pi)/N*k*n)
x=s
plt.subplot(211)
plt.plot(t,np.abs(x))
plt.subplot(212)
plt.plot(t,np.angle(x))
plt.show()

