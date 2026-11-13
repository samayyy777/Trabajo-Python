from modelo.log import registrar_evento

registrar_evento("PRESTAMO", "Libro L001 prestado al socio S001")
registrar_evento("DEVOLUCION", "Libro L001 devuelto por el socio S001")
print("Eventos guardados en log.txt")