import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y = np.sin(x)

plt.figure(figsize=(3, 3))
plt.plot(x, y)
plt.show()