from matplotlib import pyplot as plt
import numpy as np
w=np.arange(-np.pi,np.pi,0.01*np.pi)
x=[1,2,3,4,5]
for i in range(0,len(w)):
	s=0
	for n in range(0,len(x)):
		s=s+x[n]*np.e**(-1*1j*w*n)
x=s
plt.subplot(211)
plt.stem(w,np.abs(x))
plt.subplot(212)
plt.stem(w,np.angle(x))
plt.show()

