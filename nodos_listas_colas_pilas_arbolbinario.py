
############################################### CLASE NODO ###############################################

class Nodo():

	def __init__(self,dato=None,nxt=None):
		self.__dato = dato
		self.__nxt = nxt

	def getdato(self):
		return self.__dato

	def getnxt(self):
		return self.__nxt

	def setdato(self,nuevo_dato):
		self.__dato = nuevo_dato

	def setnxt(self,nuevo_nxt):
		self.__nxt = nuevo_nxt

####  print(n1.getData()[0])      Muestra el contenido de la posicion 0 del Nodo 1

############################################### CLASE LINKEDLIST ###############################################


class LinkedList():

	def __init__(self,head=None):
		self.__head = head

	def gethead(self):
		return self.__head

	def sethead(self,nuevo_head):
		self.__head = nuevo_head


############################################### FORMAS DE AGREGAR ###############################################

########### Agregar al Final ###########

	def agregaralFinal(self,dato):
		nuevo = Nodo(dato,None)
		act = self.__head
		#Caso 1: Esta vacia 
		if (act == None):
			self.__head = nuevo
		#Caso 2: No esta vacia
		else:
			while (act.getnxt() != None):
				act = act.getnxt()
			act.setnxt(nuevo)

	def agregaralPrincipio(self,dato):
		nuevo = Nodo(dato)
		#Caso 1: Esta vacia
		if self.__head == None:
			self.__head = nuevo
		#Cas0 2: No esta vacia
		else:
			nuevo.setnxt(self.__head)
			self.__head = nuevo

############################################### FUNCIONES ELIMINAR ###############################################

	def borraralFinal(self):
		tam = tamaniolista()
		#Caso 1: Un elemento en la lista
		if tam == 1:
			self.__head = None

		if self.__head != None:
			act = self.__head
			ant = act
			while act.getnxt() !=None:
				ant = act
				act = act.getnxt()
			ant.setnxt(None)
			act = ant

	def borraralPrincipio(self):
		aux = self.__head
		self.__head = aux.getnxt()

############################################### FUNCIONES POR POSICION ###############################################

	def agregarporPosicion(self,dato,posicion):
		nuevo = Nodo(dato)
		tam = self.tamaniolista()
		#Caso 1: Lista vacia
		if posicion == 0:
			agregaralPrincipio(dato)
		else:
			if(posicion > tam):
				#Caso 2: Final de lista en caso de que la posicion sea mayor al tamaño de la lista
				agregaralFinal(dato)
			else:
				#La posición esta esta dentro del rango de la lista
				act = self.__head
				k = 1
				while act.getnxt() != None and k < posicion:
					act = act.getnxt()
					k = k + 1
				aux = act.getnxt()
				act.setnxt(nuevo)
				nuevo.setnxt(aux)

	def retornamosdatoenPosicion(self,posicion):
		if self.__head:
			act = self.__head
			i = 0
			while(act.getnxt() != None and i < posicion):
				act = act.getnxt()
				i = i + 1
			if(i == posicion):
				return act.getdato()
			else:
				print("La posicion ingresada no existe")

	def borrarAlFinal(self):
		if self.tamaniolista() == 1:
			self.__head = None

		if self.__head:     
			act = self.__head
			ant = act
			while act.getnxt() != None:
				ant = act
				act = act.getnxt()
			ant.setnxt(None)
			act = ant

	def borrarAlPrincipio(self):
		aux = self.__head
		self.__head = aux.getnxt()


	def borrarporPosicion(self, posicion):
		if self.tamaniolista() != 0:
			if posicion == 0:
				self.__head = None
				aux = act.getdato()
				return aux
			act = self.__head
			i = 0
			while act.getnxt() != None and i < posicion:
				act = act.getnxt()
				i = i + 1
			if act.getnxt() != None:
				aux = act.getdato()
				next_next = act.getnxt().getnxt()
				act.setnxt(next_next)
			return aux


############################################### TAMAÑO E IMPRIMIR ###############################################


	def imprimir(self):
		act = self.__head
		while act.getnxt() != None:
			print(act.getdato())
			act = act.getnxt()
		print(act.getdato())



	def tamaniolista(self):
		tam = 0
		if self.__head == None:
			return tam
		else:
			act = self.__head
			while act.getnxt() != None:
				tam = tam + 1
				act = act.getnxt()
			return tam +1



############################################### SCRIPT - LLAMADO DE FUNCIONES ###############################################


