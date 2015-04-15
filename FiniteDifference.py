import numpy as np

def build_matrix(xdim, zdim):

	dims = xdim * zdim
	matrix = np.zeros((dims, dims))

	
	for i in range(dims):
		for j in range(dims):
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
	print theta
	return theta
			
def solve():
	deltaX = 1
	xdim = 10
	zdim = 10
	mat = build_matrix(xdim, zdim)

	mat *= 1/deltaX
	b = init_theta(xdim,zdim)
	theta = np.linalg.solve(mat, b)
	return theta
	

theta = solve()
print theta
