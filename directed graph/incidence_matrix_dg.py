def incidence_matrix_to_edge_list():
	i_m = [[1, 0, 1, 0, 0], [1, 1, 0, 0, 1], [0, 1, 1, 1, 0], [0, 0, 0, 1, 1]]
	e_l = []
	vertices = {}
	pares = {}

	for i in range(len(i_m)):
		vertices[i+1] = []

	for i in range(len(i_m)):
		for j in range(len(i_m[i])):
			if i_m[i][j] == 1:
				vertices[i+1].append(j)

	for i in range(len(i_m)):
		for j in vertices.keys():
			if i+1 != j:
				for k in vertices[i+1]:
					if k in vertices[j]:
						aux = []
						aux.append(i+1)
						aux.append(j)
						pares[i+1] = j
						if j not in pares:
							e_l.append(aux)
	print('Incidence Matrix: '+str(i_m))
	print('Edge List: '+str(e_l))

incidence_matrix_to_edge_list()

def incidence_matrix_to_adjacency_matrix(len_m):
	i_m = [[1, 0, 1, 0, 0], [1, 1, 0, 0, 1], [0, 1, 1, 1, 0], [0, 0, 0, 1, 1]]
	a_m = []
	vertices = {}
	pares = {}

	for i in range(len_m):
		a_m.append([0]*len_m)

	for i in range(len(i_m)):
		vertices[i+1] = []

	for i in range(len(i_m)):
		for j in range(len(i_m[i])):
			if i_m[i][j] == 1:
				vertices[i+1].append(j)

	for i in range(len(i_m)):
		for j in vertices.keys():
			if i+1 != j:
				for k in vertices[i+1]:
					if k in vertices[j]:
						if a_m[j-1][i] != 1:
							a_m[i][j-1] = 1

	print('Adjacency Matrix: '+str(a_m))

incidence_matrix_to_adjacency_matrix(4)

def adjacency_list_to_star():
	a_l = incidence_matrix_to_adjacency_list()
	vertex_pointer = {}
	pointer_al = {}
	num = 1
	cont = 0

	for i in a_l.keys():
		for j in a_l[i]:
			cont = cont+1
			if cont == 1:
				vertex_pointer[i] = num
			pointer_al[num] = j
			num = num + 1
		cont = 0
		if len(a_l[i]) == 0:
			vertex_pointer[i] = num
	pointer_al[num] = 0
	vertex_pointer[i+1] = num

	print('Star: ')
	print(str(pointer_al))
	print(str(vertex_pointer))

def incidence_matrix_to_adjacency_list():
	i_m = [[1, 0, 1, 0, 0], [1, 1, 0, 0, 1], [0, 1, 1, 1, 0], [0, 0, 0, 1, 1]]
	e_l = []
	vertices = {}
	a_l = {}

	for i in range(len(i_m)):
		vertices[i+1] = []

	for i in range(len(i_m)):
		a_l[i+1] = []

	for i in range(len(i_m)):
		for j in range(len(i_m[i])):
			if i_m[i][j] == 1:
				vertices[i+1].append(j)

	for i in range(len(i_m)):
		for j in vertices.keys():
			if i+1 != j:
				for k in vertices[i+1]:
					if k in vertices[j] and i+1 not in a_l[j]:
						a_l[i+1].append(j)
	
	print('Adjacency List: '+str(a_l))
	return a_l

def incidence_matrix_to_star():
	adjacency_list_to_star()

incidence_matrix_to_star()