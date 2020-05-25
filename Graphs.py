import numpy as np
from matplotlib import pyplot as plt
x = np.arange(-5*(np.pi), 5*(np.pi), 0.05)
y1 = -x
y2 = x
y3 = np.sin(x)
y4 = x*(np.sin(x))

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.legend(['x','-x','sin(x)','x*sin(x)'])
plt.show()