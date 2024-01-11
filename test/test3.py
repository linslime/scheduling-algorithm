import numpy as np

a = np.arange(20)
b = a.reshape((4,5))
c = a.reshape((1,4,5))
print(c)