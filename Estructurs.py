def Stack():
    return []

# Verifica si la pila no tiene elementos
def isEmptyStack(pila):
    return len(pila)==0

# Adiciona un valor a la pila (al final)
def push(pila, valor):
    pila.append(valor)

# Elimina un valor de la pila (el ultimo)
def pop(pila):
    if not isEmptyStack(pila):
        return pila.pop()
    else:
        print("Error: pila vacia")
        return []

# Consulta el ultimo valor de la pila sin sacarlo
def top(pila):
    if not isEmptyStack(pila):
        return pila[-1]
    else:
        print("Error: pila vacia")
        return []

# Retorna la cantidad de elementos en la pila
def sizeStack(pila):
    return len(pila)

def Queue():
    return []

# Verifica si la cola no tiene elementos
def isEmptyQueue(cola):
    return len(cola)==0

# Adiciona un valor a la cola (al final)
def inQueue(cola, valor):
    cola.append(valor)

# Elimina un valor de la cola (el primero)
def deQueue(cola):
    if not isEmptyQueue(cola):
        return cola.pop(0)
    else:
        print("Error: cola vacia")
        return []

# Consulta el primer valor de la cola sin sacarlo
def frontQueue(cola):
    if not isEmptyQueue(cola):
        return cola[0]
    else:
        print("Error: cola vacia")
        return []

# Retorna la cantidad de elementos en la cola
def sizeQueue(cola):
    return len(cola)



##Inicio  - Elkin Idarraga Valencia

def imprimirCola(cola):
    aux = Queue()
    while not isEmptyQueue(cola):
        valor = deQueue(cola)
        print(valor, end="")
        inQueue(aux, valor)
    while not isEmptyQueue(aux):
        inQueue(cola, deQueue(aux))

    return cola

def imprimirPila(pila):
    aux = Stack()
    while not isEmptyStack(pila):
        valor = pop(pila)
        print(valor)
        push(aux, valor)
    while not isEmptyStack(aux):
        push(pila, pop(aux))

    return pila





operacionInterString = input("Ingrese la operacion: ")
print("Operacion ingresada:",operacionInterString)

cumple = True


#Pasar el string a una cola
operacionInter = Queue()
for i in range(0, len(operacionInterString)):
    inQueue(operacionInter, operacionInterString[i])      

#Comprobar si tiene parentesis y validarlos
auxP = Queue()
paren = Stack()

while not isEmptyQueue(operacionInter):
    valor1 = deQueue(operacionInter)
    if (valor1 == "(" ):
        push(paren, valor1)
    elif (valor1 == ")"):
        pop(paren)
    else:
        inQueue(auxP, valor1)

if(isEmptyStack(paren)):
    cumple = True
else:
    cumple = False

if (cumple !=True):
    print("\nLos parentesis no concuerdan, alguno de ellos no cierra, intentelo de nuevo")

while not isEmptyQueue(auxP):
    inQueue(operacionInter, deQueue(auxP))



#Pasar de interfijo a posfijo
signos = Stack()
numeros = Queue()
finalConversion = Queue()

while not isEmptyQueue(operacionInter) and cumple == True:
    valor = deQueue(operacionInter)
    if(valor == "+" or valor == "-" or valor == "*" or valor == "/"):
        push(signos, valor)
    else:
        inQueue(numeros, valor)
        if (sizeQueue(numeros) == 2):
            valor2 = deQueue(numeros)
            valor3 = deQueue(numeros)
            inQueue(finalConversion, valor2)
            inQueue(finalConversion, valor3)

            while not isEmptyStack(signos):
                valor4 = pop(signos)
                inQueue(finalConversion, valor4)


while not isEmptyQueue(numeros):
    inQueue(finalConversion, deQueue(numeros))

while not isEmptyStack(signos):
    inQueue(finalConversion, pop(signos))



imprimirCola(finalConversion)




#Operacion polaca

pila = Stack()

while not isEmptyQueue(finalConversion) and cumple == True:
    valor = deQueue(finalConversion)
    if(valor == "+"):
        valor1 = int(pop(pila))
        valor2 = int(pop(pila))
        op = valor1 + valor2
        push(pila, op)
    elif(valor == "-"):
        valor1 = int(pop(pila))
        valor2 = int(pop(pila))
        op = valor2 - valor1
        push(pila, op)
    elif(valor == "*"):
        valor1 = int(pop(pila))
        valor2 = int(pop(pila))
        op = valor1 * valor2
        push(pila, op)
    elif(valor == "/"):
        valor1 = float(pop(pila))
        valor2 = float(pop(pila))
        if(valor1 == 0 or valor2 == 0):
            print("\nNo esta definida la division por cero")
            break
        op = valor2 / valor1
        push(pila, op)
    else: #Es numero
        push(pila, valor)


if(cumple):
    print("\nEl resultado es: ")
    imprimirPila(pila)

