# Sistema de gestion de biblioteca, mini documentacion

## Estructura del proyecto

El proyecto se estructura de la siguiente manera:

- `modelo`: clases `Libro` y `Socio`, lectura y escritura de ficheros y log.
- `errores`: excepcion personalizada `PrestamoError`.
- `datos`: ficheros `libros.txt` (100 libros) y `socios.txt` (15 socios).
- `main.py`: menu principal y funciones de cada opcion.

## Como ejecutarlo

- Si tuvieramos que ejecutarlo desde el git, tendriamos que poner el comando: python main.py
- O simplemente ejecutar desde cualquier eejcutor de codigo compatible

    

## Funcionalidades

1. Mostrar todos los libros.
2. Mostrar libros disponibles.
3. Buscar libro por titulo (sin distinguir mayusculas).
4. Prestar un libro a un socio.
5. Devolver el libro de un socio.
6. Mostrar socios con libro prestado.
7. Añadir socios y libros.
8. Guardar y salir.

Los prestamos, devoluciones, altas y errores se registran en `log.txt`

## Posibles mejoras que no pondre por falta de tiempo

- Añadir opciones para eliminar o modificar libros y socios.
- Permitir que un socio tenga varios libros a la vez.
- Guardar la fecha del prestamo y avisar de devoluciones atrasadas.
- Validar el formato del email y de los codigos.
- Usar una base de datos (SQLite) en lugar de ficheros de texto.
- Crear una interfaz grafica o web.a
- Añadir pruebas automaticas.
- Buscar tambien por autor o categoria.
