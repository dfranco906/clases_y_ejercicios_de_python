# TUPLAS EN PYTHON
# es un tipo de estructura de datos que nos permite guardar una coleccion
# de elementos que no se pueden modificar durante la ejecucion del programa
# se utilizan parentesis y comas para separar los elementos dentro de ella

tupla = 1,2,3 # se pueden declarar sin () pero deben tener las comas
tupla2 = (1,2,3) 

# cada elemento de la tupla tiene una posicion, a esta posicion se le conoce
# como indice. 
print(tupla[1]) # Resultado: 2
# los indices se enumeran desde 0 en adelante
# las tuplas pueden contener otras tuplas dentro de ellas
tupla3 = (1,2,('x','y','z'),3,4)