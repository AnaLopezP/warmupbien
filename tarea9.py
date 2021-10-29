from os import close, read


f = open("flag.txt", "r")
texto = f.read()
f.close()
print(texto)
f = open("flag.txt", "a")
f.write("prueba de añadir texto en el fichero")
f.close()
f = open("flag.txt", "r")
texto = f.read()
f.close()
print(texto)