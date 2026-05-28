class RopaDiaria:
    def __init__(self, tipo_prenda, talla_prenda, color_prenda):
        self.tipo_prenda = tipo_prenda
        self.talla_prenda = talla_prenda
        self.color_prenda = color_prenda
    def lavar_prenda(self):
        return f"despues de limpiar mis {self.tipo_prenda} color {self.color_prenda}."

class MisZapatos(RopaDiaria):
    def __init__(self, tipo_prenda, talla_prenda, color_prenda, marca_zapato):
        super().__init__(tipo_prenda, talla_prenda, color_prenda)
        self.marca_zapato = marca_zapato
    def estrenar(self):
        return f"elijo bien los zapatos {self.marca_zapato} talla {self.talla_prenda}."

mis_nike = MisZapatos("Zapatos casuales", 39.5, "Negros con blanco", "Nike")
print(mis_nike.lavar_prenda())
print(mis_nike.estrenar())