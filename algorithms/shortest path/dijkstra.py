import numpy as np 
import pandas as pd 

data_frame = pd.read_excel("matriz_ady.xlsx")
data_frame2 = pd.read_excel("tabla_andreina.xlsx")
a_m = []
tabla = []

for i in range(36):
  a_m.append(data_frame[i+1].tolist())
  tabla.append(data_frame2[i+1].tolist())

tabla = np.array(tabla)

#a_m = [[0, 3, 2, 0, 0, 0], [3, 0, 5, 4, 5, 0], [2, 5, 0, 1, 0, 2], [0, 4, 1, 0, 8, 1], [0, 5, 0, 8, 0, 2], [0, 0, 2, 1, 2, 0]]
#nodo - visitado - dist min desde 1 - predecesor
#tabla = np.array([[1, 0, 0, 0], [2, 0, 999, 0], [3, 0, 999, 0], [4, 0, 999, 0], [5, 0, 999, 0], [6, 0, 999, 0]]) #0 false, 1 true
pila = [1] 

def buscarAdy(nodo):
	nodos_ady = []
	for i in range(len(a_m)):
		if a_m[i][nodo-1] != 0:
			nodos_ady.append(i+1)
	return nodos_ady

while pila:
	v = pila.pop() #sacar primer elemento de la pila 
	print('visito: '+str(v))

	for nodo_ady in range(len(a_m[v-1])):
		if a_m[v-1][nodo_ady] != 0 and tabla[v-1,1] == 0:
			if tabla[nodo_ady,0] in buscarAdy(20):
				if v!=20 and tabla[v-1,2] + a_m[v-1][nodo_ady] < tabla[nodo_ady,2]:
					tabla[nodo_ady,2] = tabla[v-1,2] + a_m[v-1][nodo_ady]
					tabla[nodo_ady,3] = v
			elif tabla[v-1,2] + a_m[v-1][nodo_ady] < tabla[nodo_ady,2]:
				tabla[nodo_ady,2] = tabla[v-1,2] + a_m[v-1][nodo_ady]
				tabla[nodo_ady,3] = v
	tabla[v-1,1] = 1
	print(tabla)

	no_visitados = np.where(tabla[:,1] == 0)
	if len(no_visitados[0]) > 0:
		filas_nv = [i for i in no_visitados[0]]
		dist_min = min(tabla[filas_nv,2]) 
		for i in range(len(tabla)):
			if tabla[i][2] == dist_min and tabla[i][1] == 0:
				nodo = tabla[i][0]
		pila.append(nodo)
		
start, end, camino_javier, seguir, guardar = 21, 32, [], True, True

while seguir:
	fila_end = np.where(tabla[:,0] == end)
	camino_javier.append(end)
	if guardar:
		costo = tabla[fila_end[0][0],2]
	guardar = False
	end = tabla[fila_end[0][0],3]
	if tabla[fila_end,0] == start:
		seguir = False
print('el camino de costo mínimo es: '+str(camino_javier[::-1]))
print('costo: '+str(costo))

'''
data_frame2 = pd.read_excel("tabla_andreina.xlsx")
a_m = []
tabla = []

for i in range(36):
  a_m.append(data_frame[i+1].tolist())
  tabla.append(data_frame2[i+1].tolist())

tabla = np.array(tabla)
pila = [21] 


while pila:
	v = pila.pop() #sacar primer elemento de la pila 
	print('visito: '+str(v))

	for nodo_ady in range(len(a_m[v-1])):
		if a_m[v-1][nodo_ady] != 0 and tabla[v-1,1] == 0:
			if tabla[nodo_ady,0] == 32:
				if v!=26 and tabla[v-1,2] + a_m[v-1][nodo_ady] < tabla[nodo_ady,2]:
					tabla[nodo_ady,2] = tabla[v-1,2] + a_m[v-1][nodo_ady]
					tabla[nodo_ady,3] = v
			elif tabla[v-1,2] + a_m[v-1][nodo_ady] < tabla[nodo_ady,2]:
				tabla[nodo_ady,2] = tabla[v-1,2] + a_m[v-1][nodo_ady]
				tabla[nodo_ady,3] = v
	tabla[v-1,1] = 1
	print(tabla)

	no_visitados = np.where(tabla[:,1] == 0)
	if len(no_visitados[0]) > 0:
		filas_nv = [i for i in no_visitados[0]]
		dist_min = min(tabla[filas_nv,2]) 
		for i in range(len(tabla)):
			if tabla[i][2] == dist_min and tabla[i][1] == 0:
				nodo = tabla[i][0]
		pila.append(nodo)
		
start, end, camino_javier, seguir, costo = 21, 32, [], True, 0

while seguir:
	fila_end = np.where(tabla[:,0] == end)
	camino_javier.append(end)
	costo += tabla[fila_end[0][0],3]
	end = tabla[fila_end[0][0],3]
	if tabla[fila_end,0] == start:
		seguir = False
print('el camino de costo mínimo es: '+str(camino_javier[::-1]))


def verificar_cuadra(v, dist):
	cont = 0
	for nodo in camino_javier:
		if a_m[v-1][nodo-1] == dist and nodo != 32:
			cont +=1 
	if cont > 0:
		return True
	else: 
		return False

while pila:
	v = pila.pop() #sacar primer elemento de la pila 
	print('visito: '+str(v))

	for nodo_ady in range(len(a_m[v-1])):
		if a_m[v-1][nodo_ady] != 0 and tabla[v-1,1] == 0:
			if v == 21:
				tabla[nodo_ady,2] = tabla[v-1,2] + a_m[v-1][nodo_ady]
				tabla[nodo_ady,3] = v
			if tabla[v-1,2] + a_m[v-1][nodo_ady] < tabla[nodo_ady,2] and verificar_cuadra(v, tabla[v-1,2])==False:
				tabla[nodo_ady,2] = tabla[v-1,2] + a_m[v-1][nodo_ady]
				tabla[nodo_ady,3] = v
			elif tabla[v-1,2] + a_m[v-1][nodo_ady] < tabla[nodo_ady,2] and verificar_cuadra(v, tabla[v-1,2]):
				tabla[nodo_ady,2] = 0
			if tabla[v-1,2] + a_m[v-1][nodo_ady] > tabla[nodo_ady,2] and verificar_cuadra(v, tabla[v-1,2])==False:
				tabla[nodo_ady,2] = tabla[v-1,2] + a_m[v-1][nodo_ady]
				tabla[nodo_ady,3] = v
			elif tabla[v-1,2] + a_m[v-1][nodo_ady] < tabla[nodo_ady,2] and verificar_cuadra(v, tabla[v-1,2]):
				tabla[nodo_ady,2] = 0
	tabla[v-1,1] = 1
	print(tabla)

	no_visitados = np.where(tabla[:,1] == 0)
	if len(no_visitados[0]) > 0:
		filas_nv = [i for i in no_visitados[0]]
		dist_min = min(tabla[filas_nv,2]) 
		for i in range(len(tabla)):
			if tabla[i][2] == dist_min and tabla[i][1] == 0:
				nodo = tabla[i][0]
		pila.append(nodo)

start, end, camino, seguir = 21, 32, [], True

while seguir:
	fila_end = np.where(tabla[:,0] == end)
	camino.append(end)
	end = tabla[fila_end[0][0],3]
	if tabla[fila_end,0] == start:
		seguir = False
print('el camino de costo mínimo es: '+str(camino[::-1]))
'''