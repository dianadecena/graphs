def adjacency_matrix(vertex):
	a_m = [[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]]
	a_v = []

	for i in range(len(a_m)):	
		if i == vertex-1:
			for j in range(4):
				if a_m[i][j] == 1:
					a_v.append(j+1)
			break			

	print('Adjacency Matrix: '+str(a_v))

def incidence_matrix(vertex):
	i_m = [[1, 0, 1, 0, 0], [1, 1, 0, 0, 1], [0, 1, 1, 1, 0], [0, 0, 0, 1, 1]]
	i_v = []
	pos = []

	for i in range(len(i_m)):	
		if i == vertex-1:
			for j in range(5):
				if i_m[i][j] == 1:
					pos.append(j)

	for i in range(len(i_m)):
		for j in range(5):
			if i+1 != vertex and i_m[i][j] == 1 and j in pos:
				i_v.append(i+1)

	print('Incidence Matrix: '+str(i_v))

def adjacency_list(vertex):
	a_l = [[2, 3], [1, 3, 4], [1, 2, 4], [2, 3]]
	a_l_v = []

	for i in range(len(a_l)):
		if i+1 == vertex:
			for j in range(len(a_l[i])):
				a_l_v.append(a_l[i][j])
	print('Adjacency List: '+str(a_l_v))

def edge_list(vertex):
	e_l = [[1, 2], [2, 3], [1, 3], [3, 4], [2, 4]]
	e_l_v = []

	for i in range(len(e_l)):
		if e_l[i][0] == vertex:
			e_l_v.append(e_l[i][1])
		elif e_l[i][1] == vertex:
			e_l_v.append(e_l[i][0])
	e_l_v.sort()
	print('Edge List: '+str(e_l_v))

def star(vertex):
	vertex_pointer = {1:2, 2:3, 3:1, 4:3, 5:4, 6:1, 7:2, 8:4, 9:2, 10:3, 11:0}
	pointer_al = {1:1, 2:3, 3:6, 4:9, 5:11}
	value_1 = 0
	value_2 = 0
	s_v = []

	for i in vertex_pointer.keys():
		if i == vertex:
			value_1 = pointer_al[i]
			value_2 = pointer_al[i+1]

	for j in range(value_1, value_2):
		s_v.append(vertex_pointer[j])

	print('Star: '+str(s_v))

adjacency_matrix(4)
incidence_matrix(4)
adjacency_list(4)
edge_list(4)
star(4)