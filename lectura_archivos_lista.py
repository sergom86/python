import os,shutil,sys
ruta_app = os.getcwd()  # obtiene ruta del script 
contenido = os.listdir(ruta_app)  # obtiene lista con archivos/dir 
carpeta_destino = 'listados'

ruta = os.getcwd() + os.sep
try:
	os.stat(ruta + carpeta_destino)
except:
	os.mkdir(ruta + carpeta_destino)

file = open(ruta + carpeta_destino+os.sep+"listados.txt", "w")

for elemento in contenido:				
	file.write(elemento+'\n')

file.close()			