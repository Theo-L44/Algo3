def recibirInput():
    n:int = int(input().strip()) #longitud del string
    palabra:str = input().strip()
    
    memoria = [] #inicio la memoria
    invalido = 10**15

    for _ in range(n):
        memoria.append([invalido]*n) #creo la matriz
    
    respuesta = cantidadOperaciones(0, n - 1, palabra, memoria)
    return respuesta

def cantidadOperaciones(i, j, palabra, memoria): #abcba
    if i > j:
        return 0 #no tengo mas palabra (los rangos son invalidos)
    
    if memoria[i][j] != 10**15:
        return memoria[i][j] #ya tengo el resultado, no lo vuelvo a calcular
    
    if i == j:
        memoria[i][j] = 1 #caso base en el que tengo solo 1 letra
        return 1

    operaciones = 1 + cantidadOperaciones(i + 1, j, palabra, memoria) 
    
    for k in range(i + 1, j + 1): #busco letras iguales asi no las elimino, y quedan para el final
        if palabra[i] == palabra[k]:
            medio = cantidadOperaciones(i+1, k-1, palabra, memoria)
            faltante = cantidadOperaciones(k, j, palabra, memoria)
            letrasIguales = medio + faltante

            if letrasIguales < operaciones:
                operaciones = letrasIguales
    
    memoria[i][j] = operaciones #escribo la memoria
    return operaciones

if __name__ == "__main__":
    respuesta = recibirInput()
    print(respuesta)