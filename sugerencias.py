# Mostrar un encabezado.
def encabezado():
	print("=====================================\n")
	print("      SUGERENCIAS DE PELÍCULAS       \n")
	print("=====================================\n")
# mostrar el perfil del usuario del argumento que se le pasa
def perfil_usuario(usuario):
	print("perfil de "+usuario["nombre"])
	print("genero_favorito "+usuario["genero_fav"])
	print("Peliculas Sugeridas", usuario["vistas"])
	# Mostrar generos de peliculas.
def mostrar_generos():
	generos=["Acción","Comedia","Terror","Animación","Drama"]
	print("-------- GÉNEROS --------")
	# Imprimir la lista de géneros
	for genero in generos:
		print(genero)
def main():
	encabezado()
	usuario=input("Buen día, ¿cuál es tu nombre? ") 
	print("¿Qué querés ver hoy, "+usuario+"?")
	peliculas=[["Rapidos y Furiosos","Acción",2001,6.8],["Troya","Acción",2004,7.3],["Terminator 2","Acción",1991,8.6],["¿Y dónde está el piloto?","Comedia",1980,7.7],["Resident Evil: Noche cero","Terror",2026,7.7],["Coco","Animación",2017,8.4],["Toy story","Animación",1995,8.3],["Shrek","Animación",2001,7.9],["El exorcista","Terror",1973,8.1],["¿Y dónde están las rubias?","Comedia",2004,5.8],["Son como niños","Comedia",2010,6]]
	mostrar_generos()   
	genero_favorito=input("¿Qué género te gusta? ")
	rating_favorito=float(input("¿Cuál es el rating mínimo? " ))
	usuario={"nombre":usuario,"genero_fav":genero_favorito,"vistas":[]}
	print ("Buscando Películas del Género "+genero_favorito)
	encontrar_pelicula=False 
	for pelicula in  peliculas:
		nombre=pelicula[0]
		genero=pelicula[1]
		rating=pelicula[3]
		if (genero_favorito.lower()==genero.lower()) and (rating_favorito<rating):
			#print(nombre)
			usuario["vistas"].append(nombre)
			encontrar_pelicula=True
	if (not encontrar_pelicula):
		print("No se ha encontrado ninguna película.") 
	perfil_usuario(usuario)  # usuario es una variable dentro del main. Pasando esa variable al procedimiento perfil_usuario
if __name__ == "__main__":
		main()
    