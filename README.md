# Context
All the information that is stored in a computer can be in ASCII or binary format, which are the two basic information encoding formats in a computer. The natural way, from the point of view of the machine, is to store the information in binary format; and the natural way for the user is to do it in ASCII format. Both systems use the byte as the minimum unit of information capable of storing 256 different values (usually numbers between 0 and 255). The ASCII format (American Standard Code for Information Interchange) is based on a coding system that assigns each alphanumeric character (A-Z, a-z, 0-9) or control character (carriage return, line feed, etc.) a value between 0 and 255. In this way, when storing a text we will use one byte per character plus some control bytes, the problem arises when storing numbers.

# How it Works
The program consists of asking the user if he is interested in translating ASCII to binary or vice versa, once the program receives a response depending on the selection obtained, the program will search within the functions and ask the user for the data he wishes to translate, a Once the value is obtained, the program will do arithmetic calculations and data comparison to be able to give the translated value. The program has verification methods, if you do not enter a valid value, it will show you an error and ask again.

# Installation
The program runs inside the terminal (Windows) or in interpreters like Visual Studio Code with Python 3.
- First you will have to download the zip available on GitHub.
- Then unzip the file
- Open the terminal and type Python Binary_Translator.py
- Once done, enjoy the program :D

# Algorithm
## Input:
- Integer data for selection in the menu
- Data in binary or text
## Process:
- Ask the user what data he wishes to enter to identify the type of data
- Separate the characters and by mathematical methods get the decimal value
- Compare each decimal value between lists/text files
- Obtain the respective translation of each character/string
- Reform the character string
- Show the set of characters in their respective translation
## Output:
- Data obtained by the program

##Note
You will need the txt files to use the program
