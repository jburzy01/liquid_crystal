import numpy as np
import matplotlib.pyplot as plt

def build_matrix(xdim, zdim):

	dims = xdim * zdim
	matrix = np.zeros((dims, dims))

	
	for i in range(dims):
		for j in range(dims):
			# boundary conditions
			if i < xdim or i >= dims-xdim:
				if i==j:
					matrix[i,j] = 1
			# diagonal
			elif i == j:
				matrix[i,j] = -4
			elif (i+1) % xdim == 0:
				if i-j == 1:
					matrix[i,j] = 1
				elif i-j == xdim-1:
					matrix[i,j] = 1
				elif abs(j-i) == xdim:
					matrix[i,j] = 1
			# on left edge: special case
			elif i % xdim == 0:
				if j-i == 1:
					matrix[i,j] = 1
				if j-i == xdim-1:
					matrix[i,j] = 1
				elif abs(i-j) == xdim:
					matrix[i,j] = 1
			# off diagonal
			elif abs(i-j) == 1:
				matrix[i,j] = 1
			# upper/lower neighbors
			elif abs(i-j) == xdim:
				matrix[i,j] = 1	

	return matrix

def init_theta(xdim, zdim):
	dims = xdim * zdim
	theta = np.zeros(dims)

	for i in range(dims):
		if i < xdim/2:
			theta[i] = np.pi/2
		if i >= dims-xdim and i < dims-xdim/2:
			theta[i] = np.pi/2
	return theta
			
def solve(xdim, zdim):
	deltaX = 1

	mat = build_matrix(xdim, zdim)

	mat *= 1/deltaX
	b = init_theta(xdim,zdim)
	theta = np.linalg.solve(mat, b)
	return theta
	
def revert_to_matrix(xdim, zdim, theta):
	array = np.zeros((xdim,zdim))
	dims = xdim*zdim
	j = 0
	k = 0
	for i in range(dims):
		if k == xdim:
			k = 0
			j += 1

		array[j,k] = theta[i]
		k += 1
		
	return array
		
def plot(array):

    # initialize the plot
    fig = plt.figure(figsize=(3.5, 3.2))
    plt.gcf().subplots_adjust(bottom = 0.15)
    ax = fig.add_subplot(111)
    ax.set_xlabel('x')
    ax.set_ylabel('z')

    # define the plot
    plt.imshow(array)
    ax.set_aspect('equal')
    cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
    cax.get_xaxis().set_visible(False)
    cax.get_yaxis().set_visible(False)
    cax.patch.set_alpha(0)
    cax.set_frame_on(False)
    plt.colorbar(orientation='vertical')
	
    # save and show the plot
    plt.show()

xdim = 20
zdim = 20
theta = solve(xdim,zdim)
array = revert_to_matrix(xdim,zdim,theta)

plot(array)

