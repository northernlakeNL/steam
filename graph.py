import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

data1 = [1, 4, 33, 55, 69, 100]

y = data1
x = np.arange(len(data1))

plt.plot(x,y)
plt.show()