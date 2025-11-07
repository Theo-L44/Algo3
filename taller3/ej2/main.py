import heapq

def recibirInput():
    datos = input().split()
    cantPlanetas:int = int(datos[0])
    cantPortales:int = int(datos[1])
    grafo = []

    for i in range(2,cantPortales+1):
        


    res:int = contarTiempo(grafo)
    
    return res

def contarTiempo(grafo):
    
    tiempoTotal:int = 0
    
    grafo.append(0)
    calculados = set()
    calculados.add(0)

if __name__ == "__main__":
    respuesta = str(recibirInput())
    print(respuesta)


#usar .heapify() para transformar una lista en un min-heap