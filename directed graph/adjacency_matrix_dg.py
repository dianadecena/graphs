def adjacency_matrix_to_edge_list():
	a_m = [[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
	e_l = []
	aux = []

	for i in range(len(a_m)):	
		for j in range(4):
			if a_m[i][j] == 1:
				aux = []
				aux.append(i+1)
				aux.append(j+1)	
				e_l.append(aux)

	print('Adjacency Matrix: '+str(a_m))
	print('Edge List: '+str(e_l))

def adjacency_matrix_to_adjacency_list():
	a_m = [[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
	a_l = {}

	for i in range(len(a_m)):
		a_l[i+1] = []

	for i in range(len(a_m)):	
		for j in range(4):
			if a_m[i][j] == 1:
				a_l[i+1].append(j+1)

	print('Adjacency List: '+str(a_l))

def adjacency_matrix_to_star():
	a_m = [[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
	vertex_pointer = {}
	pointer_al = {}
	num = 0
	cont = 0

	for i in range(len(a_m)):	
		for j in range(4):
			if a_m[i][j] == 1:
				cont = cont+1
				num = num+1
				pointer_al[num] = j+1
				if cont == 1:
					vertex_pointer[i+1] = num
		cont = 0
		if i == len(a_m)-1:
			num = num + 1 
			pointer_al[num] = 0
			vertex_pointer[i+1] = num
			vertex_pointer[i+2] = num

	print('Star: ')
	print(vertex_pointer)
	print(pointer_al)

adjacency_matrix_to_edge_list()
adjacency_matrix_to_adjacency_list()
adjacency_matrix_to_star()

def adjacency_matrix_to_incidence_matrix(num_a, num_v):
	a_m = [[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
	e_l = []
	aux = []
	pares = {}
	i_m = []
	cont = 0

	for i in range(len(a_m)):	
		for j in range(4):
			if a_m[i][j] == 1 and j <= 1 and len(aux) <= 2:
				aux = []
				aux.append(i+1)
				aux.append(j+1)	
				pares[i+1] = j+1
				if j+1 not in pares:
					e_l.append(aux)
			elif a_m[i][j] == 1 and j > 1 and len(aux) <= 2:
				aux = []
				aux.append(i+1)
				aux.append(j+1)	
				pares[i+1] = j+1
				if j+1 not in pares:
					e_l.append(aux)

	for i in range(num_v):
		i_m.append([0]*num_a)

	for i in range(len(e_l)):
		for j in e_l[i]:
			i_m[j-1][cont] = 1
		cont = cont + 1

	print('Incidence Matrix: '+str(i_m))

adjacency_matrix_to_incidence_matrix(5, 4)