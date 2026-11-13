from datetime import datetime


def registrar_evento(nombre_evento, detalles):
    # Guarda una linea en log.txt con el formato [Fecha][Evento][Detalles] (importante recordar)
    
    fecha_actual = datetime.now()
    texto_fecha = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
    linea = "[" + texto_fecha + "][" + nombre_evento + "][" + detalles + "]"
    archivo = open("log.txt", "a", encoding="utf-8")
    archivo.write(linea + "\n")
    archivo.close()