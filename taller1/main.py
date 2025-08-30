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

def esStringLindo(palabra:str, letra:str) -> int: #aca decido si el string es l-lindo o no y devuelvo si hay que hacer un cambio o no

    if len(palabra) == 1 and palabra==letra:
        return print(0)
    else:
        return 1

esStringLindo('a', 'b')
 