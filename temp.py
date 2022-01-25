import matplotlib.pyplot as plt
xdata = [1, 4, 8]
ydata = [10, 20, 30]
plt.plot(xdata, ydata)
plt.ylim(ymin=0)  # this line
plt.show()