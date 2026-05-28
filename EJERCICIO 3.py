class PlatoComida:
    def __init__(self, nombre_plato, precio, ingrediente_principal):
        self.nombre_plato = nombre_plato
        self.precio = precio
        self.ingrediente_principal = ingrediente_principal
    def servir_orden(self):
        return f"Sirviendo {self.nombre_plato} con bastante {self.ingrediente_principal}."

class OrdenSalchipapa(PlatoComida):
    def __init__(self, nombre_plato, precio, ingrediente_principal, cantidad_porciones):
        super().__init__(nombre_plato, precio, ingrediente_principal)
        self.cantidad_porciones = cantidad_porciones
    def agregar_cremas(self):
        return f"yo pido para mis hermanos {self.cantidad_porciones} salchipapas con todas las cremas por ${self.precio} cada uno."

mi_comida = OrdenSalchipapa("Salchipapa", 2.50, "Papas y buena salchicha", 4)
print(mi_comida.servir_orden())
print(mi_comida.agregar_cremas())