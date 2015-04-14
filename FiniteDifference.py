import numpy as np

def build_matrix(xdim, zdim):

	dims = xdim * zdim
	matrix = np.zeros((dims, dims))

	
	for i in range(dims):
		for j in range(dims):
			# diagonal
			if i == j:
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

mat = build_matrix(3,3)
print mat

