"""Level 1"""
#Operands

print(3 + 4) #addition(+)
print(4 - 3) #substraction(-)
print(4 % 3) #modulus(%)
print(4 / 3) #division(/)
print(3 ** 4) #exponential(**)
print(4 // 3) #integer division(//)
print("\n") # Salto de linea


#Strings. To create a string, just put any character (or text) between quotes.

print("Spain")
print("I am enjoying 30 days python")
print("\n") # Salto de linea


#Data types

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(["Name", "Pyhton", "Hello"]))
print(type("Hi"))
print(type("Spain")) # A partir de aqui hablamos en español
print("\n") # Salto de linea


#Ejercicio 3.1 --> Aqui van algunos ejercicios extra donde podemos ver qué tipos de clases podemos albergar dentro de otras, para mayor aclaracion
print(type(True))
print(type(["qe ase", 78, {45, "98", "cien"}, (3,4), {"hola":34}])) # Listas. Podemos meter strings, enteros, decimales, tuplas
print(type({"hola", 8, ("hola", 98)})) # Conjuntos  {"hola":8} daria error, en un conjunto solo podemos meter string, enteros, y conjuntos formados por estos ultimos
print(type(("adios", 87))) # Tuplas, formadas por string y enteros o decimales
print(type({"hola, boog":67})) # Diccionarios, se definen con una clave , y un valor asociado,, separado por ":"{"clave":6}, 
print("\n") # Salto de linea

#Ejercicio 3.3
print("Euclidean distance between (2,3) and (10,8)")
print(f" La distancia sera: {((10 - 2) ** 2 + (8 - 3) ** 2) ** (1/2):.2f}") # Esto es una cadena formateada print(f""), y es el metodo actual mas elegante para formatear texto
#Los dos puntos indica que empieza la especificacion del formato, .2 que quiero 2 decimales, y f que deseo el formato float
