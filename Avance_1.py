def binario_a_decimal(num):
    potencia =1
    decimal= 0
    while num>0:
        binario = num % 10
        num = int(num / 10)
        decimal = decimal + binario * potencia
        potencia = potencia * 2
    return decimal
def decimal_a_binario():
    binario = input("Ingrese su texto:")
    print("Aqui se mostrara tu traduccion.")
def main():
    menu()
    entrada = int(input(":"))
    if entrada==1:
        num = int(input("Ingrese el numero binario: "))
        print("Su valor decimal es =", binario_a_decimal(num))
    elif entrada==2:
        decimal_a_binario()
    elif entrada==3:
        print("Adios")
    else:
        print("Ingrese un valor valido la proxima vez.")

def menu():
    print("Ingrese 1 si desea traducir codigo binario a decimal.")
    print("Ingrese 2 si desea traducir decimal a codigo binario. ")
    print("Ingrese 3 si quiere salir.")

main()
