''' Funcion para el proceso de binafrio a decimal
    Entradas:
    Salidas:
    Temas: '''
def binario_a_decimal(binario):
    #Declaracion de variables necesarias
    potencia =1
    decimal= 0
    binario = int(binario)
    #Repetir proceso mientras binario mayor que0
    while binario>0:
        #Declaramos la variable residuo para obtener el residuo de num entre 10
        residuo = binario % 10
        #Le damos el nuevo valor a num
        binario = binario // 10
        #Agregamos a la variable decimal el residuo multiplicando a la potencia
        decimal = decimal + residuo * potencia
        #Multiplicamos la potencia por 2
        potencia = potencia * 2
    return decimal

''' Funcion para el proceso de decimal a binario llamando una lista vacia y el valor ingresado
    Entradas:
    Salidas:
    Temas: '''
def traduccion_a_binario(modulos,decimal):
    #Repetir proceso mientras decimal no sea 0
    while decimal != 0: 
        #Obtenemos el residuo de la division decim al entre 2
        residuo = decimal%2
        #Obtenemos el cociente de la misma division
        cociente = decimal//2
        #Agregamos el valor del residuo a la lista
        modulos.append(residuo)
        #Le asignamos el valor del cociente a decimal
        decimal = cociente 
    #Invertimos el orden de la lista
    modulos_invertidos=modulos[::-1]

    #Para la variable i en modulos invertidos repetir
    for i in modulos_invertidos:
        #Imprimir el valor de i, el cual es respectivamente cada caracter del binario 
        print(i, end = '')
    print()


def dividir_entrada(binarioStr):
    chunks = []
    if len(binarioStr)>=8:
        binario = 0
        residuo=len(binarioStr)%8
        if residuo != 0:
            auxiliar=""
            tamaño=len(binarioStr)+8
            for i in range(8-residuo):
                auxiliar+="0"
            auxiliar+=binarioStr
            binarioStr=auxiliar
            print(auxiliar)
        for i in range(0,len(binarioStr),8):
            if i+8<len(binarioStr):
                chunks.append(binarioStr[i:i+8])
            else:
                chunks.append(binarioStr[i:len(binarioStr)])
        for i in range(len(chunks)):
            binario = chunks[i]
            print(binario_a_decimal(binario))
    else:
        tamaño=len(binarioStr)
        auxiliar=""
        for i in range(8-tamaño):
            auxiliar+="0"
        auxiliar+=binarioStr
        dividir_entrada(auxiliar)






def validacion(binarioStr):
    valido = False
    while valido==False:
        for elemento in binarioStr:
            if elemento!='0' and elemento!="1":
                print("Por favor ingrese solo 0 o 1, tampoco aceptamos espacios")
                binarioStr = input("Ingrese el numero binario: ")
                valido = False
                break
            else:
                valido = True
    return binarioStr    


''' Declaramos funcion main en la cual vamos a llamar las distintas funciones del programa
    Entradas:
    Salidas:
    Temas: '''
def main():
    #Iniciamos un bucle para mostrar el menu y seleccionar alguna funcion
    while True:
        #Llamamos a la funcion menu para que muestre las opciones
        menu()
        #Entrada de datos
        entrada = int(input())
        #Si entrada vale 1 continuar
        if entrada==1:
            #Entrada del dato binario
            binarioStr = input("Ingrese el numero binario: ")
            #binario_valido=validacion(binarioStr)
            #dividir_entrada(binario_valido)
            dividir_entrada(binarioStr)
        #Si entrada vale 2 continuar
        elif entrada==2:
            #Entrada de dato numerico
            decimal = int(input("Ingrese número entero:"))
            #Declaracion de lista
            modulos=[]
            #Imprimir la pregunta y el llamado de la funcion
            print("Su binario es: ")
            traduccion_a_binario(modulos,decimal) 
        #Si entrada vale 3 continuar
        elif entrada==3:
            #Despedir al usuario y terminar con el programa
            print("Adios")
            break
        #Cualquier otra cosa continuar
        else:
            #Imprimir el texto y terminar el programa
            print("Ingrese un valor valido la proxima vez.")
            break
#Funcion menu
def menu():
    #Imprimir las opciones
    print("Ingrese 1 si desea traducir codigo binario a decimal.")
    print("Ingrese 2 si desea traducir decimal a codigo binario. ")
    print("Ingrese 3 si quiere salir.")

#Funcion de pruebas
def pruebas():
    #Imprimir los valores de distintas traducciones y viceversa 
    print(binario_a_decimal(110))
    print(binario_a_decimal(111))
    print(binario_a_decimal(1110))
    traduccion_a_binario([],6)
    traduccion_a_binario([],7)
    traduccion_a_binario([],14)
    

#pruebas()
main()
