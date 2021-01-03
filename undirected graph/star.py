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

	return s_v

def star_to_adjacency_matrix(len_m):
	vertex_pointer = {1:2, 2:3, 3:1, 4:3, 5:4, 6:1, 7:2, 8:4, 9:2, 10:3, 11:0}
	pointer_al = {1:1, 2:3, 3:6, 4:9, 5:11}
	a_m = []
	aux = []

	for i in range(len_m):
		a_m.append([0]*len_m)

	for i in range(1, 5):
		aux.append(star(i))

	for i in range(len(aux)):	
		for j in aux[i]:
			a_m[i][j-1] = 1
	
	print('Star: ')
	print(vertex_pointer)
	print(pointer_al)
	print('Adjacency Matrix: '+str(a_m))

star_to_adjacency_matrix(4)

def star_to_edge_list():
	vertex_pointer = {1:2, 2:3, 3:1, 4:3, 5:4, 6:1, 7:2, 8:4, 9:2, 10:3, 11:0}
	pointer_al = {1:1, 2:3, 3:6, 4:9, 5:11}
	aux = []
	e_l = []
	pares = {}
	aux2 = []

	for i in range(1, 5):
		aux.append(star(i))

	for i in range(len(aux)):
		for j in range(len(aux[i])):
			aux2 = []
			aux2.append(i+1)
			aux2.append(aux[i][j])
			pares[i+1] = aux[i][j]
			if aux[i][j] not in pares:
				e_l.append(aux2)

	print('Edge List: '+str(e_l))

star_to_edge_list()

def star_to_adjacency_list(len_m):
	vertex_pointer = {1:2, 2:3, 3:1, 4:3, 5:4, 6:1, 7:2, 8:4, 9:2, 10:3, 11:0}
	pointer_al = {1:1, 2:3, 3:6, 4:9, 5:11}
	aux = []
	a_l = {}

	for i in range(1, 5):
		aux.append(star(i))

	for i in range(len_m):
		a_l[i+1] = []

	for i in range(len(aux)):
		for j in aux[i]:
			a_l[i+1].append(j)

	print('Adjacency List: '+str(a_l))

star_to_adjacency_list(4)

def star_to_incidence_matrix(num_a, num_v):
	vertex_pointer = {1:2, 2:3, 3:1, 4:3, 5:4, 6:1, 7:2, 8:4, 9:2, 10:3, 11:0}
	pointer_al = {1:1, 2:3, 3:6, 4:9, 5:11}
	aux = []
	e_l = []
	pares = {}
	aux2 = []
	i_m = []
	cont = 0

	for i in range(1, 5):
		aux.append(star(i))

	for i in range(len(aux)):
		for j in range(len(aux[i])):
			aux2 = []
			aux2.append(i+1)
			aux2.append(aux[i][j])
			pares[i+1] = aux[i][j]
			if aux[i][j] not in pares:
				e_l.append(aux2)

	for i in range(num_v):
		i_m.append([0]*num_a)

	for i in range(len(e_l)):
		for j in e_l[i]:
			i_m[j-1][cont] = 1
		cont = cont + 1

	print('Incidence Matrix: '+str(i_m))

star_to_incidence_matrix(5, 4)