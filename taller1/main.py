def recibirInput():
    cantidadCasos = int(input())
    palabras = []     
    for i in range(0,cantidadCasos):
        cantidadLetras = int(input()) #no me sirve realmente
        palabra = input()
        palabras.append((cantidadLetras,palabra))
    
    return palabras #acá tengo que hacer el output que va a consola


def cantidadesDeCambios(palabras:list[str]):
    resultado = []

    for i in range(len(palabras)):
        resultado.append(str(esPalabraLinda(palabras[i][1],'a'))) #esto debería calcular cuantos cambios hay que hacerle a la palabra determinada
    
    return


def esPalabraLinda(palabra:str, letra:str) -> int: #aca decido si el string es l-lindo o no y devuelvo si hay que hacer un cambio o no en forma de int
    cambios:int = 0
    if len(palabra) == 1 and palabra==letra: #casos base
        return cambios#no hubo ningún cambio
    elif len(palabra) == 1 and palabra!=letra:
        cambios += 1 #sumo uno a cambios
        return cambios
    
    mitad: int = len(palabra) // 2 #div entera 
    mitadIzq: str = palabra[:mitad]
    mitadDer: str = palabra[mitad:]

    if esPalabraLinda(mitadIzq, letra)==0 and esPalabraLinda(mitadDer, chr(ord(letra)+1))==0:
        return cambios
    elif esPalabraLinda(mitadDer, letra)==0 and esPalabraLinda(mitadIzq, chr(ord(letra)+1))==0:
        return cambios
    else: #no se bien que hacer aca, hay un problema con la logica
        return cambios  
        

if __name__ == "__main__":
    recibirInput()


#esStringLindo('a', 'b')
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


################ PRUEBAS ################ 
'''def esLindo(s:str, l:str )->bool: #s es el string y l es la letra que hace que el string sea l-lindo
    if len(s) == 1 and s==l: #caso base
        return True
    
    mitad: int = len(s) // 2 #div entera 
    mitadIzq: str = s[:mitad]
    mitadDer: str = s[mitad:]

    if esLindo(mitadIzq, l) and esLindo(mitadDer, chr(ord(l)+1)):
        return print((esLindo(mitadIzq, l) and esLindo(mitadDer, chr(ord(l)+1))))
    elif esLindo(mitadDer, l) and esLindo(mitadIzq, chr(ord(l)+1)):
        return print((esLindo(mitadIzq, l) and esLindo(mitadDer, chr(ord(l)+1))))
    else: 
        return False

esLindo('aaaa','a')'''


'''def cantidadDeCambios()->int: #aca tomo los valores input 
    cuantasPalabras:str = input()
    for i in range (0,2):

    largoPalabra:int = input()
    cambiosHechos:int = 0
    
    
    
    return 0'''
