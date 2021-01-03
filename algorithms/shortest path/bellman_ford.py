import numpy as np 

a_m = [[0, 3, 999, 5], [999, 0, 2, 999], [999, 999, 0, 999], [999, -4, 3, 0]]
#a_m = [[0, 3, 0, 5], [0, 0, 2, 0], [0, 0, 0, -3], [0, -4, 0, 0]]
#nodo - dist min desde 1 - predecesor
tabla = np.array([[1, 0, 0], [2, 999, 0], [3, 999, 0], [4, 999, 0]]) 
arcos = [[1, 4], [1, 2], [4, 2], [4, 3], [2, 3]]
#arcos = [[1, 4], [1, 2], [4, 2], [3, 4], [2, 3]]
iteracion = 1
cambio = False

while iteracion <= len(a_m):
	print('iteración: '+str(iteracion)) 
	for arco in arcos:
		print('arco: '+str(arcos.index(arco)+1))
		if tabla[arco[0]-1,1] + a_m[arco[0]-1][arco[1]-1] < tabla[arco[1]-1,1]:
			cambio = True
			tabla[arco[1]-1,1] = tabla[arco[0]-1,1] + a_m[arco[0]-1][arco[1]-1]
			tabla[arco[1]-1,2] = arco[0]
			print(tabla)
		else:
			print('sin cambios')
	if cambio:
		iteracion = iteracion + 1 
		cambio = False
	else: 
		break