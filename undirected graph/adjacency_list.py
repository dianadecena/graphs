def adjacency_list_to_adjacency_matrix(len_m):
	a_m = []
	a_l = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}
	#a_l = {1: [2, 3, 4], 2: [1, 4, 5], 3: [1, 4, 6], 4: [1, 2, 3, 5, 6, 7], 5: [2, 4, 7], 6: [3, 4, 7], 7: [4, 5, 6]}

	for i in range(len_m):
		a_m.append([0]*len_m)

	for i in range(len(a_m)+1):
		if i in a_l.keys():	
			for j in a_l[i]:
				a_m[i-1][j-1] = 1

	print('Adjacency List: '+str(a_l))
	print('Adjacency Matrix: '+str(a_m))

adjacency_list_to_adjacency_matrix(4)

def adjacency_list_to_edge_list():
	a_l = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}
	e_l = []
	aux = []
	pares = {}

	for i in a_l.keys():
		for j in range(len(a_l[i])):
			aux = []
			aux.append(i)
			aux.append(a_l[i][j])
			pares[i] = a_l[i][j]
			if a_l[i][j] not in pares:
				e_l.append(aux)

	print('Edge List: '+str(e_l))

adjacency_list_to_edge_list()

def adjacency_list_to_star():
	a_l = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}
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
	pointer_al[num] = 0
	vertex_pointer[i+1] = num

	print('Star: ')
	print(str(pointer_al))
	print(str(vertex_pointer))

adjacency_list_to_star()

def adjacency_list_to_incidence_matrix(num_a, num_v):
	a_l = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}
	e_l = []
	i_m = []
	pares = {}
	cont = 0

	for i in a_l.keys():
		for j in range(len(a_l[i])):
			aux = []
			aux.append(i)
			aux.append(a_l[i][j])
			pares[i] = a_l[i][j]
			if a_l[i][j] not in pares:
				e_l.append(aux)

	for i in range(num_v):
		i_m.append([0]*num_a)

	for i in range(len(e_l)):
		for j in e_l[i]:
			i_m[j-1][cont] = 1
		cont = cont + 1

	print('Incidence Matrix: '+str(i_m))

adjacency_list_to_incidence_matrix(5, 4)