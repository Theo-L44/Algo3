def recibirInput():
    n:int = int(input().strip())
    palabra:str = input().split()

    respuesta:int = cantidadSubsecuencias(n, palabra)
    return respuesta

def cantidadSubsecuencias(n:int, palabra:str):
    invalido:int = 10**15
    cambios:int = 0

    memoria = []
    
    return 1 

if __name__ == "__main__":
    cantOperaciones = recibirInput()
    print(cantOperaciones)