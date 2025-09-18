def recibirInput()->list[int]: #recibo el input puesto en consola
    entrada:list[int] = input().split()
    numero:list[int] = [int(entrada[0])]
    rango:list[int] = [int(entrada[1]),int(entrada[2])]

    if numero[0] != 1 and numero[0] != 0: #me pasaron un numero que no es 0 ni 1
        numero = [numero[0]//2, numero[0]%2, numero[0]//2]
    elif numero[0]==1: #me pasaron solo un 1
        return 1
    else: #me pasaron un 0
        return 0    
    
    listaDeUnos:list[int] = convertirEnUnos(numero)

    cantidadDeUnos:int = 0

    for i in range(rango[0]-1, rango[1]+1): 
        if listaDeUnos[i] == 1:
            cantidadDeUnos += 1

    return cantidadDeUnos

def convertirEnUnos(n:list[int])->list[int]:
    
    listaDeUnos:list[int] = n

    if len(listaDeUnos)==1 and (listaDeUnos[0]==1 or listaDeUnos[0]==0): #casos en el que la lista tiene solo 1 elemento
        return listaDeUnos
    elif len(listaDeUnos)==1:
        listaDeUnos = [listaDeUnos[0]//2, listaDeUnos[0]%2, listaDeUnos[0]//2]
        convertirEnUnos(listaDeUnos)

    for n in range(len(listaDeUnos)):
        if listaDeUnos[n]>1:
            listaDeUnos.extend(convertirEnUnos([listaDeUnos[n]]))

    return listaDeUnos

if __name__ == "__main__":
    print(recibirInput())