lista = LinkedList()                                #Creamos variable lista de clase Linkedlist
#lista.agregaralFinal(100)                          #Agregamos varios elementos al final
#lista.agregaralFinal(200)
#lista.agregaralFinal(300)
lista.agregaralFinal(400)
lista.agregaralFinal(500)
lista.agregaralFinal(50)
#lista.agregaralPrincipio(56)                       #Agregamos 2 elementos al principio
lista.agregaralPrincipio(56242423)
lista.imprimir()                                    #Imprimimos la lista
tamanio = lista.tamaniolista()                      #Le asignamos a la variable tamanio la funcion tamaniolista() que devuelve el tamaño de la misma
print("El tamaño de la lista es:"+str(tamanio))		#Imprimimos el tamaño de la lista
lista.agregarporPosicion(10,2)					#Agrega el elemento 10 en la posicion 2 de la lista
a = lista.retornamosdatoenPosicion(3)                    #Le asignamos a la variable a el dato de la posicion 3
print("El valor de la posicion 3 es: "+str(a))		#Imprimimos el dato de la posicion 3
aux = lista.borrarporPosicion(2)						#Borra el dato de la posicion 2 de la lista y lo guarda en una variable aux
print("El dato eliminado es el:"+str(aux))			#Imprime el elemento borrado
lista.imprimir()                                    #Imprimimos la lista de nuevo









############################################### PILA Y COLA ###############################################

class Pila():
	
	#Creamos una cola vacía
	def __init__(self):
		self.datos = Linkedlist()

	#Agregamos un elemento a la cola y devolvemos la cantidad de datos
	def push(self, dato):
		self.datos.agregaralFinal(dato)
		return self.datos.tamaniolista()
	
	#Elimina el primer elemento de la pila y devuelve su valor
	def pop(self):
		aux = self.datos.retornamosdatoenPosicion(self.datos.tamaniolista()-1) 
		self.datos.borrarAlFinal()
		return aux

	#Retorna sin eliminar un elemento de la cola
	def top(self):
		aux = self.datos.retornamosdatoenPosicion(self.datos.cantidad()-1)
		return aux

	#Invertir(Pila)
	def invertir(self):
		pila_nueva = Pila()
		while self.tamaniolista() > 0:
			pila_nueva.push(self.pop())
		return pila_nueva

	#Imprime todos los elementos de la cola sin modificarla
	def imprimirpila(self):
		self.datos.imprimir()


class Cola():
	
	#Creamos una cola vacía
	def __init__(self):
		self.datos = Linkedlist()

	#Agregamos un elemento a la cola y devolvemos la cantidad de datos
	def push(self, dato):
		self.datos.agregaralFinal(dato)
		return self.datos.tamaniolista()
	
	#Elimina el primer elemento de la cola y devuelve su valor
	def pop(self, pos):
		aux = self.datos.retornamosdatoenPosicion(0) 
		self.datos.borrarAlPrincipio()
		return aux

	#Retorna sin eliminar un elemento de la cola
	def top(self):
		aux = self.datos.retornamosdatoenPosicion(0) 
		return aux

	#Invertir(Pila)
	def invert(self):
		cola_nueva = Cola()
		pila = Pila()
		while self.tamaniolista() > 0:
			pila.push(self.pop())
		while pila.tamaniolista() > 0:
			cola_nueva.push(pila.pop())
		return cola_nueva

	#Imprime todos los elementos de la cola sin modificarla
	def imprimircola(self):
		self.datos.imprimir()



############################################### ARBOL Y CLASES ###############################################

class Producto():
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
class Nodo():

    def __init__(self, dato=None):
        self.izq = None
        self.der = None
        self.dato = dato

    def insertar(self, dato):
        if self.dato:
            if dato.precio < self.dato.precio:
                if self.izq is None:
                    self.izq = Nodo(dato)
                else:
                    self.izq.insertar(dato)
            elif dato.precio > self.dato.precio:
                if self.der is None:
                    self.der = Nodo(dato)
                else:
                    self.der.insertar(dato)
        else:
            self.dato = dato

    def imprimirArbol(self):
        if self.izq:
            self.izq.imprimirArbol()
        print( self.dato.nombre),
        if self.der:
            self.der.imprimirArbol()

root = Nodo()
a=Producto("arroz",40)
b=Producto("vino",120)
c=Producto("pan",60)
d=Producto("queso",140)
e=Producto("fideos",50)
f=Producto("agua",30)

l = [a,b,c,d,e,f]

for i in l:
    root.insertar(i)
root.imprimirArbol()