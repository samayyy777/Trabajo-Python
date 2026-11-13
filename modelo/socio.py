class Socio:
    def __init__(self, codigo, nombre, email, codigo_libro=None):
        
        self.codigo = codigo
        self.nombre = nombre
        self.email = email
        self.codigo_libro = codigo_libro

    def tiene_libro(self):
        
        if self.codigo_libro is None:
            return False
        else:
            return True

    def __str__(self):
        if self.tiene_libro():
            libro = self.codigo_libro
        else:
            libro = "ninguno"
            
        texto = self.codigo + " | " + self.nombre + " | " + self.email + " | Libro: " + libro
        
        return texto