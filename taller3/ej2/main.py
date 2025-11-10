import heapq

def recibirInput():
    datos = input().split()
    cantPlanetas:int = int(datos[0])
    cantPortales:int = int(datos[1])
    galaxia = []

    for _ in range(cantPlanetas+1):
        galaxia.append([])

    for _ in range(cantPortales):
        datos = input().split()
        planetaInicio = int(datos[0])
        planetaDestino = int(datos[1])
        tiempo = datos[2]
        galaxia[planetaInicio].append((planetaDestino,tiempo)) #agrego en la posición "planetaInicio" los planetas a los que pouedo llegar desde ese planeta como una tupla planeta/tiempo
        galaxia[planetaDestino].append((planetaInicio,tiempo)) #como son bidireccionales los portales, agrego en la posicion 
    
    viajeros = []
    for _ in range(cantPlanetas):
        datos = input().split()
        cantViajeros = int(datos[0]) #cantidad de viajeros que van a ocupar un portal de un planeta
        minutoEspera = [] #tiempos en los que aparecen los otros viajeros en los portales
        for n in range(1, cantViajeros+1):
            minutoEspera.append(int(datos[n]))
        viajeros.append(minutoEspera)


    res:int = contarTiempo(cantPlanetas, galaxia, viajeros)
    
    return res

def contarTiempo(cantPlanetas, galaxia, viajeros):
    
    tiempoTotal:int = -1 #no se puede llegar al planeta destino

    tiempoPortal = []
    
    for _ in range(0,cantPlanetas+1):
        tiempoPortal.append([10**18]) #propongo un numero enorme para despues comparar

    tiempoPortal[1]=0

    planetasSinExplorar  = [(0,1)] #(tiempo, planeta), el planeta 1 siempre tiene tiempo 0

    while len(planetasSinExplorar) != 0:
        nodoActual = heapq.heappop(planetasSinExplorar)

        if nodoActual[0] != tiempoPortal:
            continue

        if nodoActual[1] == cantPlanetas:
            tiempoTotal = nodoActual[0]
            break

        revisar = 0 #CAMBIAR NOMBRE DE VARIABLE
        for momento in viajeros[nodoActual[1]-1]:
            if momento < nodoActual[0]:
                continue
            if momento == nodoActual[0] + revisar:
                revisar += 1
        
        nuevoTiempo = nodoActual[0] + revisar
        for vecino, portal in galaxia[nodoActual[1]]:
            total = nuevoTiempo + portal
            if total < tiempoPortal[vecino]:
                tiempoPortal[vecino] = total
                heapq.heappush(planetasSinExplorar, (total, vecino))

    return tiempoTotal

if __name__ == "__main__":
    respuesta = str(recibirInput())
    print(respuesta)
