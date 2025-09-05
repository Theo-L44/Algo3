def recibirInput()->list[int]: #recibo el input puesto en consola
    input = int(input().split)
    numeroAsqueroso = input[0]
    rango = [input[1],input[2]]

    listaDeUnos:list[int] = convertirEnUnos(numeroAsqueroso)

    cantidadDeUnos = 0

    for i in range(rango[0], rango[1]+1): 
        if listaDeUnos[i] == 1:
            cantidadDeUnos += 1

    return cantidadDeUnos

def convertirEnUnos(n:int)->list[int]:

    

    return []
if __name__ == "__main__":
    numero = recibirInput() #recibo las palabras junto con sus largos
    output = 0
    print(output)
