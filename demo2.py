import matplotlib.pyplot as plt
import numpy as np

range1 =[-1,3]
p = np.array([3])
print(p[0]*3)
print(p*3)
plt.plot(range1,p*range1+5,c='g')
plt.show()