import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

def henon_attractor(x, y, a=1.4, b=0.3):
	'''Computes the next step in the Henon 
	map for arguments x, y with kwargs a and
	b as constants.
	'''
	x_next = 1 - a * x ** 2 + y
	y_next = b * x
	return x_next, y_next
	
# number of iterations and array initialization
steps = 100000
X = np.zeros(steps + 1)
Y = np.zeros(steps + 1)

# starting point
X[0], Y[0] = 0, 0

# add points to array
for i in range(steps):
	x_next, y_next = henon_attractor(X[i], Y[i])
	X[i+1] = x_next
	Y[i+1] = y_next
	
# plot figure
plt.plot(X, Y, '^', color='white', alpha = 0.8, markersize=0.3)
plt.axis('off')
plt.show()
plt.close()