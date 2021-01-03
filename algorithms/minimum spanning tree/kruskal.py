def kruskal():
	a_m = [[0, 3, 2, 0, 0], [3, 0, 1, 4, 3], [2, 1, 0, 1, 0], [0, 4, 1, 0, 8], [0, 3, 0, 8, 0]]
	#a_m = [[0, 5, 0, 4, 0], [5, 0, 7, 1, 2], [0, 7, 0, 6, 6], [4, 1, 6, 0, 3], [0, 2, 6, 3, 0]]
	arcos = []
	aux = []
	pares = {}
	f = 0
	ciclos = []

	for i in range(7):
		arcos.append([0]*2)

	for i in range(len(arcos)):
		arcos[i][0] = []

	for i in range(len(a_m)):	
		for j in range(5):
			if a_m[i][j] >= 1 and j <= 1 and len(aux) <= 2:
				aux = []
				aux.append(i+1)
				aux.append(j+1)	
				pares[i+1] = j+1
				if j+1 not in pares:
					arcos[f][0].append(i+1)
					arcos[f][0].append(j+1)
					arcos[f][1] = a_m[i][j]
					f = f + 1
			elif a_m[i][j] >= 1 and j > 1 and len(aux) <= 2:
				aux = []
				aux.append(i+1)
				aux.append(j+1)	
				pares[i+1] = j+1
				if j+1 not in pares:
					arcos[f][0].append(i+1)
					arcos[f][0].append(j+1)
					arcos[f][1] = a_m[i][j]
					f = f + 1

	def column(arcos):
		return arcos[1]
	arcos.sort(key=column)

	print('Adjacency Matrix: '+str(a_m))
	print('Arcos: '+str(arcos))

	nodos = {}

	for i in range(5):
		nodos[i+1] = []

	kruskal_m = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

	for i in range(len(a_m)):
		for j in range(5):
			if a_m[i][j] >= 1 and i+1 not in nodos[j+1]:
				nodos[i+1].append(j+1)
				for k in nodos.keys():
					if i+1 in nodos[k] and j+1 in nodos[k]:
						aux = []
						aux.append(k) 
						aux.append(i+1) 
						aux.append(j+1) 
						ciclos.append(aux)				

	n_arr = []
	n_arr1 = []
	n_arr2 = []
	arr = ciclos[0]+ciclos[1]
	arr1 = ciclos[1]+ciclos[2]
	arr2 = ciclos[0]+ciclos[2]
	for i in arr:
		if i not in n_arr:
			n_arr.append(i)

	for i in arr1:
		if i not in n_arr1:
			n_arr1.append(i)

	for i in arr2:
		if i not in n_arr2:
			n_arr2.append(i)

	ciclos.append(n_arr)
	ciclos.append(n_arr1)
	ciclos.append(n_arr2)
	print('Ciclos: '+str(ciclos))

	for i in range(len(arcos)):
		for j in ciclos:
			if arcos[i][0][0] in j and arcos[i][0][1] in j:
				if arcos[i][0][0] == j[0] and arcos[i][0][1] == j[2]:
					if kruskal_m[arcos[i][0][0]-1][j[1]-1] == 0 and kruskal_m[j[1]-1][j[2]-1] == 0: 
						n1 = arcos[i][0][0]-1
						n2 = arcos[i][0][1]-1
						kruskal_m[n1][n2] = arcos[i][1]
					elif kruskal_m[arcos[i][0][0]-1][j[1]-1] == 0:
						n1 = arcos[i][0][0]-1
						n2 = arcos[i][0][1]-1
						kruskal_m[n1][n2] = arcos[i][1]
				elif arcos[i][0][0] == j[0] and arcos[i][0][1] == j[1]:
					if kruskal_m[arcos[i][0][0]-1][j[2]-1] == 0 and kruskal_m[j[0]-1][j[2]-1] == 0:
						n1 = arcos[i][0][0]-1
						n2 = arcos[i][0][1]-1
						kruskal_m[n1][n2] = arcos[i][1]
				elif arcos[i][0][0] == j[1] and arcos[i][0][1] == j[2]:
					if kruskal_m[j[0]-1][j[2]-1] == 0 and kruskal_m[j[0]-1][j[1]-1] == 0 and kruskal_m[j[1]-1][j[2]-1] >= 1:
						n1 = arcos[i][0][0]-1
						n2 = arcos[i][0][1]-1
						kruskal_m[n1][n2] = arcos[i][1]
					elif kruskal_m[j[0]-1][j[2]-1] == 0 and kruskal_m[j[1]-1][j[2]-1] == 0 and kruskal_m[j[0]-1][j[1]-1] >= 1:
						n1 = arcos[i][0][0]-1
						n2 = arcos[i][0][1]-1
						kruskal_m[n1][n2] = arcos[i][1]

	print('Kruskal: '+str(kruskal_m))

	peso = 0
	for i in range(len(kruskal_m)):
		for j in kruskal_m[i]:
			if j != 0:
				peso = peso + j
	print('El peso del árbol es: '+str(peso))

kruskal()
