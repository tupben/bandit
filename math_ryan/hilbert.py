import numpy as np

image = np.random.randint(10, size=(4,4))

def convert(array):
	udlr = [[-1,0],[1,0],[0,1],[0,-1]]
	s1, s2 = array.shape
	if s1 != s2 or s1 & (s1 - 1):
		return '\nError: \n  Shape fails! \n  Desired shape: (z**2, z**2)'
	
	moves = np.array([0,2,1])
	for i in range(int(np.log2(s1)) - 1):
		moves = np.concatenate(((moves + 2) % 4, [0], moves, [2], moves, [1], (moves * 3 - 1) % 4))
	indices = map(lambda x: udlr[x], moves)
	target = np.array([s1-1,0])
	new_moves = np.array([image[s1-1][0]])
	for j in indices:
		target += j
		new_moves = np.append(new_moves, array[target[0], target[1]])
	return new_moves

print 'image array:  (dim=2)\n', image, '\n'
print 'audio array:  (dim=1)\n', convert(image), '\n'

