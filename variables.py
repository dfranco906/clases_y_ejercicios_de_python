# las variables son espacios en memoria en la que podemos guardar datos
# son como cajas donde podemos meter cosas
# en python las variables se crean poniendo el nombre de la misma
# seguida de un signo igual que '=' y seguido del valor que contendra esa variable

nombre = "John"

# el lenguaje python es key sensitive, es decir, distingue entre mayusculas y minusculas

Nombre = "Perla"

# para los humanos, conceptualmente ambas variables cumplen lo mismo
# pero para python son distintas

# Algunas reglas para las variables
# No pueden comenzar con numeros
# 1nombre= 12 # marca error
# no pueden contener espacios en el nombre
# nombre y apellido = "Perla Torres" # marca error
# se pueden usar guiones bajos para evitar los espacios
nombre_apellido = "Perla Torres"

# para nombrar las variables, se recomienda seguir una de las tres nomenclaturas:
# Pascal Case, Snake Case, Camel Case

# Pascal Case: la primera letra de cada palabra en mayusculas, se utilizan mas en funciones
NombreApellido = "Perla Torres"

# Snake Case: las palabras van separadas por guines bajos
nombre_apellido = "Perla Torres"

# Camel Case: la primera palabra en minusculas y las siguientes comienzan con mayusculas
nombreApellido = "Perla Torres"

# contenido de las variables
# las variables pueden contener todos los tipos de datos antes vistos

# Strings
cadena = "textoRandom"

# Integers
numero = 50

# Floats
decimal = 3.1416

# Tuplas
tuplaDeNumeros = (1,2,3,4,5,6,7,8,9)

# Listas
frutas = ['pera','manzana','pomelo','naranjas','limones']
paises = ['Paraguay','Argentina','Bolivia','Brasil']
numeros = [1,2,3,4,5,6,7,8,9]

# Diccionarios
estudiantes = {
    'nombre':'Pedro',
    'apellido':'Caceres',
    'edad':15
}