import numpy as np

incluidos = np.array([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]])
#a_m = [[0, 3, 2, 999, 999], [3, 0, 1, 4, 3], [2, 1, 0, 1, 999], [999, 4, 1, 0, 8], [999, 3, 999, 8, 0]]
a_m = [[0, 3, 2, 999, 999, 999], [3, 0, 5, 4, 5, 999], [2, 5, 0, 1, 999, 2], [999, 4, 1, 0, 8, 1], [999, 5, 999, 8, 0, 2], [999, 999, 2, 1, 2, 0]]
nodos = []
arbol = [[0, 999, 999, 999, 999, 999], [999, 0, 999, 999, 999, 999], [999, 999, 0, 999, 999, 999], [999, 999, 999, 0, 999, 999], [999, 999, 999, 999, 0, 999], [999, 999, 999, 999, 999, 0]]
first = True

def armar_cola(nodos):
	aux = []
	cola = []

	for i in range(len(a_m)):
		for j in range(len(a_m[i])):
			if a_m[i][j] >= 1 and a_m[i][j] != 999:
				for k in range(len(nodos)):
					if i+1 in nodos[k]:
						aux.append(i+1)
						aux.append(j+1)
						aux.append(a_m[i][j])
						cola.append(aux)
						aux = []
	return cola

def set_zeros(origen, destino):
	for i in range(len(a_m)):
		for j in range(len(a_m[i])):
			if i == destino-1 and j == origen-1:
				a_m[i][j] = 0
			if j == destino-1:
				a_m[i][j] = 0
	print(a_m)			

while 0 in incluidos[:,1]:
	if first:
		incluidos[0,1] = 1
		set_zeros(1,1)
		first = False
	nodos.append((incluidos[incluidos[:,1]==1][:,0]).tolist())
	cola = armar_cola(nodos)
	cola = np.array(cola)
	print('cola:')
	print(cola)
	peso_min = min(cola[:,2])
	for i in range(len(cola)):
		if cola[i,2] == peso_min:
			origen = cola[i,0]
			destino = cola[i,1]
	arbol[origen-1][destino-1] = peso_min
	arbol[destino-1][origen-1] = peso_min
	for k in range(len(incluidos)):
		if incluidos[k,0] == destino:
			incluidos[k,1] = 1
	set_zeros(origen, destino)
	print('incluidos:')
	print(incluidos)
	nodos = []

print(arbol)

peso = 0
repetidos = []
for i in range(len(arbol)):
	for j in range(len(arbol[i])):
		if arbol[i][j] != 0 and arbol[i][j] != 999 and j+1 not in repetidos:
			repetidos.append(i+1)
			peso = peso + arbol[i][j]
print('el peso del árbol es: '+str(peso))