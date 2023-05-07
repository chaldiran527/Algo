def comprobar_ataques(i, j):#Función para verificar si una reina en la posición i,j del tablero está siendo atacada por otra reina.
    #Comprobar vertical y horizontalmente
    for k in range(0,N):
        if tablero[i][k]==1 or tablero[k][j]==1:
            return True
    #Comprobar diagonalmente
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if tablero[k][l]==1:
                    return True
    return False


def N_reinas(n):#Función principal para resolver el problema de las N reinas utilizando backtracking
    #Se verifica si n es 0 para saber si se colocaron las reinas y se encontro una solucion correcta
    if n==0:
        return True

    #Se itera sobre todas las celdas del tablero
    for i in range(0,N):
        for j in range(0,N):
            #Si la celda actual no está siendo atacada y no tiene una reina se le coloca una reina
            if (not(comprobar_ataques(i,j))) and (tablero[i][j]!=1):
                tablero[i][j] = 1
                #Se llama recursivamente a la función para colocar la siguiente reina en el tablero
                if N_reinas(n-1)==True:
                    return True
                #Si no se pudo colocar la siguiente reina, se borra la reina en la posicion actual y se continua buscando otra posicion
                tablero[i][j] = 0

    #Se retorna false sino se encontro una posicion valida
    return False

#Main del programa
if __name__ == "__main__":
    #N numero de reinas
    N = 8
    #Se crea el tablero NxN que en este caso es 8x8
    tablero = [[0] * N for _ in range(N)]
    print("Tablero solucion con las 8 reinas: ")
    N_reinas(N)
    for i in tablero:
        print(f"\t{i}")





