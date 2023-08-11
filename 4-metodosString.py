# METODOS DE LOS STRINGS

# A continuación, veamos algunos ejemplos de metodos de strings en python
# Ref.: https://controlautomaticoeducacion.com/python-desde-cero/metodos-string-en-python/

frase = "Hola Mundo"

# ANALIZAR STRINGS
# len() Retorna el tamaño de la cadena de caracteres
# count() Retorna el numero de veces que se repite un caracter en la cadena
# find() Busca n substring o caracter dentro de la cadena de caracteres

len(frase)   #Retorna 10
frase.count('o')   #Retorna 2
frase.count('o',0,8)   #Retorna 1 (numero de 'o' desde el cero hasta el 8)
frase.find('Mun')   #Busca el substring 'Mun' retorna 5 - Desde la 
# posicion 5 en adelante se encuentra la frase buscada

# PARTICIONAR LOS STRINGS
# los strings son cadenas de texto y podemos acceder a cada 'pedazo' o 'parte' de esa cadena
print(frase[5]) # Resultado: M
frase[0:5] #Retorna el slice: 'Hola '
frase[0:10:2] #Retorna el slice: 'Hl ud'
frase[:5] #Retorna el slice: 'Hola '
frase[6:] #Retorna el slice: 'Mundo'
frase[6::3] #Retorna el slice: 'uo'

# TRANSFORMAR STRING EN PYTHON
# upper() Coloca todo el string en mayusculas
# lower() Coloca todo el string en minusculas
# capialize() Coloca la primera letra en mayusculas
# title() Coloca la primera letra de cada palabra en mayusculas
# replace(str1,str2) Reemplaza un substring por otro
# strip() Elimina los espacios innecesarios al inicio y fin del string
# rstrip() Elimina los espacios innecesarios al fin del string
# lstrip() Elimina los espacios innecesarios al inicio del string

frase.upper() # HOLA MUNDO
frase.lower()  # hola mundo
frase.capitalize() # Hola mundo
frase.title()  # Hola Mundo
frase.replace('Mundo','Que Tal')  # Hola Que Tal

# DIVIDIR CARACTERES
frase.split() # ['Hola','Mundo']
'-'.join(frase) # 'H-o-l-a- -M-u-n-d-o'