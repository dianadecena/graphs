def depth_first(start):
	a_m = [[0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0]]
	pila = [start] #se guarda el valor del nodo inicial en la pila
	visitados = [False]*len(a_m) #se inicializa el array de visitados en falso 
	add = True

	while pila: #recorrer el grafo mientras la pila no esté vacía 
		print('pila: '+str(pila))
		v = pila.pop() #sacar primer elemento de la pila 
		print('visito: '+str(v))
		if v == start: #si el nodo es el comienzo se pone add en true para que solo se agregue a la pila el primer hijo que se encuentre
			add = True
		if visitados[v-1] == False: #cuando se visita el nodo se cambia a true en el array de visitados 
			visitados[v-1] = True
		for h in range(len(a_m[v-1])): #se recorre la matriz de adyacencia  
			if a_m[v-1][h] == 1 and visitados[h] == False: #si el valor en esa posición es 1 y ese nodo no ha sido visitado 
				if v == start and add == True: #si el nodo es el comienzo y add está en true 
					if v not in pila: #se verifica que el nodo no esté en la pila 
						pila.append(v) #se agrega el nodo a la pila
					pila.append(h+1) #se agrega el primer hijo de ese nodo por orden 
					visitados[h] = True #se cambia en el array de visitados el valor a true en la posición de ese nodo 
					add = False #se pone en falso a la variable add para que no agreguen más hijos porque es el nodo del comienzo 
				elif v!= start: #si el nodo no es el del comienzo 
					if v not in pila: #se verifica que el nodo no esté en la pila
						pila.append(v) #se agrega el nodo a la pila 
					pila.append(h+1) #se agregan todos los hijos de ese nodo a la pila porque no es el nodo del comienzo 
					visitados[h] = True #se cambia en el array de visitados el valor a true en la posición de ese nodo 

depth_first(int(input('starting node: ')))

