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
    
    grafo.append((inicio,0))
    calculados = [inicio] #valores por los que pase
    

    while fin not in calculados: #hago todas las operaciones, luego si fin aparece en la lista de calculados
       actual, movimientos= grafo.popleft()
       rojo = actual * 2
       azul = actual - 1
       #boton rojo
       if rojo<=(10000) and rojo not in calculados:
        calculados.append(rojo)
        grafo.append((rojo,movimientos+1))

        #boton azul
        if azul >=1 and azul not in calculados:
           calculados.append(azul)
           grafo.append((azul,movimientos+1))
    
    return movimientos

if __name__ == "__main__":
    respuesta = recibirInput()
    print(respuesta)

#--------------------------------------------------
