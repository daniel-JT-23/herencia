class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def __str__(self):
        return f"Cuadrado de lado {self.lado} y área {self.area()}"

# Ejemplo de uso
c1 = Cuadrado(5)
print(c1)

import turtle

def dibujar_cuadrado(lado):
    ventana = turtle.Screen()
    ventana.title("Dibujo de un Cuadrado")

    cuadrado = turtle.Turtle()
    cuadrado.speed(3)

    for _ in range(4):
        cuadrado.forward(lado)
        cuadrado.right(90)

    ventana.mainloop()

dibujar_cuadrado(100)  # Dibuja un cuadrado de 100 píxeles por lado
