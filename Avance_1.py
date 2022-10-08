#Funcion para el proceso de binafrio a decimal
def binario_a_decimal(binario):
    #Declaracion de variables necesarias
    potencia =1
    decimal= 0
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

#Funcion para el proceso de decimal a binario llamando una lista vacia y el valor ingresado
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


#Declaramos funcion main en la cual vamos a llamar las distintas funciones del programa
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
            binario = int(input("Ingrese el numero binario: "))
            #Imprimir el llamado de la funcion
            print("El decimal resultante es: \n",binario_a_decimal(binario))
        #Si entrada vale 2 continuar
        elif entrada==2:
            #Entrada de dato numerico
            decimal = int(input("Ingrese número:"))
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
