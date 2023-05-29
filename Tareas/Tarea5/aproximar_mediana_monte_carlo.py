#Se importa la libreria random para la generacion aleatoria
import random
#Se inicializan en nulo a las variables a & b que almacenaran los elementos que representan la mediana
a, b = None, None

def particion(arreglo, izq, der):#Funcion para realizar la particion del arreglo y devolver el indice de la particion
    ultimo = arreglo[der] #Se selecciona al ultimo indice o indice derecho como pivote
    #Se les asigna el indice izquierdo  a: i & j
    i = izq
    j = izq
    while (j < der):
        if (arreglo[j] < ultimo):#Se verifica si el elemento actual en el indice j es menor que el pivote
            #Se intercambia este elemento del indice j con el del indice i
            arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
            i += 1# Se incrementa el indice i
        j += 1#Se incrementa el indice j
#Se intercambian los valores del arreglo entre el elemento actual y el ultimo o derecho del subarreglo
    arreglo[i], arreglo[der] = arreglo[der], arreglo[i]
    return i# Se devuelve el indice final del pivote en el arreglo particionado

def particion_aleatoria(arr, izq, der):#Funcion para escoger un pivote aleatorio en el rango de elementos de 0 a n-1
    n = der - izq + 1 #Se calcula el tamanio del subarreglo en n
    pivote = random.randrange(1, 100) % n#Se escoge el elmento aleatorio dentro del subarreglo como pivote
    #Se intercambia el elemento seleccionado aleatoriamente con el ultimo
    arr[izq + pivote], arr[der] = arr[der], arr[izq + pivote]
    return particion(arr, izq, der)#Llama a realizar la particion y retorna el indice que se devuelve

def encontrar_mediana(arreglo, izq, der,k, a1, b1):#FUncion de utilidad recursiva que encuentra la mediana
    #a1 y b1 son los elementos candidatos a la mediana
    #k representa el indice de la mediana que se desea encontrar
    global a, b #Se declaran a estas variables como globales
    #Se verifica si el indice izquierdo o primero es menor o igual que el indice derecho o ultimo del subarreglo
    if (izq <= der):
        #Se llama a la funcion particion_aleatoria para obtener el indice
        indice_particion = particion_aleatoria(arreglo, izq, der)

        #Si el indice_particion es igual a k(indice de la mediana), entonces se encontro la mediana de los elementos de tamanio impar
        if (indice_particion == k):
            #Se asigna el valor de esta posicion del sub_arreglo en b que almacena a la mediana
            b = arreglo[indice_particion]
            #Se verifica si a1 es diferente a -1 para ver si se encontro el segundo elemento candidato a la mediana
            if (a1 != -1):#En caso de que se cumpla se sale de la funcion
                return
        #Si el indice es k-1 entonces a & b son los elementos medios del arreglo arr[] cuando el tamanio es par
        elif (indice_particion == k - 1):
            #Se asigna en a la posicion de este indice del subarreglo
            a = arreglo[indice_particion]
            #Se verificia si b1 es diferente a -1, significando que se ha encontrado el segundo elemento candidato b
            if (b1 != -1):#En caso de que se cumpla se sale de la funcion
                return
        #Se realiza esta verificacion adicional para determinar si el indice esta en la primera mitad o segunda mitad
        if (indice_particion >= k):#Si es mayor o igual a k esta en la primera mitad del subarreglo
            #Se hace el llamado recusivo de la funcion para buscar el indice en el subarreglo de la primera mitad del subarreglo actual
            return encontrar_mediana(arreglo, izq, indice_particion - 1, k, a, b)
        # Si es menor o igual que k se If partitionIndex <= k then find the index in second half of the arr[]
        else:# entonces #Se hace el llamado recusivo de la funcion para buscar el indice en el subarreglo de la segunda mitad del subarreglo actual
            return encontrar_mediana(arreglo,indice_particion + 1, der, k, a, b)
    #Si no se cumple que izq <= der significa que se ha llegado a un subarreglo vacio
    #Se hace un return y se finaliza la funcion
    return

def calcular_mediana(arreglo, n):#Funcion principal del programa para encontrar la mediana
    #Se declaran a & b como variables en el ambito global del programa
    global a
    global b
    #Variables candidatos a y b que almacenan las medianas candidatas posibles
    a = -1 #inicializada en -1
    b = -1 #tambien incializado en -1
    #Se verifica si la longitud del arreglo es impar o par
    if (n % 2 == 1):#Si n es impar, se busca a la mediana con el indice de mediana como n//2
        encontrar_mediana(arreglo, 0, n - 1, n // 2, a, b)#El resultado sera almacenado en b
        resultado = b
    else:#Si n es par, el indice de la mediana igualmente es n // 2, y el resultado se almacena en a & b
        encontrar_mediana(arreglo, 0, n - 1, n // 2, a, b)
        #El resultado se calcula como el promedio de a y b
        resultado = (a + b) // 2
    return resultado#Se retorna el resultado de la mediana


#Main del programa
if __name__ == "__main__":
    #Se calculan e imprimen las medianas de los 2 arreglos de prueba
    arr1 = [4, 2, 9, 7, 5, 1, 8, 6, 3]
    n1 = len(arr1)
    print(f"Mediana del arreglo 1 {arr1} de longitud impar es: {calcular_mediana(arr1,n1)}")

    arr2 = [2, 4, 6, 8, 10, 12]
    n2 = len(arr2)
    print(f"Mediana del arreglo 2 {arr2} de longitud par es: {calcular_mediana(arr2, n2)}")




