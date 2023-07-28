# la funcion print() en python nos ayuda a visualizar los resultados de los programas
# en la consola

print("Hola Mundo") # muestra en la consola: Hola Mundo

# Se pueden imprimir numeros y letras
# las letras van entre comillas simples o dobles
# los numeros no requieren de comillas

print('Hola Mundo') # con comillas simples
print(50) # los numeros no requieren de comillas

# la funcion print() tiene dos argumentos muy interesantes: 'end' y 'sep'
# veamos el argumento 'end'

print("Hola Mundo", end="*") # Resultado: Hola Mundo*
# el argumento end añade al final del resultado en pantalla lo que lleguemos a indicar
# en el ejemplo, se indica que al final debe aparecer un * asterisco

# tambien se puede multiplicar las veces que querramos aquello que queremos que salga
# al final
print("Hola Mundo", end="#" * 5) # '* 5' indica una multiplicacion, es decir, cinco veces
# Resultado: Hola Mundo#####

# Sino se indica nada al argumento 'end' su valor por defecto sera: '\n' que significa
# 'new line', es como dar un 'enter', se genera una nueva linea
print()
print("hola\n" + "Mundo") # Resultado: 'hola' en una linea y 'Mundo' en otra linea

# Ahora veamos el argumento 'sep'
print("HolaMundo", "HolaMundo", "HolaMundo", sep="#")
# Resultado: HolaMundo#HolaMundo#HolaMundo
# El argumento 'sep' nos permite indicar con que seperar las cosas que se van a imprimir en consola
