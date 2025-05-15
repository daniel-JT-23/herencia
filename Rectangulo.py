import turtle

def dibujar_rectangulo(ancho, alto):
    ventana = turtle.Screen()
    ventana.title("Dibujo de un Rectángulo")

    rectangulo = turtle.Turtle()
    rectangulo.speed(3)

    for _ in range(2):
        rectangulo.forward(ancho)
        rectangulo.right(90)
        rectangulo.forward(alto)
        rectangulo.right(90)

    ventana.mainloop()

dibujar_rectangulo(150, 100)  # Dibuja un rectángulo de 150x100 píxeles