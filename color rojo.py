import turtle


def dibujar_rectangulo_rojo(ancho, alto):
    ventana = turtle.Screen()
    ventana.title("Dibujo de un Rectángulo Rojo")

    rectangulo = turtle.Turtle()
    rectangulo.speed(3)
    rectangulo.color("red")  # Establece el color rojo
    rectangulo.begin_fill()  # Comienza el relleno con color

    for _ in range(2):
        rectangulo.forward(ancho)
        rectangulo.right(90)
        rectangulo.forward(alto)
        rectangulo.right(90)

    rectangulo.end_fill()  # Finaliza el relleno de color

    ventana.mainloop()


dibujar_rectangulo_rojo(150, 100)  # Dibuja un rectángulo rojo de 150x100 píxeles
