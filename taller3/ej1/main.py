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
    calculados = set() #valores por los que pase
    calculados.add(inicio)
    
    while True: #"apreto" los botones, luego si fin aparece en la lista de calculados ya tengo calculados los movimientos 
       actual, movimientos= grafo.popleft()
       if actual == fin:
          return movimientos 

       rojo:int = actual * 2
       azul:int = actual - 1
       
       #boton rojo
       if (rojo <= 20000) and (rojo not in calculados):
        calculados.add(rojo)
        grafo.append((rojo,movimientos+1))

        #boton azul
        if (azul >= 1) and (azul not in calculados):
           calculados.add(azul)
           grafo.append((azul,movimientos+1))

if __name__ == "__main__":
    respuesta = str(recibirInput())
    print(respuesta)
