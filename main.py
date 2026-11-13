from errores.excepciones import PrestamoError

try:
    raise PrestamoError("El libro ya esta prestado", "L001", "S002")
except PrestamoError as error:
    print("Error: " + error.mensaje)
    print("Libro: " + error.codigo_libro)
    print("Socio: " + error.codigo_socio)