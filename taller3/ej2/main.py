import heapq

def recibirInput():
    datos = input().split()
    cantidadPlanetas = int(datos[0])
    cantidadPortales = int(datos[1])
    galaxia = []

    for _ in range(cantidadPlanetas+1):
        galaxia.append([])

    for _ in range(cantidadPortales):
        datos = input().split()
        planetaInicio = int(datos[0])
        planetaDestino = int(datos[1])
        tiempo = int(datos[2])
        galaxia[planetaInicio].append((planetaDestino, tiempo)) #agrego en la posición "planetaInicio" los planetas a los que pouedo llegar desde ese planeta como una tupla planeta/tiempo
        galaxia[planetaDestino].append((planetaInicio, tiempo)) #como son bidireccionales los portales, agrego en la posicion 
    
    viajeros = []
    for _ in range(cantidadPlanetas):
        datos = input().split()
        cantViajeros = int(datos[0]) #cantidad de viajeros que van a ocupar un portal de un planeta
        minutoEspera = [] #tiempos en los que aparecen los otros viajeros en los portales
        
        for n in range(1, cantViajeros+1):
            minutoEspera.append(int(datos[n]))
        
        viajeros.append(minutoEspera)

    res:int = contarTiempo(cantidadPlanetas, galaxia, viajeros)
    
    return res

def contarTiempo(cantidadPlanetas, galaxia, viajeros):
    tiempoTotal:int = -1 #no se puede llegar al planeta destino
    tiempoPortal = []
    
    for _ in range(0,cantidadPlanetas+1):
        tiempoPortal.append(10**18) #propongo un numero enorme para despues comparar por el mínimo

    tiempoPortal[1] = 0

    elegirCamino = [(0,1)] #(tiempo, planeta), el planeta 1 siempre tiene tiempo 0

    while len(elegirCamino) != 0:
        nodoActual = heapq.heappop(elegirCamino)

        if nodoActual[0] != tiempoPortal[nodoActual[1]]:
            continue

        if nodoActual[1] == cantidadPlanetas:
            tiempoTotal = nodoActual[0]
            break

        tiempoEspera = 0
        for n in viajeros[nodoActual[1]-1]:
            if n < nodoActual[0]:
                continue
            if n == nodoActual[0] + tiempoEspera:
                tiempoEspera += 1
        
        nuevoTiempo = nodoActual[0] + tiempoEspera
        for siguientePlaneta, portal in galaxia[nodoActual[1]]:
            total = nuevoTiempo + portal
            if total < tiempoPortal[siguientePlaneta]:
                tiempoPortal[siguientePlaneta] = total
                heapq.heappush(elegirCamino, (total, siguientePlaneta))

    return tiempoTotal

if __name__ == "__main__":
    respuesta = str(recibirInput())
    print(respuesta)
