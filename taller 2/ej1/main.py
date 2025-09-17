memoria = [] 

def recibirInput():
    n = int(input().strip()) #string entero
    
    costos = input().split() #me devuelve la linea de los costos 
    
    for i in range(n):
        costos[i] = int(costos[i])

    palabras = []
    
    for i in range(n):
        palabras.append(input().strip())

    respuesta = calcularCambios(n,costos,palabras)

    return respuesta
 

def calcularCambios(n,costos,palabras):
    return True

if __name__ == "__main__":
    movimientos = recibirInput()
    print(movimientos)

#para dar vuelta un string uso reversed_string = my_string[::-1] entonces paso de 'hola' a 'aloh'
#para obtener el valor de una letra (a=1, b=2, etc), uso 
