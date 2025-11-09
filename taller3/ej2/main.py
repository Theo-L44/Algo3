import heapq

def recibirInput():
    datos = input().split()
    cantPlanetas:int = int(datos[0])
    cantPortales:int = int(datos[1])
    portales = []

    for _ in range(cantPlanetas+1):
        portales.append([])

    for _ in range(cantPortales):
        datos = input().split()
        planetaInicio = datos[0]
        planetaDestino = datos[1]
        tiempo = datos[2]
        portales[planetaInicio].append((planetaDestino,tiempo)) #agrego en la posición "planetaInicio" los planetas a los que pouedo llegar desde ese planeta como una tupla planeta/tiempo
        portales[planetaDestino].append((planetaInicio,tiempo)) #como son bidireccionales los portales, agrego en la posicion 
    
    

    res:int = contarTiempo(portales)
    
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