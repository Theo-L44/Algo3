def recibirInput()-> list[int]:
    valores = input().split()
    valorInicial = int(valores[0])
    valorObjetivo = int(valores[1])

    movimientos = listarMovimientos(valorInicial, valorObjetivo)

    return movimientos

def listarMovimientos(valorInicial:int, valorObjetivo:int):
    movimientos = []
    valorActual = valorObjetivo

    while valorActual > valorInicial:

        if valorActual==valorInicial:
            movimientos.append(valorActual)
            


    return

if __name__ == "__main__":
    output = recibirInput()

    #for i in range(len()):
        
    #output = cantidadesDeCambios(strings)
    return output