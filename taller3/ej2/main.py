import heapq

def recibirInput():
    datos = input().split()
    cantidadPlanetas = int(datos[0])
    cantidadPortales = int(datos[1])
    galaxia = [] #es el mapa de la galaxia

    for _ in range(cantidadPlanetas+1):
        galaxia.append([])

    for _ in range(cantidadPortales):
        datos = input().split()
        planetaInicio = int(datos[0])
        planetaDestino = int(datos[1])
        tiempo = int(datos[2])
        galaxia[planetaInicio].append((planetaDestino, tiempo)) #agrego en la posición planetaInicio los planetas a los que pouedo llegar desde ese planeta como una tupla planeta/tiempo
        galaxia[planetaDestino].append((planetaInicio, tiempo)) #los portales son bidireccionales
    
    viajeros = []
    for _ in range(cantidadPlanetas):
        datos = input().split()
        cantViajeros= int(datos[0]) #cantidad de viajeros que van a ocupar un portal de un planeta en algun tiempo
        minutoEspera = [] #tiempos en los que aparecen los otros viajeros en los portales
        
        for viajero in range(1, cantViajeros+1):
            minutoEspera.append(int(datos[viajero])) 
        
        viajeros.append(minutoEspera) 

    res:int = contarTiempo(cantidadPlanetas, galaxia, viajeros)
    
    return res

def contarTiempo(cantidadPlanetas, galaxia, viajeros):
    tiempoTotal = -1 #no se puede llegar al planeta destino
    tiempoPortal = []
    
    for _ in range(0, cantidadPlanetas+1):
        tiempoPortal.append(10**18) #propongo un numero enorme para despues comparar por el mínimo

    tiempoPortal[1] = 0

    elegirCamino = [(0,1)] #(tiempo, planeta), el planeta 1 siempre tiene tiempo 0

    while len(elegirCamino) != 0:
        planetaActual = heapq.heappop(elegirCamino)

        if planetaActual[0] != tiempoPortal[planetaActual[1]]:
         continue

        if planetaActual[1] == cantidadPlanetas: #me fijo si es el último planeta (donde está Zargon)
            tiempoTotal = planetaActual[0] 
            break

        tiempoEspera = 0
        for n in viajeros[planetaActual[1]-1]:
            if n < planetaActual[0]: #llegué antes de que hubiesen otros viajeros
                continue
            if n == planetaActual[0] + tiempoEspera: #había un viajero y tuve que esperar
                tiempoEspera+=1
        
        nuevoTiempo = planetaActual[0] + tiempoEspera #tiempo en el que llegué al planeta + la cantidad de segundos esperados
        for planeta, portal in galaxia[planetaActual[1]]:
            total = nuevoTiempo + portal #sumo lo que me tomó cruzar al planeta por el portal + tiempo que tuve que esperar (si es que tuve que hacerlo)
            if total < tiempoPortal[planeta]: #si el tiempo del camino que hice es menor del que me hubiese tomado ir directo, entonces elijo ese primer camino
                tiempoPortal[planeta] = total 
                heapq.heappush(elegirCamino, (total, planeta)) #lo sumo al min-heap

    return tiempoTotal

if __name__ =="__main__":
    respuesta = str(recibirInput())
    print(respuesta)