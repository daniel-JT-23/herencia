class Vehiculo:
    def __init__(self, color, modelo, placa, valor, cilindraje, año, tipo_puertas,
                 combustible, kilometraje, caja_cambios, seguro, gama, chasis,
                 pais_origen, marca, llanta_emergencia, numero_puertas):
        self.color = color
        self.modelo = modelo
        self.placa = placa
        self.valor = valor
        self.cilindraje = cilindraje
        self.año = año
        self.tipo_puertas = tipo_puertas
        self.combustible = combustible
        self.kilometraje = kilometraje
        self.caja_cambios = caja_cambios
        self.seguro = seguro
        self.gama = gama
        self.chasis = chasis
        self.pais_origen = pais_origen
        self.marca = marca
        self.llanta_emergencia = llanta_emergencia
        self.numero_puertas = numero_puertas

    def vender(self):
        return f"El vehículo {self.marca} {self.modelo} ha sido vendido."

    def acelerar(self):
        return f"El {self.marca} {self.modelo} está acelerando."

    def frenar(self):
        return f"El {self.marca} {self.modelo} está frenando."

    def girar(self, direccion):
        return f"El {self.marca} {self.modelo} está girando hacia {direccion}."

    def encender(self):
        return f"El {self.marca} {self.modelo} ha sido encendido."

    def apagar(self):
        return f"El {self.marca} {self.modelo} ha sido apagado."

# Ejemplo de uso
mi_carro = Vehiculo("Rojo", "Corolla", "ABC123", 15000, 1600, 2021, "Sedán",
                    "Gasolina", 50000, "Automática", True, "Alta", "XYZ789",
                    "Japón", "Toyota", True, 4)

print(mi_carro.encender())
print(mi_carro.acelerar())
print(mi_carro.frenar())
