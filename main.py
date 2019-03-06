"""
@author Jairo Andres

"""


from NodonoTerminal import NodonoTerminal
from NodoTerminal import NodoTerminal
#import pdb
# pdb.set_trace()

nodosTerminales = []
nodosNoterminales = []
contadornuevoNoTerminal = 0
variableInicial = None
palabraProduccion = ""




def solicitarDato():
    global variableInicial
    entradaTerminales = input(
        "ingresa las variables terminales separadas por comas (ejm 1,2,3): ")
    entradaNoTerminales = input(
        "ingresa las variables no terminales separadas por comas (ejm A,B,C): ")
    variableTerminales = entradaTerminales.split(',')
    variablenoTerminales = entradaNoTerminales.split(',')

    apilarNodosnoTerminales(variablenoTerminales)
    apilarNodosTerminales(variableTerminales)

    for nodonoterminal in nodosNoterminales:
        pedidoReglas = True
        while(pedidoReglas):
            try:

                cantidadReglas = int(
                    input("ingresa la cantidad de reglas de  " + nodonoterminal.nombre+" : "))
                pedidoReglas = False
            except ValueError:
                print("La cantidad de Reglas para la variable " +
                      nodonoterminal.nombre+" debe ser numerica2")

        # solicitar reglas
        print("Recuerde digitar las reglas tal y como las escribio al inicio ejm A=>B es diferente A=>b")
        while(cantidadReglas > 0):
            reglasTexto = input(nodonoterminal.nombre+"=> ")
            reglas = []
            for reglatexto in reglasTexto:
                reglas.append(buscarInstanciaNodo(reglatexto))
            cantidadReglas = cantidadReglas-1

            nodonoterminal.reglas.append(reglas)
    while(True):
        inicialTexto = input(
            "Digite la variable inicial de la gramatica (debe estar dentro de las variables no terminales): ")
        variableInicial = buscarInstanciaNodo(inicialTexto)
        if variableInicial is None:
            continue

        break

        # ya se tendria las reglas referenciadas por instancias

    formaNormalChomsky()


def formaNormalChomsky():
    tamanionoTerminales = len(nodosNoterminales)
    generarReglaTerminal()

    for posicion in range(0, tamanionoTerminales):
        print(posicion)
        reglas = nodosNoterminales[posicion].reglas
        for regla in reglas:

            formalizaRegla(regla, nodosNoterminales[posicion])

    # imprimirResultadoFormalizacion()


def imprimirResultadoFormalizacion():
    for noterminal in nodosNoterminales:
        print(noterminal)
# Formalizacion continua de las relgas


def formalizaRegla(regla, nodoNoTerminal):
    global contadornuevoNoTerminal
    salida = True

    while(salida):
        if len(regla) <= 2:
            reglas = []
            if not isinstance(regla[0], NodonoTerminal):
                reglas.append(buscadorGeneradorTerminal(regla[0]))
            else:
                reglas.append(regla[0])

            if len(regla) == 2:
                if not isinstance(regla[1], NodonoTerminal):
                    reglas.append(buscadorGeneradorTerminal(regla[1]))
                else:
                    reglas.append(regla[1])

            nodoNoTerminal.reglasPrima.append(reglas)

            salida = False
        else:

            nodo = regla.pop(0)
            nuevoNoTerminal = NodonoTerminal("X"+str(contadornuevoNoTerminal))
            contadornuevoNoTerminal += 1
            nuevoNoTerminal.reglas.append(regla)
            nodosNoterminales.append(nuevoNoTerminal)
            reglaprima = []
            if isinstance(nodo, NodonoTerminal):
                reglaprima = [nodo, nuevoNoTerminal]
            else:
                reglaprima = [buscadorGeneradorTerminal(nodo), nuevoNoTerminal]

            nodoNoTerminal.reglasPrima.append(reglaprima)

            regla = nuevoNoTerminal.reglas[0]
            nodoNoTerminal = nuevoNoTerminal


def buscadorGeneradorTerminal(terminalabuscar):
    for noterminal in nodosNoterminales:
        if len(noterminal.reglasPrima) == 1:
            reglaPrima = noterminal.reglasPrima[0]

            if isinstance(reglaPrima[0], NodoTerminal):
                if reglaPrima[0].valor == terminalabuscar.valor:
                    return noterminal


def generarReglaTerminal():
    global contadornuevoNoTerminal

    for nodoTerminal in nodosTerminales:

        reglas = []
        nuevonoTerminal = NodonoTerminal("X"+str(contadornuevoNoTerminal))
        contadornuevoNoTerminal += 1
        reglas.append(nodoTerminal)
        nuevonoTerminal.reglasPrima.append(reglas)
        nodosNoterminales.append(nuevonoTerminal)


def buscarInstanciaNodo(valor):
    for nodoTerminal in nodosTerminales:
        if nodoTerminal.valor == valor:
            return nodoTerminal
    for nodoNoTerminal in nodosNoterminales:
        if nodoNoTerminal.nombre == valor:
            return nodoNoTerminal


def apilarNodosnoTerminales(variablenoTerminales):
    for noterminal in variablenoTerminales:
        nodonoterminal = NodonoTerminal(noterminal)
        nodosNoterminales.append(nodonoterminal)


def apilarNodosTerminales(variableTerminales):
    for terminal in variableTerminales:
        nodoterminal = NodoTerminal(terminal)
        nodosTerminales.append(nodoterminal)


def imprimirdatos():
    print("Reglas Generadas : ")
    for noterminal in nodosNoterminales:

        print(noterminal.nombre+"=> " + str(noterminal.reglasPrima))


def generarLenguaje():
    global palabraProduccion
    global variableInicial
    while(True):
        try:

            cantidadPalabra = int(
                input("Digite la cantidad de palabras que desea generar "))
            break
        except ValueError:
            continue

    contadorPalabra = 0
    print("Producciones Generadas")
    print("_______________________")
    while(cantidadPalabra > contadorPalabra):
        palabraProduccion = ""

        recorrerinOrden(variableInicial)
        print (palabraProduccion)
        contadorPalabra = contadorPalabra+1


def recorrerinOrden(nodo):
    global palabraProduccion

    if isinstance(nodo, NodonoTerminal) and nodo is not None:
        nodo.escogerCaminoAZar()
        recorrerinOrden(nodo.getIzquierdo())
        recorrerinOrden(nodo.getDerecho())
    if isinstance(nodo, NodoTerminal):
        palabraProduccion += nodo.valor


solicitarDato()
imprimirdatos()
generarLenguaje()
