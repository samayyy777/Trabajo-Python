from modelo.libro import Libro
from modelo.socio import Socio

libro = Libro("L001", "El Quijote", "Cervantes", 1605, "Novela")
socio = Socio("S001", "Ana Pérez", "ana@correo.com")

print(libro)
print(socio)
print(libro.esta_disponible())
print(socio.tiene_libro())