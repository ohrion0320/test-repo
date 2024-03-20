Oh Seung Hyeon 202303690 Computer Engineering
Touched by SeungHyeonSubb
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-2,2,0.001)
y = 4*x*x
plt.plot(x,y)
plt.title('Quadratic Curve', color='b')
plt.xlabel('x'+r'$\rightarrow$')
plt.ylabel('y'+r'$rightarrow$')
plt.legend(['Quadratic function'])
plt.grid()
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()
