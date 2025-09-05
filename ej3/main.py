def recibirInput()->list[int]: #recibo el input puesto en consola
    input:list[int] = int(input().split())
    numeroAsqueroso:int = int(input[0])
    rango:list[int] = [input[1],input[2]]

    listaDeUnos:list[int] = convertirEnUnos(numeroAsqueroso)

    cantidadDeUnos = 0

    for i in range(rango[0], rango[1]+1): 
        if listaDeUnos[i] == 1:
            cantidadDeUnos += 1

    return cantidadDeUnos

def convertirEnUnos(n:int)->list[int]:
    listaDeUnos:list[int] = [n]

    for numero in listaDeUnos:
        if numero != 1 or numero!=0:
            convertirEnUnos(numero)

    return listaDeUnos


if __name__ == "__main__":
    numero = recibirInput() #recibo las palabras junto con sus largos
    output = 0
    print(output)
