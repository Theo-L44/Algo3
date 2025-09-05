def recibirInput()->list[int]: #recibo el input puesto en consola
    input:list[int] = int(input().split())
    numeroAsqueroso:list[int] = [int(input[0])]
    rango:list[int] = [input[1],input[2]]

    if numeroAsqueroso[0] != 1:
        numeroAsqueroso = [numeroAsqueroso[0]//2, numeroAsqueroso[0]%2, numeroAsqueroso[0]//2]
        
    listaDeUnos:list[int] = convertirEnUnos(numeroAsqueroso)

    cantidadDeUnos = 0

    for i in range(rango[0], rango[1]+1): 
        if listaDeUnos[i] == 1:
            cantidadDeUnos += 1

    return cantidadDeUnos

def convertirEnUnos(n:list[int])->list[int]:
    listaDeUnos:list[int] = n

    mitad: int = len(listaDeUnos) // 2 #calculo donde esta la mitad del string para separar las dos mitades y hacer DyC
    mitadIzq: str = listaDeUnos[:mitad] 
    mitadDer: str = listaDeUnos[mitad:]

    for numero in listaDeUnos:
        if numero != 1 or numero!=0:
            convertirEnUnos(numero)

    return listaDeUnos

if __name__ == "__main__":
    numero = recibirInput() #recibo las palabras junto con sus largos
    output = 0
    print(output)