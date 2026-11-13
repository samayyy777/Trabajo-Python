from modelo.biblioteca_ficheros import cargar_libros, cargar_socios

lista_libros = cargar_libros("datos/libros.txt")
lista_socios = cargar_socios("datos/socios.txt")

print("Se han cargado " + str(len(lista_libros)) + " libros")
print("Se han cargado " + str(len(lista_socios)) + " socios")
print(lista_libros[0])
print(lista_socios[0])