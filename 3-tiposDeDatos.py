# TIPOS DE DATOS EN PYTHON

# python trabaja con diferentes tipos de datos, veamos los mas conocidos

# int - integer - enteros
# corresponde a todos los numeros enteros
type(45) 
# Resultado: <class 'int'>

# Floats - flotantes - decimales
type(3.1416)
# Resultado: <class 'float'>

# str - string - cadenas de texto - texto
type("Hola Mundo")
# Resultado: <class 'str'>

# tuple - tuplas - lista que no se puede modificar - van entre parentesis
type((1,2,3,4,5))
# Resultado: <class 'tuple'>

# list - listas - coleccion de elementos - van entre corchetes
type([1,2,3,4,5])
# Resultado: <class 'list'>

# dict - diccionarios - coleccion de elementos: clave, valor - van entre llaves
type(
        {
        'nombre':'John',
        'apellido':'Kennedy',
        'dni':'58976542-abc'
        }
    )
# Resultado: <class 'dict'>