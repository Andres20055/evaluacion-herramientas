# evaluacion-herramientas

### integrantes del grupo: Andrés Felipe Vélez Gálvez usuario: Andres20055

# Explicación del codigo

## Primera función

En la primera funcion se utilizan diferentes variables como el caracter y el byte, en el caracter se utiliza un input para preguntarle al usuario que caracter quiere verlo como un byte utilizando la funcion ord() esto para revisar a que equivale el caracter preguntado como un byte y en la parte del print muestra en la consola la representación en bytes del carácter ingresado, precedida por un mensaje que indica qué se está mostrando. La representación binaria se muestra sin los primeros dos caracteres **('0b')**, y se asegura de que tenga al menos 8 caracteres, rellenando con ceros a la izquierda si es necesario; las funciones q se utilizan en el print algunas son bin(byte): Toma el valor numérico del carácter (que se convirtió en un número entero usando ord(caracter)) y luego lo convierte en su representación binaria como una cadena. Por ejemplo, bin(97) resultaría en '0b1100001' y tambien [2:]: Selecciona todos los caracteres de la cadena binaria, excepto los primeros dos. En la representación binaria generada por bin(), los primeros dos caracteres son '0b'

## Segunda función

En la segunda función es basicamente lo mismo que la primera función solo que se agrega un **for in** para crear un ciclo, este ciclo lo que va hacer sera revisar cuanto equivale cada caracter de la palabra en binario

## Tercera función

Aquí unicamente se realizó el menu donde el usuario podrá interactuar para digitar ya sea solo un caracter o una palabra, lo unico nuevo que se utilizo fueron los if y elif para restringir los digitos que no se pueden usar por ejemplo si el usuario digita *1* entonces solo podra digitar un caracter para que el programa se lo de en binario el *2* es para que el  programa revise la palabra en binario y el *0* para salirse del programa

# Explicación repositorio


### Creación del repositorio

Primeramente se creo el repositorio en donde se tuvo que crearlo de manera publica y a parte agregar el archivo **gitignore** los archivos que no acepta este archivo son los que contengan algún archivo del lenguaje *C++*; tambien se logro agregar el archivo README.md

### Agregar el codigo de python

Posteriormente se crea una nueva rama para agregar el archivo de python para despues hacer el pull request de la rama principal **main**

### Explicacion de pasos

Por ultimo se explican los pasos del desarrollo de codigo de **python** y del desarrollo del repositorio utilizando en ambas explicaciones formato de lenguaje Markdown

