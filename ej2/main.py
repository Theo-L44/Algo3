def recibirInput()-> list[int]:
    valores = input().split()
    valorInicial = int(valores[0])
    valorObjetivo = int(valores[1])

    movimientos = listarMovimientos(valorInicial, valorObjetivo)
    
    resultado:str = '' #resultado termina siendo un str que contiene si se puede o no formar la cadena de numeros, la cantidad de movimientos, y los movimientos

    if movimientos == []: #si devolvi la lista de movimientos vacia es porque no podia formar una cadena de movimientos
        resultado = 'NO'
    else:
        resultado = 'YES\n'+str(len(movimientos))+'\n'

        for i in range(len(movimientos)-1,-1,-1): #voy desde el final de la lista hasta el valor en la pos 0
            n = str(movimientos[i]) #movimiento actual
            resultado = resultado+' '+n

    return resultado 

def listarMovimientos(valorInicial:int, valorObjetivo:int):
    movimientos = [valorObjetivo]
    valorActual = valorObjetivo

    while valorActual >= valorInicial: #Me interesa ver si el numero en el que estoy parado es mayor al valor inicial, si lo es, continuo con el while, dentro del while me fijo si el valor es par, si resulta de la multiplicacion por 10 más la suma de 1 o si es exactamente el numero inicial.

        if valorActual==valorInicial:
            movimientos.append(valorActual) #llegué al valor inicial
            valorActual-1 #de esta manera me queda un valor menor al inicial y salgo del bucle
            return movimientos
        elif valorActual % 2 == 0: #si el valor es par significa que provino de hacer la multiplicacion por 2
            valorActual = valorActual/2
            movimientos.append(valorActual)
            return movimientos
        elif (valorActual-1)%10 == 0 and (valorActual-1)/10 >= valorInicial: # Si al valor le resto 1 y es divisible por 10 es probable que haya venido de haberle puesto un uno a la izq, por lo que hago la operacion contraria #aca creo que me falta una clausula para que quede bien definido
            valorActual = (valorActual-1)/10 
            movimientos.append(valorActual)
            return movimientos
        else: #el valor en el que estoy parado no es par ni tampoco tiene un uno a la izq, por lo que no puedo formar el valorInicial
            movimientos = [] #no se puede formar la cadena de int que me lleva a mi resultado objetivos, por lo que ya se que la respuesta es no
            valorActual = valorInicial-1
            return movimientos
            
    return movimientos

if __name__ == "__main__":
    output = recibirInput()
    print(output)