from collections import deque 

def recibirInput():
    datos:list[int] = input().split()
    inicio:int = int(datos[0])
    fin:int = int(datos[1])
    grafo = deque()

    res:int = contarClicks(inicio,fin,grafo)
    
    return res

def contarClicks(inicio,fin,grafo):
    if inicio>=fin:
        return inicio-fin #devuelvo la diferencia (sería la cantidad de clicks en botón azul)
    
    movimientos:int = 0
    
    grafo.append((inicio,0))
    calculados:list[int] = [inicio] #valores por los que pase
    
    while fin not in calculados: #"apreto" los botones, luego si fin aparece en la lista de calculados ya tengo calculados los movimientos
       actual:int; movimientos:int= grafo.popleft()
       rojo:int = actual * 2
       azul:int = actual - 1
       
       #boton rojo
       if (rojo <= 10000) and (rojo not in calculados):
        calculados.append(rojo)
        grafo.append((rojo,movimientos+1))

        #boton azul
        if (azul >= 1) and (azul not in calculados):
           calculados.append(azul)
           grafo.append((azul,movimientos+1))
    
    return movimientos

if __name__ == "__main__":
    respuesta:int = recibirInput()
    print(respuesta)
