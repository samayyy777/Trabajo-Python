class PrestamoError(Exception):
    def __init__(self, mensaje, codigo_libro, codigo_socio):
        # Estamos llamamos al constructor de Exception para guardar el mensaje
        
        super().__init__(mensaje)
        self.mensaje = mensaje
        
        # Se supone que estos son los tributos de instancia personalizados
        self.codigo_libro = codigo_libro
        self.codigo_socio = codigo_socio