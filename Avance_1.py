#Funcion para convertir de binario a decimal
def binario_a_decimal(num):
    #Declaracion de variables que se van a ocupar en el proceso matematico
    potencia =1
    decimal= 0
    #Repetir hasta que el valor de la variable num sea 0 o menor
    while num>0:
        #Obtencion del modulo de variable num entre 10 guardada en una nueva variable
        binario = num % 10
        #Nuevo valor a num dividiendo num entre 10
        num = int(num / 10)
        #Suma del valor actual decimal al binario multiplicado por la respectiva potencia
        decimal = decimal + binario * potencia
        #Obtencion de la potencia susesiva para obtrener los valores de cada digito binario
        potencia = potencia * 2
    #Obtener el valor decimal final y mostrarlo
    return decimal

#Futura funcion decimal a binario
def decimal_a_binario():
    binario = input("Ingrese número:")
    print("Aqui se mostrara tu traduccion.")

#Funcion main
def main():
    #Dar un valor temporal a entrada para usar elwhile
    entrada = ""
    #Repetir mientras entrada no sea igual a 3
    while entrada!=3:
        #LLamar funcion menu
        menu()
        #Requerir nuevo valor de entrada al usuario
        entrada = int(input(":"))
        #Condicionales para que al usuario se le muestre lo que relativamente selecciono
        if entrada==1:
            #Entrada del valor num
            num = int(input("Ingrese el numero binario: "))
            #Imprimir el llamado de la funcion binario a decimal
            print("Su valor decimal es =", binario_a_decimal(num))
        elif entrada==2:
            #LLamar funcion decimal a binario(out of service)
            decimal_a_binario()
        elif entrada==3:
            #Finalizar programa a solicitud del usuario
            print("Adios")
        else:
            #Finalizar programa por que el usuario no sabe leer :D
            print("Ingrese un valor valido la proxima vez.")
            break
#Funcion menu
def menu():
    #Impresion de opciones disponibles para el usuario
    print("Ingrese 1 si desea traducir codigo binario a decimal.")
    print("Ingrese 2 si desea traducir decimal a codigo binario. ")
    print("Ingrese 3 si quiere salir.")

#Funcion de pruebas :D
def pruebas():
    binario_a_decimal(110)
        #El resultado tendria que ser 6
    

#pruebas()
main()
