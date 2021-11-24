fichero=open("archivo.txt")
contador = 0
for i in fichero:
    if i in "aeiou":
        contador=contador+1
    print ("La cantidad de vocales son ")
