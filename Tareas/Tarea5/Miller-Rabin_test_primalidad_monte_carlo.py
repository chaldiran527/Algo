#Se importa la libreria random para la generacion de numeros aleatorios
import random

def exponenciacion(x, y, p):#Funcion para realizar la exponenciacion modular del tipo (x^y) % p
    resultado = 1#Inicializar el resultado en 1
    x = x % p#En caso de que x es mayor o igual que p se actualiza el valor por el modulo de x divido entre p
    while (y > 0):
        if (y & 1):#Se verifica si y es impar
            resultado = (resultado * x) % p #Se multiplica x por el resultado para despues sacar el modulo p
        y = y >> 1 #Se divide a y entre 2 haciendo un shiftright
        x = (x * x) % p#Se toma el modulo p de el resultado de elevar x al cuadrado
    return resultado#Se retorna la exponenciacion modular resultante


def prueba_miller_rabin(d, n):
    #Funcion que ejecuta la prueba de primalidad de Miller-Rabin para  un numero dado n
    #Se elige un numero aleatorio en el rango [2..n-2]
    #Los casos especiales aseguran que n > 4
    a = 2 + random.randint(1, n - 4)
    #Se calcula el numero aleatorio  a^d % n para aplicar la formula (x^y) % p
    x = exponenciacion(a, d, n)
    if (x == 1 or x == n - 1):
        return True#Se retorna verdadero que es primo en caso de que sea uno o n-1

    #Se realiza el cuadrado de x
    while (d != n - 1):#Mientras d sea diferente al valor de n-1
        x = (x * x) % n#Se eleva x al cuadrado y se le saca el modulo n
        d *= 2#Se duplica d

        if (x == 1):#Se verifica si es igual a 1
            return False#Retornar false
        if (x == n - 1):#Se verifica si es igual a n-1
            return True#Retornar true

    #Se retorna false indicando que es un numero compuesto
    return False


def es_primo(n, k):#Funcion que comprueba si un numero n es primo llamando a la prueba de Miller-Rabin para primalidad
    #Se verifican los casos especiales primero
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    d = n - 1
    while (d % 2 == 0):
        d //= 2
    #Se itera k veces dado el numero n
    for i in range(k):
        if (prueba_miller_rabin(d, n) == False):
            return False
    return True#Se retorna verdadero indicando que el numero probablemente es primo


#Main del programa
if __name__ == "__main__":
    k = 20 # Cantidad k de iteraciones
    #Numeros de prueba
    num1 = 3
    num2 = 541
    num3 = 48
    print(f"Con un total de {k} iteraciones se tiene para los numeros {num1}, {num2} y {num3}:")
    if(es_primo(num1,k)):
        print(f"\tEl numero {num1} es probablemente primo")
    else:
        print(f"\tEl numero {num1} definitivamente es un numero compuesto no primo")

    if(es_primo(num2,k)):
        print(f"\tEl numero {num2} es probablemente primo")
    else:
        print(f"\tEl numero {num2} definitivamente es un numero compuesto no primo")

    if(es_primo(num3,k)):
        print(f"\tEl numero {num3} es probablemente primo")
    else:
        print(f"\tEl numero {num3} definitivamente es un numero compuesto no primo")


