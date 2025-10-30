def recibirInput():
    n:int = (input().strip()) 
    return True

def resolver():
    return True

if __name__ == "__main__":
    respuesta = recibirInput()
    print(respuesta)

""" #pruebo hacerlo con backtracking
def recibirInput()->str:
    valores = input().split() #me va a devolver ['valor1', 'valor2'] donde valor 1 es desde donde empiezo, y valor 2 es donde yo quiero terminar
    valorInicial:int = int(valores[0])
    valorObjetivo:int = int(valores[1])

    movimientos:int = listarMovimientos(valorInicial, valorObjetivo)
     #resultado termina siendo un str que contiene si se puede o no formar la cadena de numeros, la cantidad de movimientos, y los movimientos

    return movimientos 

def listarMovimientos(valorInicial:int, valorObjetivo:int)->list[int]:
    movimientos = []
    valorActual = valorObjetivo #empiezo de atras para adelante, eso me va a devolver, si existe, 1 camino posible

    while valorActual > valorInicial: #Me interesa ver si el numero en el que estoy parado es mayor al valor inicial, si lo es, continuo con el while, dentro me fijo si el valor actual es par o si resulta de la multiplicacion por 10 más la suma de 1
        movimientos.append(valorActual) 

        if valorActual % 2 == 0: #si el valor es par significa que provino de hacer la multiplicacion por 2
            valorActual = int(valorActual//2) #comprobe que es par, asi que divido por 2 en division entera 
        elif valorActual+1 >= 0: #Si divido por 10 y el resto es uno, entonces el numero pudo haber provenido de haber hecho n*10 + 1
            valorActual = int(valorActual+1) #comprobe que podia restar 1 y dividir por 10
        else: #el valor en el que estoy parado no es par ni tampoco tiene un uno a la izq, por lo que no puedo formar el valorInicial
            movimientos = [] #no se puede formar la cadena de int que me lleva a mi resultado objetivos, por lo que ya se que la respuesta es no
            return len(movimientos)
        
    if valorActual==valorInicial:
        return 0
    
    return 0

if __name__ == "__main__":
    print(recibirInput()) """