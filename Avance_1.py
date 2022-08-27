def binario_a_texto():
    binario = int(input("Ingrese su codigo binario:"))
    print("Aqui se mostrara tu traduccion.")
def texto_a_binario():
    binario = input("Ingrese su texto:")
    print("Aqui se mostrara tu traduccion.")
def main():
    menu()
    entrada = int(input(":"))
    if entrada==1:
        binario_a_texto()
    elif entrada==2:
        texto_a_binario()
    elif entrada==3:
        print("Adios")
    else:
        print("Ingrese un valor valido la proxima vez.")

def menu():
    print("Ingrese 1 si desea traducir codigo binario a texto.")
    print("Ingrese 2 si desea traducir texto a codigo binario. ")
    print("Ingrese 3 si quiere salir.")

main()