'''
Binary Translator Project
The program asks the user what he wants to translate,
receives your response and asks for the data you would like to translate.
Finally by arithmetic and comparative operations,
shows what was requested in its respective translation.
'''


''' Function for processing from binary to decimal
     Inputs: binary variable string
     Outputs: decimal numeric variable
     Topics: Cycles, Arithmetic Calculations and Functions'''
def binary_to_decimal(binary):
    #Declaration of necessary variables
    power = 1
    decimal = 0
    binary = int(binary)
    #Repit process while binary is greater than
    while binary > 0:
        #We declare the remainder variable to obtain the remainder of num between 10
        remainder = binary % 10
        #Replace the value of binary
        binary = binary // 10
        #Add to the actual value of decimal the remider times the power
        decimal = decimal + remainder * power
        #Multiply the power by two
        power = power * 2
    conversion_to_ASCII(decimal)

''' Function to process from decimal to binary by calling an empty list and the entered value
     Inputs: String type variable modules / Character list, decimal numeric variable
     Outputs: Prints the already translated list/String
     Topics: Lists, Cycles, Mathematical calculations and Functions'''
def translate_to_binary(decimal):
    # We declare necessary variables/lists
    decimal=int(decimal)
    modules=[]
    #Repeat process while decimal is not 0
    while decimal != 0: 
        #We get the reminder of the decimal division by 2
        reminder = decimal % 2
        #We get the quotient of the same division
        quotient = decimal // 2
        #We add the value of the reminder to the list
        modules.append(reminder)
        #We assign the value of the quotient to decimal
        decimal = quotient 
    #In case of missing digits add "0" to complete the 8-digit string
    while len(modules) != 8:
        modules.append(0)
    #Reverse the order of the list
    inverted_modules = modules[::-1]
    for i in inverted_modules:
        #Print the value of i, which is respectively each character of the binary 
        print(i, end='')

    

''' Function for character division of a binary/string value
     Inputs: binaryStr variable string/List of characters
     Outputs: Print the function that is called
     Topics: Arrays, Lists, String, Loops, Nested Conditionals'''
def split_input(binaryStr):
    #We declare an empty list
    chunks = []
    #If the length of binaryStr is greater than or equal to 8 it will have to process the value
    if len(binaryStr) >= 8:
        binary = 0
        reminder = len(binaryStr) % 8
        #Add 0 in case they are missing to make it a multiple of 8
        if reminder != 0:
            auxiliar = ""
            size = len(binaryStr) + 8
            for i in range(8 - reminder):
                auxiliar += "0"
            auxiliar+=binaryStr
            binaryStr=auxiliar
        #We extract the bytes with the following for loops and store them in chunks, then call binary_to_decimal with the respective binary value
        for i in range(0,len(binaryStr),8):
            if i+8<len(binaryStr):
                chunks.append(binaryStr[i:i+8])
            else:
                chunks.append(binaryStr[i:len(binaryStr)])
        for i in range(len(chunks)):
            binary = chunks[i]
            binary_to_decimal(binary)
        print('')
    #Add zeros in case they are missing to complete the byte (8 digits)
    else:
        size = len(binaryStr)
        auxiliar = ""
        for i in range(8-size):
            auxiliar += "0"
        auxiliar += binaryStr
        split_input(auxiliar)

''' Function to validate the user's keyboard 
    Inputs: binaryStr variable string 
    Outputs: binaryStr or print error 
    Topics: Functions, Conditionals, nested and boolean loops'''
def validation(binaryStr):
    valid = False
    #If the validation is false, repeat until the user gives a binary value to be able to process it.
    while valid == False:
        for element in binaryStr:
            if element != '0' and element != "1":
                print("Por favor ingrese solo 0 o 1, tampoco aceptamos espacios")
                binaryStr = input("Ingrese el numero binario: ")
                valid = False
                break
            else:
                valid = True
    return binaryStr    

''' Function to convert the calculated decimal value to a respective character and form a string
     Inputs: decimal numeric variable
     Outputs: Print final character string
     Topics: Functions, Conditionals, Loops, Lists and File Connections'''
def conversion_to_ASCII(decimal):
    #Obtener los archivos necesarios
    file = open('decimal_List.txt', 'r+')
    file2 = open('ASCII_List.txt','r+')
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

''' Funcion para convertir el valor character obtenido a un respecitivo valor decimal
    inputs: character variable de character
    Salidas: llama a la funcion translate_to_binary con el valor de i respectivo a cada character
    Temas: Funciones, Condicionales, Ciclos anidados, Listas y Conexion de archivos'''
def conversion_to_binary(character):
    #Get necessary files
    file = open('decimal_List.txt','r')
    file2 = open('ASCII_List.txt','r')
    #Read the files and consider them as lists
    read2 = file2.read().splitlines()
    read = file.read().splitlines()
    final = []
    #With the use of nested loops, check if the value entered in that position of the entered string is equal to some value in the file
    for j in range(len(character)):
        for i in range(len(read2)):
            if character[j]==read2[i]:
                final.append(read[i])    
    #Call the function translate_to_binary with the respective value of i
    for i in final:
        translate_to_binary(i)
    print('')
    #Close files
    file.close()
    file2.close()
    
''' Function that handles the interaction with the user and program logic
     Topics: Functions, Loops and Conditionals '''
def main():
    #We start a loop to show the menu and select some function
    while True:
        #We call the function menu to show the options
        menu()
        #Data input
        entry = int(input())
        #If input is 1 continue
        if entry == 1:
            #Binary data input
            binaryStr = input("Enter the binary number: ")
            binario_valid = validation(binaryStr)
            print("Your text is: ")
            split_input(binario_valid)
        #If input is 2 continue
        elif entry == 2:
            #Numeric data entry
            txt = input("Enter a text:")
            #Print the question and the function call
            print("Su binario es: ")
            conversion_to_binary(txt) 
        #If input is 3 continue
        elif entry == 3:
            #Say Goodbye to the user and end the program
            print("Bye")
            break
        #Anything else continue
        else:
            #Print the text and end the program
            print("Enter a valid value next time.")
            break

'''Function menu'''
def menu():
    #Print the options
    print("Enter 1 if you want to translate binary code to Text/ASCII.")
    print("Enter 2 if you want to translate Text/ASCII to binary code. ")
    print("Enter 3 if you want to exit.")

'''Test function'''
def test():
    #Print the values of different translations and vice versa
    split_input("01101000011011110110110001100001001000000110110101110101011011100110010001101111")
    split_input("0110001101100001011011000110100101100110011010010110001101100001011000110110100101101111011011100010000000101011001100010011000000110000")
    split_input("0100110001101111011100100110010101101101001000000110100101110000011100110111010101101101")
    conversion_to_binary("hola mundo")
    conversion_to_binary("calificacion +100")
    conversion_to_binary("Lorem ipsum")

#test()
main()
