def recibirInput()->str:
    valores = input().split() #me va a devolver ['valor1', 'valor2'] donde valor 1 es desde donde empiezo, y valor 2 es donde yo quiero terminar
    valorInicial:int = int(valores[0])
    valorObjetivo:int = int(valores[1])

    movimientos:list[int] = listarMovimientos(valorInicial, valorObjetivo)
    
    resultado:str = '' #resultado termina siendo un str que contiene si se puede o no formar la cadena de numeros, la cantidad de movimientos, y los movimientos

    if movimientos == []: #si devolvi la lista de movimientos vacia es porque no podia formar una cadena de movimientos
        resultado = 'NO'
    else:
        resultado = 'YES\n'+str(len(movimientos))+'\n'

        for i in range(len(movimientos)-1,-1,-1): #voy desde el final de la lista hasta el valor en la pos 0
            n = str(movimientos[i])

            if n==str(movimientos[len(movimientos)-1]): #tengo que hacer esto para que no me agregue una identación al principio
                resultado = resultado + n 
            else:
                resultado += ' ' + n

    return resultado 

def listarMovimientos(valorInicial:int, valorObjetivo:int)->list[int]:
    movimientos = []
    valorActual = valorObjetivo #empiezo de atras para adelante, eso me va a devolver, si existe, 1 camino posible

    while valorActual > valorInicial: #Me interesa ver si el numero en el que estoy parado es mayor al valor inicial, si lo es, continuo con el while, dentro me fijo si el valor actual es par o si resulta de la multiplicacion por 10 más la suma de 1
        movimientos.append(valorActual) 

        if valorActual % 2 == 0: #si el valor es par significa que provino de hacer la multiplicacion por 2
            valorActual = int(valorActual//2) #comprobe que es par, asi que divido por 2 en division entera 
        elif (valorActual)%10 == 1: #Si divido por 10 y el resto es uno, entonces el numero pudo haber provenido de haber hecho n*10 + 1
            valorActual = int((valorActual-1)//10) #comprobe que podia restar 1 y dividir por 10
        else: #el valor en el que estoy parado no es par ni tampoco tiene un uno a la izq, por lo que no puedo formar el valorInicial
            movimientos = [] #no se puede formar la cadena de int que me lleva a mi resultado objetivos, por lo que ya se que la respuesta es no
            return movimientos
        
    if valorActual==valorInicial:
        movimientos.append(valorActual) #llegué al valor inicial
        return movimientos    

    return movimientos

if __name__ == "__main__":
    print(recibirInput())