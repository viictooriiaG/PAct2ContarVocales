import os
import time
#CONTAR VOCALES EN SERIE#

def leerArchivo(caracter):
    fichero=open("archivo.txt")
    contador=0
    fichero_size = os.stat("archivo.txt")

    for cursor in range(fichero_size.st_size): #para sacar el numero total de caracteres del fichero en byte
        x=fichero.read(1)
        if (caracter==x):
            contador = contador + 1
    fichero.close()
    return contador

tiempo = time.time_ns()
print ("Caracter a: " + str(leerArchivo("a")))
print ("Caracter e: " + str(leerArchivo("e")))
print ("Caracter i: " + str(leerArchivo("i")))
print ("Caracter o: " + str(leerArchivo("o")))
print ("Caracter u: " + str(leerArchivo("u")))
tiempofinal = time.time_ns()
print("El tiempo que tarda es: ",(tiempofinal-tiempo), "nanosegundos.")