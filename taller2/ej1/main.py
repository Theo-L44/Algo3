def recibirInput():
    n = int(input().strip()) #string entero
    costos = input().split() #me devuelve la linea de los costos 
    
    for i in range(n):
        costos[i] = int(costos[i])

    palabras = []
    
    for i in range(n):
        palabras.append(input().strip())

    respuesta = calcularCambios(n, costos, palabras)

    return respuesta
 
def calcularCambios(n,costos,palabras):
    invalido = 10**10
    cambios = 0

    memoria =[] #inicializo la matriz con el caso base del costo de girar la primer palabra
    
    for i in range(0,n): #completo el resto de espacios
        memoria.append([invalido,invalido])
    
    memoria[0][0] = 0 
    memoria[0][1] = costos[0]

    for i in range(1, n):
        revertidaAnterior = palabras[i-1][::-1]        

        #primero veo el caso revirtiendo la palabra anterior
        if palabras[i-1] <= palabras[i]:
            memoria[i][0] = min(memoria[i][1], memoria[i-1][0]) #veo si es menor que la palabra anterior 
        if revertidaAnterior <= palabras[i]:
            memoria[i][0] = min(memoria[i][1], memoria[i-1][1])

        revertida = palabras[i][::-1] #ahora revierto la palabra actual

        #ahora veo que pasa si tengo la palabra actual revertida    
        if palabras[i-1] <= revertida:
            memoria[i][1] = min(memoria[i][1], memoria[i-1][0] + costos[i])
        if revertidaAnterior <= revertida:
            memoria[i][1] = min(memoria[i][1], memoria[i-1][1] + costos[i])

    cambios = min(memoria[n-1][0], memoria[n-1][1])

    if cambios >= invalido:
        return -1
    else:
        return cambios

if __name__ == "__main__":
    movimientos = recibirInput()
    print(movimientos)

#para dar vuelta un string uso reversed_string = my_string[::-1] entonces pasa de 'hola' a 'aloh'
#para obtener el valor de una letra (a=1, b=2, etc), uso 

#>Input
# 3
# 100 200 300
# abc
# efg
# hij

# >Output
# 0

# >Input
# 3
# 100 200 300
# za
# yb
# xc

# >Output
# 300

# >Input
# 2
# 0 0
# casas
# abraza
# >Output
# -1
