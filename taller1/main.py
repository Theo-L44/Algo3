def recibirInput()->list[str]:
    cantidadCasos = int(input())
    palabras:list[str] = []     
    for i in range(0,cantidadCasos):
        cantidadLetras = int(input()) #no me sirve realmente, aprovecho para descartar la linea de los largos de palabras
        palabra = input()
        palabras.append(palabra)
    
    return palabras


def cantidadesDeCambios(palabras:list[str])->list[int]:
    listaDeCambios:list[int] = []

    for palabra in palabras:
        listaDeCambios.append(str(esPalabraLinda(len(palabra),palabra,'a'))) #esto debería calcular cuantos cambios hay que hacerle a la palabra determinada
    
    return listaDeCambios


def esPalabraLinda(largo:int, palabra:str, letra:str) -> int: #aca decido si el string es l-lindo o no y devuelvo si hay que hacer un cambio o no en forma de int
    cambios:int = 0

    if len(palabra) == 1 and palabra==letra: #casos base
        return cambios #no hubo ningún cambio
    elif len(palabra) == 1 and palabra!=letra:
        cambios += 1 #sumo uno a cambios porque no coinciden las letras
        return cambios
    
    mitad: int = largo // 2 #div entera 
    mitadIzq: str = palabra[:mitad]
    mitadDer: str = palabra[mitad:]

    letrasDistintasCaso1:int = 0
    for l in mitadIzq:
        if l != letra:
            letrasDistintasCaso1 += 1
    letrasDistintasCaso1 += esPalabraLinda(len(mitadDer), mitadDer, chr(ord(letra)+1))

    letrasDistintasCaso2:int = 0
    for l in mitadDer:
        if l != letra:
            letrasDistintasCaso2 += 1
    letrasDistintasCaso2 += esPalabraLinda(len(mitadIzq), mitadIzq, chr(ord(letra)+1))

    if letrasDistintasCaso1 <= letrasDistintasCaso2:
        return letrasDistintasCaso1
    else:
        return letrasDistintasCaso2


if __name__ == "__main__":
    strings = recibirInput()
    output = cantidadesDeCambios(strings)
    for i in output:
        print(i)



#Input
'''
6
8
aaaadcbb
8
bbaaceaa
8
jkghasdf
1
x
2
da
8
ccddaabb
'''


#Output
'''
0
4
7
1
1
5
'''