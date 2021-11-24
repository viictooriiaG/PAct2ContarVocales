#CONTAR VOCALES EN PARALELO#
import os
import time
#CONTAR VOCALES EN SERIE#
from multiprocessing import Process


class Proceso (Process):
    def __init__(self, caracter):
        Process.__init__(self)
        self.caracter = caracter

    def run(self):
        fichero=open("archivo.txt")
        contador=0
        fichero_size = os.stat("archivo.txt") #os.stat saca los metadatos del fichero

        for cursor in range(fichero_size.st_size): #para sacar el numero total de caracteres del fichero en byte
            x=fichero.read(1)
            if (self.caracter==x):
                contador = contador + 1
        fichero.close()
        print(f"Caracter {self.caracter} : total de letras: {contador}")


if __name__ == '__main__':
    tiempo = time.time_ns()
    lista=[]
    procesoA = Proceso("a")
    procesoE = Proceso("e")
    procesoI = Proceso("i")
    procesoO = Proceso("o")
    procesoU = Proceso("u")

    lista.append(procesoA)
    lista.append(procesoE)
    lista.append(procesoI)
    lista.append(procesoO)
    lista.append(procesoU)
    #Arrancamos todos los procesos
    for i in range(len(lista)):
        lista[i].start()
    #El padre espera a los procesos
    for i in range(len(lista)):
        lista[i].join()
    tiempofinal = time.time_ns()
    print("El tiempo que tardan todos los procesos: ",(tiempofinal-tiempo), "nanosegundos.")