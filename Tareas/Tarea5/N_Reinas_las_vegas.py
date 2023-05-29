import random # Se importa la libreria de random para la generacion de numeros enteros

def NReinas(n,tablero): #Funcion principal del programa usando Las Vegas
    #n: Tamanio del tablero
    # Se inicializa la lista vacia correspondiente a las n columnas que estaran disponibles
    columnas_candidatas = []
    for a in range(n):#Se itera sobre las n numeros correspondientes a las columnas del tablero
        columnas_candidatas += [a]#Se concatena la actual columna a
    fila_actual = 0 #Variable que representa la fila que se esta procesando

    #Ciclo while que se ejecuta hasta que todas las columnas esten ocupadas o fila_actual sea mayor que n
    #si fila_actual > n todas las filas se han procesado
    while( len(columnas_candidatas) != 0 and fila_actual < n):
        columnas_disponibles = [] #Lista con las posiciones de las columnas disponibles
        for i in columnas_candidatas:#Se concatenan las posiciones de las columnas candidatas comprobando que no son atacadas las reinas
            if(comprobar_ataques(tablero, fila_actual, i)):#Se verifica si la posicion fila_actual,i es segura para la reina
                columnas_disponibles += [i]#Se concatena la posicion de la columna
        if (len(columnas_disponibles) == 0):#Se verifica si no hay columnas seguras para posicionar a las reinas
           #En caso de no haber columnas seguras para la fila actual se retorna false indicando que no hay solucion
            return False
        aleatorio = random.choice(columnas_disponibles) #Se selecciona aleatoriamente la posicion de una columna de las disponibles
        tablero[fila_actual][aleatorio] = 1#Se posiciona a una reina en La fila actual y la columna aleatoria calculada
        fila_actual += 1#Se incrementa la fila actual
        columnas_candidatas.remove(aleatorio)#Se remueve al numero aleatoria de los indices de las columnas candidatas
    return True #Se retorna true indicando que se encontro un tablero solucion

#Función para verificar si una reina en la fila y columna que esta posicionada del tablero está siendo atacada por otra reina.
def comprobar_ataques(tablero, fila, columna):
    #Se comprueba si existe alguna reina en la misma fila, es decir si esta siendo atacada horizontalmente
    for i in range(columna):
        if tablero[fila][i]:#Se verifica si hay una reina en esta posicion de la fila
            return False#Se retorna false indicando que la reina esta siendo atacada

    #Se asignan a las variables i,j la fila y la columna para verificar ataques diagonales izquierdos
    i = fila
    j = columna
    while (i >= 0 and j >= 0):#Mientras las posiciones de la fila y la columna sean mayores que cero
        if tablero[i][j]:#Se verifica si hay una reina en esta posicion (i,j)
            return False#Se retorna false indicando que esta sieno atacada
        i -= 1 # Se decrementa la fila
        j -= 1 # Se decrementa la columna
    #Se asignan nuevamente a i,j la fila y columna para verificar ataques diagonales derechos
    i = fila
    j = columna
    while (i >= 0 and j < len(tablero)):#Mientras las posicion de i sea mayor que cero y j sea menor que N o el largo del tablero
        if (tablero[i][j]):#Se verifica si hay una reina en esta posicion (i,j)
            return False#Se retorna false indicando que esta siendo atcada
        i -=  1#Se decrementa i
        j +=  1# Se incrementa j
#Se retorna True indicando que no hay ataques hacia esta reina
    return True

#Main del programa
if __name__ == "__main__":
    soluciones = 0 #Contador de soluciones correctas
    num_iteraciones = 200
    N = 8#int(input())
    print(f"Tableros soluciones son: ")
    for a in range(200):
        tablero = [[0 for j in range(N)] for i in range(N)]
        if (NReinas(N,tablero) == True):#Se verifica si se encontro un tablero solucion valido
           #Se imprime este tablero valido
            for p in tablero:
                print(f"\t{p}")
            print("\n")
            soluciones += 1#Se incrementa el contador de soluciones correctas
    print(f"Empleando {N} reinas y calculando {num_iteraciones} veces: ")
    print(f"\tSoluciones correctas: {soluciones}")
    print("\tLa tasa de exito es: ", soluciones/num_iteraciones)


