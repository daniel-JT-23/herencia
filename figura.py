import turtle


def dibujar_figura(lados, tamaño, color):
    ventana = turtle.Screen()
    ventana.title(f"Dibujo de una figura de {lados} lados")

    figura = turtle.Turtle()
    figura.color(color)
    figura.begin_fill()

    for _ in range(lados):
        figura.forward(tamaño)
        figura.right(360 / lados)

    figura.end_fill()
    ventana.mainloop()


dibujar_figura(5, 100, "blue")  # Dibuja un pentágono azul
