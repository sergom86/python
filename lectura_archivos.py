import os,shutil,sys
ruta_app = os.getcwd()  # obtiene ruta del script 
contenido = os.listdir(ruta_app)  # obtiene lista con archivos/dir 
carpeta_destino = 'copiados'


for elemento in contenido:    	
	
	ruta = os.getcwd() + os.sep
	origen = ruta + elemento
	destino = ruta + carpeta_destino+os.sep+ elemento.upper()
	try:
		os.stat(ruta + carpeta_destino)
	except:
		os.mkdir(ruta + carpeta_destino)

	if os.path.exists(origen):
		print('origen ',origen)
		print('destino ',destino)
		try:
			archivo = shutil.copy2(origen, destino)
			print('Copiado...', archivo)
		except:
			print("Error inesperado:", sys.exc_info()[0])
			print('Error en la copia')