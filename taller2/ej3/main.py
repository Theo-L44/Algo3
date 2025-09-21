def recibirInput():
    n:int = int(input().strip()) #longitud del string
    palabra:str = input().split()

    respuesta:int = cantidadSubsecuencias(n, palabra)
    return respuesta

def cantidadSubsecuencias(n:int, palabra:str):
    invalido:int = 10**15
    memoria = []

    for i in range(n):
        memoria.append([invalido]*n) #revisar, creo la matriz

    for i in range(n): #
        memoria[i][i] = 1



    return 1 

if __name__ == "__main__":
    cantOperaciones = recibirInput()
    print(cantOperaciones)