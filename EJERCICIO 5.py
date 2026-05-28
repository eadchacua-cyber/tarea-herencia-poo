class MascotaHogar:
    def __init__(self, nombre_mascota, edad_mascota, tipo_animal):
        self.nombre_mascota = nombre_mascota
        self.edad_mascota = edad_mascota
        self.tipo_animal = tipo_animal
    def dar_comida(self):
        return f"{self.nombre_mascota} el {self.tipo_animal} mio está feliz."

class PerroScubi(MascotaHogar):
    def __init__(self, nombre_mascota, edad_mascota, tipo_animal, raza_perro):
        super().__init__(nombre_mascota, edad_mascota, tipo_animal)
        self.raza_perro = raza_perro
    def hacer_sonido(self):
        return f"¡Guau guau! a mi hermoso {self.nombre_mascota} le gusta que le lanze rocas y traermelas denuevo."

mi_perro = PerroScubi("Scubi", 2, "Perro", "Criollo")
print(mi_perro.dar_comida())
print(mi_perro.hacer_sonido())