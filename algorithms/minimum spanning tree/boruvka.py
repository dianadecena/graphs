import numpy as np

a_m = np.array([[0, 4, 2, 999, 999], [4, 0, 7, 6, 1], [2, 7, 0, 9, 999], [999, 6, 9, 0, 8], [999, 1, 999, 8, 0]])
arbol = [[0, 999, 999, 999, 999], [999, 0, 999, 999, 999], [999, 999, 0, 999, 999], [999, 999, 999, 0, 999], [999, 999, 999, 999, 0]]
# origen - destino - costo - tobo 
tobos = []
aux = []
min_dist = 0
tobo = 1

for i in range(len(a_m)):
	arr = a_m[i,:]
	min_dist = arr[arr>0].min()
	for j in range(len(a_m[i])):
		if a_m[i][j] == min_dist:
			agregar = True
			for k in range(len(tobos)):
				if j+1 == tobos[k][0]:
					tobo = tobos[k][3]
				if i+1 == tobos[k][1]:
					agregar = False
			if agregar:
				if i+1 > j+1:
					aux.append(j+1)
					aux.append(i+1)
				else:
					aux.append(i+1)
					aux.append(j+1)
				aux.append(min_dist)
				aux.append(tobo)
				tobos.append(aux)
				aux = []
	tobo = tobo + 1
print('primera vuelta: '+str(tobos))

num_tobos = []
for i in range(len(tobos)):
	if tobos[i][3] not in num_tobos:
		num_tobos.append(tobos[i][3])
nodos_tobos = {}
for i in range(len(tobos)):
	for t in num_tobos:
		nodos_tobos[t] = []

for i in range(len(tobos)):
	for t in num_tobos:
		if tobos[i][3] == t:
			if tobos[i][0] not in nodos_tobos[t]:
				nodos_tobos[t].append(tobos[i][0])
			if tobos[i][1] not in nodos_tobos[t]:
				nodos_tobos[t].append(tobos[i][1])
minimos = []
if len(num_tobos) > 1:
	for i in range(len(a_m)):
			for k in range(len(tobos)):
				if i+1 == tobos[k][0] or i+1 == tobos[k][1]:
					for key in nodos_tobos.keys():
						if key != tobos[k][3]:
							for j in range(len(a_m[i])):
								if j+1 in nodos_tobos[key]:
									if a_m[i][j] != 0 and a_m[i][j] != 999:
										aux = []
										aux.append(i+1)
										aux.append(j+1)
										aux.append(a_m[i][j])
										aux.append(key)
										minimos.append(aux)
min_ab = []
for i in range(len(minimos)):
	min_ab.append(minimos[i][2])
aux = []
for i in range(len(minimos)):
	if minimos[i][2] == min(min_ab) and len(aux) == 0:
		aux.append(minimos[i][0])
		aux.append(minimos[i][1])
		aux.append(minimos[i][2])
		aux.append(minimos[i][3])	
		tobos.append(aux)

for i in range(len(tobos)):
	arbol[tobos[i][0]-1][tobos[i][1]-1] = tobos[i][2]
	arbol[tobos[i][1]-1][tobos[i][0]-1] = tobos[i][2]
	tobos[i][3] = 1
print('segunda vuelta: '+str(tobos))
print('matriz de adyacencia arbol cobertor:')
print(arbol)

peso = 0
repetidos = []
for i in range(len(arbol)):
	for j in range(len(arbol[i])):
		if arbol[i][j] != 0 and arbol[i][j] != 999 and j+1 not in repetidos:
			repetidos.append(i+1)
			peso = peso + arbol[i][j]
print('el peso del árbol es: '+str(peso))