from collections import deque 

def recibirInput():
    datos = input().split()
    inicio:int = int(datos[0])
    fin:int = int(datos[1])
    
    res = contarClicks(inicio,fin)
    return res

def contarClicks(inicio,fin):
    if inicio>=fin:
        return inicio-fin #devuelvo la diferencia (sería la cantidad de clicks en botón azul)
    
    grafo = deque()
    movimientos:int = 0
    
    grafo.append(inicio)
    visitados = [inicio] #valores por los que pase
    

    while fin not in visitados:
       siguiente = visitados[len(visitados)-1] * 2 #boton rojo
       if siguiente<=(10^4) and siguiente not in visitados:
        visitados.append(siguiente)
        grafo.append(siguiente)
        movimientos +=1


        siguiente = visitados[len(visitados)-2] - 1
        #boton azul
        if siguiente >=1 and siguiente not in visitados:
           visitados.append(siguiente)
           grafo.append(siguiente)
           movimientos += 1
    
    return movimientos

if __name__ == "__main__":
    respuesta = recibirInput()
    print(respuesta)
