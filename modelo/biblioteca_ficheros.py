from modelo.libro import Libro
from modelo.socio import Socio


def cargar_libros(ruta):
    # Esto de aqui lee el fichero y devuelve una lista de objetos Libro
    
    lista_libros = []
    archivo = open(ruta, "r", encoding="utf-8")
    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            partes = linea.split(";")
            codigo = partes[0]
            titulo = partes[1]
            autor = partes[2]
            anio = int(partes[3])
            categoria = partes[4]
            codigo_socio = partes[5]
            
            # En el fichero, None se guarda como texto
            
            if codigo_socio == "None":
                codigo_socio = None
            libro = Libro(codigo, titulo, autor, anio, categoria, codigo_socio)
            lista_libros.append(libro)
    archivo.close()
    return lista_libros


def cargar_socios(ruta):
    
    # Lee el fichero y devuelve una lista de objetos Socio
    lista_socios = []
    archivo = open(ruta, "r", encoding="utf-8")
    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            partes = linea.split(";")
            codigo = partes[0]
            nombre = partes[1]
            email = partes[2]
            codigo_libro = partes[3]
            if codigo_libro == "None":
                codigo_libro = None
            socio = Socio(codigo, nombre, email, codigo_libro)
            lista_socios.append(socio)
    archivo.close()
    return lista_socios


def guardar_libros(ruta, lista_libros):
    
    # Escribe todos los libros en el fichero, uno por linea
    archivo = open(ruta, "w", encoding="utf-8")
    for libro in lista_libros:
        if libro.codigo_socio is None:
            codigo_socio = "None"
        else:
            codigo_socio = libro.codigo_socio
        linea = libro.codigo + ";" + libro.titulo + ";" + libro.autor + ";"
        linea = linea + str(libro.anio) + ";" + libro.categoria + ";" + codigo_socio
        archivo.write(linea + "\n")
    archivo.close()


def guardar_socios(ruta, lista_socios):
    
    # Escribe todos los socios en el fichero, uno por linea
    
    archivo = open(ruta, "w", encoding="utf-8")
    for socio in lista_socios:
        if socio.codigo_libro is None:
            codigo_libro = "None"
        else:
            codigo_libro = socio.codigo_libro
        linea = socio.codigo + ";" + socio.nombre + ";" + socio.email + ";" + codigo_libro
        archivo.write(linea + "\n")
    archivo.close()