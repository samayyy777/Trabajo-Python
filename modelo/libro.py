class Libro:
    def __init__(self, codigo, titulo, autor, anio, categoria, codigo_socio=None):
        
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.categoria = categoria
        self.codigo_socio = codigo_socio

    def esta_disponible(self):
        
        if self.codigo_socio is None:
            return True
        else:
            return False

    def __str__(self):
        
        if self.esta_disponible():
            
            estado = "Disponible"
            
        else:
            
            estado = "Prestado al socio " + self.codigo_socio
        texto = self.codigo + " | " + self.titulo + " | " + self.autor + " | " + estado
        
        return texto