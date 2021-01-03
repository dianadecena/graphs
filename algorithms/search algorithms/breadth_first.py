def breadth_first(start):
	a_m = [[0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0]]
	cola = [] #se crea un array que será la cola 
	visitados = [False]*len(a_m) #se inicializa el array de visitados en falso
	seguir = True #se crea una variable booleana para el bucle del recorrido 
	v = start #v primero será el nodo inicial 
	
	while seguir:
		if cola:
			v = cola.pop(0) #sale de la cola el primer elemento y será el nodo que se visitará 
		print('visito: '+str(v))
		for h in range(len(a_m[v-1])): #recorrer la matriz de adyacencia 
			if a_m[v-1][h] == 1: #si el valor en esa posición es igual a 1 
				visitados[v-1] = True #se cambia el valor en el array porque el nodo ya ha sido visitado
				if visitados[h] == False and h+1 not in cola: #se verifica que el nodo no ha sido visitado y que no esté en la cola
					cola.append(h+1) #se agrega el nodo a la cola 
		print('cola: '+str(cola))
		if False not in visitados: #si no hay ningún false en el array de visitados se sale del bucle 
			seguir = False

breadth_first(int(input('starting node: ')))

