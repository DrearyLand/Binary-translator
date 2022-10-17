'''
Proyecto Traductor de Binario
El programa pregunta al usuario por que quiere traducir,
recibe su respuesta y le pide el dato que quisiera traducir.
Finalmente por operaciones aritmeticas y comparativas, 
muestra lo solicitado en su respectiva traduccion.
'''


''' Funcion para el proceso de binario a decimal
    Entradas: binario variable string
    Salidas: decimal variable numerica
    Temas: Ciclos, Calculos Aritmeticos y Funciones'''
def binario_a_decimal(binario):
    #Declaracion de variables necesarias
    potencia =1
    decimal= 0
    binario=int(binario)
    #Repetir proceso mientras binario mayor que
    while binario>0:
        #Declaramos la variable residuo para obtener el residuo de num entre 10
        residuo = binario % 10
        #Le damos el nuevo valor a num
        binario = binario // 10
        #Agregamos a la variable decimal el residuo multiplicando a la potencia
        decimal = decimal + residuo * potencia
        #Multiplicamos la potencia por 2
        potencia = potencia * 2
    conversion_a_texto(decimal)
    # conversion_a_binario(decimal_lista)


''' Funcion para el proceso de decimal a binario llamando una lista vacia y el valor ingresado
    Entradas: modulos variable tipo String/Lista de caracteres, decimal variable numerica
    Salidas: Imprime la lista/String ya traducida 
    Temas: Listas, Ciclos, Calculos matematicos y Funciones'''
def traduccion_a_binario(decimal):
    #Declaramos variables/listas necesarias
    decimal=int(decimal)
    modulos=[]
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
    #En caso de faltar digitos agregar "0" para completar la cadena de 8 digitos
    while len(modulos)!=8:
        modulos.append(0)
    #Invertimos el orden de la lista
    modulos_invertidos=modulos[::-1]
    for i in modulos_invertidos:
        #Imprimir el valor de i, el cual es respectivamente cada caracter del binario 
        print(i, end='')

    

''' Funcion para la division de caracteres de un valor binario/string
    Entradas: binarioStr variable string/Lista de caracteres
    Salidas: Imprimir la fucion que se llama
    Temas: Matrices, Listas, Cadena de caracteres, Ciclos, Condicionales anidados'''
def dividir_entrada(binarioStr):
    #Declaramos lista
    chunks = []
    #Si la longitud de binarioStr es mayor o igual a 8 tendra que procesar el valor
    if len(binarioStr)>=8:
        binario = 0
        residuo=len(binarioStr)%8
        #Agregar 0 en caso de que falten para que sea multiplo de 8
        if residuo != 0:
            auxiliar=""
            tamaño=len(binarioStr)+8
            for i in range(8-residuo):
                auxiliar+="0"
            auxiliar+=binarioStr
            binarioStr=auxiliar
        #Extraemos los bytes con los siguentes ciclos for y los almacenamos en chunks, luego llamamos a binario_a_decimal con el respectivo valor binario
        for i in range(0,len(binarioStr),8):
            if i+8<len(binarioStr):
                chunks.append(binarioStr[i:i+8])
            else:
                chunks.append(binarioStr[i:len(binarioStr)])
        for i in range(len(chunks)):
            binario = chunks[i]
            binario_a_decimal(binario)
        print('')
    #Agregar ceros en caso de que falten para completar el byte(8 digitos)
    else:
        tamaño=len(binarioStr)
        auxiliar=""
        for i in range(8-tamaño):
            auxiliar+="0"
        auxiliar+=binarioStr
        dividir_entrada(auxiliar)

''' Funcion para validar el tecleo del usuario
    Entradas:binarioStr variable string
    Salidas: binarioStr o impresion de error
    Temas: Funciones, Condicionales, Ciclos anidados y boleanos'''
def validacion(binarioStr):
    valido = False
    #Si la validacion es falasa repetir hasta que el usuario de un valor binario para poder procesarlo
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

''' Funcion para convertir el valor decimal calculado a un respectivo caracter y formar una cadena
    Entradas: decimal variable numerica
    Salidas: Imprime cadena de caracteres final
    Temas: Funciones, Condicionales, Ciclos, Listas y Conexion de archivos'''
def conversion_a_texto(decimal):
    #Obtener los archivos necesarios
    file = open('listadecimal.txt', 'r+')
    file2 = open('listaascii.txt','r+')
    #Leer los archivos y considerarlos como listas
    read2=file2.read().splitlines()
    read = file.read().splitlines()
    final = []
    #Si el valor decimal coincide con algun punto de la lista, agregar su respectiva traduccion
    if str(decimal)==read[decimal-32]:
        final.append(read2[decimal-32])
    #Imprimir la lista donde guardamos cada decimal traducido
    for i in final:
        print(i, end='')
    #Cerrar archivos
    file.close()
    file2.close()

''' Funcion para convertir el valor caracter obtenido a un respecitivo valor decimal
    Entradas: caracter variable de caracter
    Salidas: llama a la funcion traduccion_a_binario con el valor de i respectivo a cada caracter
    Temas: Funciones, Condicionales, Ciclos anidados, Listas y Conexion de archivos'''
def conversion_a_binario(caracter):
    #Obtener archivos necesarios
    file = open('listadecimal.txt','r')
    file2 = open('listaascii.txt','r')
    #Leer los archivos y considerarlos como listas
    read2=file2.read().splitlines()
    read = file.read().splitlines()
    final = []
    #Con el uso ciclos anidados verificar si el valor ingresado en tal posicion de la cadena ingresada es igual a algun valor del archivo
    for j in range(len(caracter)):
        for i in range(len(read2)):
            if caracter[j]==read2[i]:
                final.append(read[i])    
    #LLamar a la funcion traduccion_a_binario con el respectivo valor de i
    for i in final:
        traduccion_a_binario(i)
    print('')
    #Cerrar archivos
    file.close()
    file2.close()
    
''' Funcion que lleva la interaccion con el usuario y logica del programa
    Temas: Funciones, Ciclos y condicionales '''
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
            binario_valido=validacion(binarioStr)
            print("Su texto es: ")
            dividir_entrada(binario_valido)
        #Si entrada vale 2 continuar
        elif entrada==2:
            #Entrada de dato numerico
            txt = input("Ingrese un texto:")
            #Imprimir la pregunta y el llamado de la funcion
            print("Su binario es: ")
            conversion_a_binario(txt) 
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

'''Funcion menu'''
def menu():
    #Imprimir las opciones
    print("Ingrese 1 si desea traducir codigo binario a Texto/Ascii.")
    print("Ingrese 2 si desea traducir Texto/Ascii a codigo binario. ")
    print("Ingrese 3 si quiere salir.")

'''Funcion de pruebas'''
def pruebas():
    #Imprimir los valores de distintas traducciones y viceversa 
    dividir_entrada("01101000011011110110110001100001001000000110110101110101011011100110010001101111")
    dividir_entrada("0110001101100001011011000110100101100110011010010110001101100001011000110110100101101111011011100010000000101011001100010011000000110000")
    dividir_entrada("0100110001101111011100100110010101101101001000000110100101110000011100110111010101101101")
    conversion_a_binario("hola mundo")
    conversion_a_binario("calificacion +100")
    conversion_a_binario("Lorem ipsum")

#pruebas()
main()
