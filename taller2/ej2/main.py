def recibirInput():
    n:int = int(input().strip()) #longitud del string
    palabra:str = input().strip()
    
    memoria = [] #inicio la memoria
    invalido = 10**15
    
    if n == 0: #caso en el que no hay palabra
        return 0
    
    for _ in range(n):
        memoria.append([invalido]*n) #creo la matriz con valores invalidos
    
    respuesta = cantidadOperaciones(0, n - 1, palabra, memoria) #le paso los indices de inicio y fin de la palabra
    return respuesta

def cantidadOperaciones(i, j, palabra, memoria):
    if i > j:
        return 0 #no tengo mas palabra (los rangos son invalidos)
    
    if memoria[i][j] != 10**15: #ya tengo el resultado (veo si la matriz tiene un valor distinto "invalido"), no lo vuelvo a calcular
        return memoria[i][j] 
    
    if i == j:
        memoria[i][j] = 1 #caso en el que tengo solo 1 letra
        return 1

    operaciones = 1 + cantidadOperaciones(i + 1, j, palabra, memoria) #lo que me cuesta borrar todos los caracteres uno a uno
    
    for k in range(i + 1, j + 1):
        if palabra[i] == palabra[k]:
            medio = cantidadOperaciones(i+1, k-1, palabra, memoria) 
            faltante = cantidadOperaciones(k, j, palabra, memoria) #string que me falta calcular
            costo = medio + faltante 

            if costo < operaciones: #veo si el nuevo costo es menor a la cantidad de operaciones que ya tengo
                operaciones = costo
    
    memoria[i][j] = operaciones #reescribo la memoria
    return operaciones

if __name__ == "__main__":
    respuesta = recibirInput()
    print(respuesta)