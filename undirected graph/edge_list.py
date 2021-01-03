def edge_list_to_adjacency_matrix(len_m):
	e_l = [[1, 2], [2, 3], [1, 3], [3, 4], [2, 4]]
	a_m = []

	for i in range(len_m):
		a_m.append([0]*len_m)

	for i in range(len(e_l)):
		a_m[e_l[i][0]-1][e_l[i][1]-1] = 1
		a_m[e_l[i][1]-1][e_l[i][0]-1] = 1
	
	print('Edge List: '+str(e_l)) 
	print('Adjacency Matrix: '+str(a_m))

edge_list_to_adjacency_matrix(4)

def edge_list_to_adjacency_list():
	e_l = [[1, 2], [2, 3], [1, 3], [3, 4], [2, 4]]
	a_l = {}

	for i in range(len(e_l)-1):
		a_l[i+1] = []

	for i in range(len(e_l)):
		a_l[e_l[i][0]].append(e_l[i][1])
		a_l[e_l[i][1]].append(e_l[i][0])

	for i in range(len(e_l)-1):
		a_l[i+1].sort()

	print('Adjacency List: '+str(a_l))

edge_list_to_adjacency_list()

def edge_list_to_star():
	e_l = [[1, 2], [2, 3], [1, 3], [3, 4], [2, 4]]
	a_l = {}
	vertex_pointer = {}
	pointer_al = {}
	num = 1
	cont = 0

	for i in range(len(e_l)-1):
		a_l[i+1] = []

	for i in range(len(e_l)):
		a_l[e_l[i][0]].append(e_l[i][1])

	for i in range(len(e_l)):
		if e_l[i][0] in a_l.keys():
			a_l[e_l[i][1]].append(e_l[i][0])

	for i in range(len(e_l)-1):
		a_l[i+1].sort()

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
	print(vertex_pointer)
	print(pointer_al)

edge_list_to_star()

def edge_list_to_incidence_matrix(num_a, num_v):
	e_l = [[1, 2], [2, 3], [1, 3], [3, 4], [2, 4]]
	cont = 0
	i_m = []

	for i in range(num_v):
		i_m.append([0]*num_a)

	for i in range(len(e_l)):
		for j in e_l[i]:
			i_m[j-1][cont] = 1
		cont = cont + 1

	print('Incidence Matrix: '+str(i_m))

edge_list_to_incidence_matrix(5, 4)