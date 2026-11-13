from modelo.biblioteca_ficheros import cargar_libros, cargar_socios
from modelo.log import registrar_evento
from errores.excepciones import PrestamoError

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
        elif opcion == "4":
            opcion_prestar(lista_libros, lista_socios)
        elif opcion == "5":
            devolver_libro(lista_libros, lista_socios)
        elif opcion == "6":
            mostrar_socios_con_libro(lista_libros, lista_socios)
        elif opcion == "7":
            print("Esta opcion todavia no esta disponible")
        elif opcion == "8":
            print("Hasta pronto")
        else:
            print("Opcion no valida")
            
    
def buscar_libro_por_codigo(lista_libros, codigo):
    # Devuelve el libro con ese codigo, o None si no existe
    for libro in lista_libros:
        if libro.codigo == codigo:
            return libro
    return None


def buscar_socio_por_codigo(lista_socios, codigo):
    # Devuelve el socio con ese codigo, o None si no existe
    for socio in lista_socios:
        if socio.codigo == codigo:
            return socio
    return None


def prestar_libro(lista_libros, lista_socios, codigo_libro, codigo_socio):
    # Presta el libro al socio. Si algo falla, lanza PrestamoError
    libro = buscar_libro_por_codigo(lista_libros, codigo_libro)
    socio = buscar_socio_por_codigo(lista_socios, codigo_socio)

    if libro is None:
        raise PrestamoError("El libro no existe", codigo_libro, codigo_socio)
    if socio is None:
        raise PrestamoError("El socio no existe", codigo_libro, codigo_socio)
    if libro.esta_disponible() == False:
        raise PrestamoError("El libro ya lo tiene otro socio", codigo_libro, codigo_socio)
    if socio.tiene_libro():
        raise PrestamoError("El socio ya tiene un libro", codigo_libro, codigo_socio)

    # Si llegamos aqui, todo esta bien y hacemos el prestamo
    libro.codigo_socio = codigo_socio
    socio.codigo_libro = codigo_libro
    registrar_evento("PRESTAMO", "Libro " + codigo_libro + " prestado al socio " + codigo_socio)


def opcion_prestar(lista_libros, lista_socios):
    # Pide los codigos y presta el libro, controlando los errores
    codigo_libro = input("Codigo del libro: ").strip().upper()
    codigo_socio = input("Codigo del socio: ").strip().upper()
    try:
        prestar_libro(lista_libros, lista_socios, codigo_libro, codigo_socio)
        print("Prestamo realizado correctamente")
    except PrestamoError as error:
        print("No se puede prestar: " + error.mensaje)
        registrar_evento("ERROR_PRESTAMO", error.mensaje + " (libro " + error.codigo_libro + ", socio " + error.codigo_socio + ")")


def devolver_libro(lista_libros, lista_socios):
    # Pide el codigo de socio y devuelve el libro que tenga
    codigo_socio = input("Codigo del socio: ").strip().upper()
    socio = buscar_socio_por_codigo(lista_socios, codigo_socio)

    if socio is None:
        print("El socio no existe")
        return
    if socio.tiene_libro() == False:
        print("Ese socio no tiene ningun libro")
        return

    codigo_libro = socio.codigo_libro
    libro = buscar_libro_por_codigo(lista_libros, codigo_libro)
    libro.codigo_socio = None
    socio.codigo_libro = None
    registrar_evento("DEVOLUCION", "Libro " + codigo_libro + " devuelto por el socio " + codigo_socio)
    print("Libro " + codigo_libro + " devuelto correctamente")


def mostrar_socios_con_libro(lista_libros, lista_socios):
    # Muestra los socios que tienen un libro y cual es
    print("--- Socios con libro ---")
    contador = 0
    for socio in lista_socios:
        if socio.tiene_libro():
            libro = buscar_libro_por_codigo(lista_libros, socio.codigo_libro)
            print(socio.nombre + " (" + socio.codigo + ") tiene: " + libro.titulo)
            contador = contador + 1
    if contador == 0:
        print("Ningun socio tiene libros")



main()