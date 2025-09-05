def recibirInput()->list[str]: #recibo el input puesto en consola
    cantidadCasos = int(input())
    palabras:list[str] = []     
    for i in range(0,cantidadCasos):
        cantidadLetras = int(input()) #no me sirve realmente, aprovecho para descartar la linea de los largos de palabras
        palabra = input()
        palabras.append(palabra)
    
    return palabras


def cantidadesDeCambios(palabras:list[str])->list[int]: #por cada palabra llamo a la funcion que calcula los cambios que hay que hacer y devuelvo una lista con los cambios
    listaDeCambios:list[int] = [] #creo una lista que va a tener las cantidades de cambios minimos que hay que hacerle a cada palabra para que sean 'a'-lindas

    for palabra in palabras:
        listaDeCambios.append(str(esPalabraLinda(len(palabra),palabra,'a'))) #esto debería calcular cuantos cambios hay que hacerle a la palabra determinada
    
    return listaDeCambios


def esPalabraLinda(largo:int, palabra:str, letra:str) -> int: #aca decido si el string es l-lindo o no y devuelvo cuantos cambios hubo que hacer hasta que efectivamente fue a-lindo, se devuelve en forma de int
    cambios:int = 0

    if len(palabra) == 1 and palabra==letra: #casos base
        return cambios #no hubo ningún cambio
    elif len(palabra) == 1 and palabra!=letra:
        cambios += 1 #sumo uno a cambios porque no coinciden las letras
        return cambios
    
    mitad: int = largo // 2 #calculo donde esta la mitad del string para separar las dos mitades y hacer DyC
    mitadIzq: str = palabra[:mitad] 
    mitadDer: str = palabra[mitad:]

    #veo el camino que me conviene de dos casos, si la mitad izq requiere menos cambios que la derecha, elijo esa, si no el caso contrario 

    letrasDistintasCaso1:int = 0 #este es el caso donde la primer mitad es l-linda y la segunda l+1 linda
    for l in mitadIzq:
        if l != letra:
            letrasDistintasCaso1 += 1
    letrasDistintasCaso1 += esPalabraLinda(len(mitadDer), mitadDer, chr(ord(letra)+1)) 

    letrasDistintasCaso2:int = 0 #este es el caso donde la segunda mitad es l-linda y la primer mitad es l+1 linda
    for l in mitadDer:
        if l != letra:
            letrasDistintasCaso2 += 1
    letrasDistintasCaso2 += esPalabraLinda(len(mitadIzq), mitadIzq, chr(ord(letra)+1))

    if letrasDistintasCaso1 <= letrasDistintasCaso2: #miro a ver que caso me conviene
        return letrasDistintasCaso1
    else:
        return letrasDistintasCaso2


if __name__ == "__main__":
    strings = recibirInput() #recibo las palabras junto con sus largos
    output = cantidadesDeCambios(strings) #calculo las menores cantidades de cambios que le debo hacer a cada palabra para que sean 'a'-lindas
    for i in output:
        print(i) #devuelvo las palabras