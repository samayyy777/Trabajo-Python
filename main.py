from modelo.biblioteca_ficheros import cargar_libros, cargar_socios

RUTA_LIBROS = "datos/libros.txt"
RUTA_SOCIOS = "datos/socios.txt"


def mostrar_menu():
    print("")
    print("===== BIBLIOTECA =====")
    print("1. Mostrar todos los libros")
    print("2. Mostrar libros disponibles")
    print("3. Buscar libro por titulo")
    print("4. Prestar un libro")
    print("5. Devolver un libro")
    print("6. Mostrar socios con libro")
    print("7. Anadir socio o libro")
    print("8. Salir")


def mostrar_todos_los_libros(lista_libros):
    # Recorre la lista y muestra todos los libros
    print("--- Todos los libros ---")
    for libro in lista_libros:
        print(libro)


def mostrar_libros_disponibles(lista_libros):
    # Muestra solo los libros que nadie tiene
    print("--- Libros disponibles ---")
    contador = 0
    for libro in lista_libros:
        if libro.esta_disponible():
            print(libro)
            contador = contador + 1
    if contador == 0:
        print("No hay libros disponibles")


def buscar_libro(lista_libros):
    # Busca libros cuyo titulo contenga el texto escrito
    termino = input("Escribe parte del titulo: ")
    termino = termino.strip().lower()
    if termino == "":
        print("No has escrito nada")
        return
    encontrado = False
    for libro in lista_libros:
        titulo_en_minusculas = libro.titulo.lower()
        if termino in titulo_en_minusculas:
            print(libro)
            encontrado = True
    if encontrado == False:
        print("No existe ningun libro con ese termino")


def main():
    lista_libros = cargar_libros(RUTA_LIBROS)
    lista_socios = cargar_socios(RUTA_SOCIOS)
    print("Se ha cargado la informacion de " + str(len(lista_libros)) + " libros")
    print("Se ha cargado la informacion de " + str(len(lista_socios)) + " socios")

    opcion = ""
    while opcion != "8":
        mostrar_menu()
        opcion = input("Elige una opcion: ")
        if opcion == "1":
            mostrar_todos_los_libros(lista_libros)
        elif opcion == "2":
            mostrar_libros_disponibles(lista_libros)
        elif opcion == "3":
            buscar_libro(lista_libros)
        elif opcion == "4" or opcion == "5" or opcion == "6" or opcion == "7":
            print("Esta opcion todavia no esta disponible")
        elif opcion == "8":
            print("Hasta pronto")
        else:
            print("Opcion no valida")


main()