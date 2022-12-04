# Contexto
Toda la información que se almacena en un ordenador puede encontrarse en formato ASCII o binario, que son los dos formatos básicos de codificación de información en un ordenador. La forma natural, desde el punto de vista de la máquina, es almacenar la información en formato binario; y la forma natural para el usuario es hacerlo en formato ASCII. Ambos sistemas utilizan el byte como unidad mínima de información capaz de almacenar 256 valores diferentes (normalmente números entre 0 y 255). El formato ASCII (American Standard Code for Information Interchange) se basa en un sistema de codificación que asigna a cada carácter alfanumérico (A-Z, a-z, 0-9) o de control (retorno de carro, paso de línea, etc.) un valor entre 0 y 255. De este modo al almacenar un texto utilizaremos un byte por carácter más algunos bytes de control, el problema surge a la hora de almacenar números.

# Como funciona
El programa consta en preguntar al usuario si este interesado en traducir ASCII a binario o viceversa, una vez recibiendo una respuesta el programa dependiendo de la selección obtenida, el programa buscara dentro de las funciones y preguntará al usuario por el dato que desea traducir, una vez obtenido el valor el programa hará cálculos aritméticos y comparación de datos para poder dar el valor traducido. El programa cuenta con métodos de verificación, en caso de no introducir un valor valido te mostrara un error y preguntara nuevamente.

# Instalación
El programa corre dentro de la terminal (Windows) o en interpretadores como Visual Studio Code con Python 3.
- Primero tendrás que descargar el zip disponible en GitHub.
- Después descomprime el archivo
- Abrir la terminal y teclear Python Avance_1.py
- Una vez hecho esta disfruta el programa :D

# Algoritmo
## Entrada:
- Dato entero para selección en el menú
- Datos en binario o en texto
## Proceso:
- Preguntar al usuario que dato desea ingresar para identificar el tipo de dato
- Separar los caracteres y por métodos matemáticos conseguir el valor decimal
- Comparar cada valor decimal entre las listas/archivos de texto
- Obtener la respectiva traducción de cada carácter/cadena
- Formar nuevamente la cadena de caracteres
- Mostrar el conjunto de caracteres en su respectiva traducción
## Salida:
- Datos obtenidos por el programa

