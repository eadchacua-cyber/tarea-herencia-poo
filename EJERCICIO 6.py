class DispositivoMovil:
    def __init__(self, marca_fono, modelo_fono, capacidad_bateria):
        self.marca_fono = marca_fono
        self.modelo_fono = modelo_fono
        self.capacidad_bateria = capacidad_bateria
    def revisar_bateria(self):
        return f"Batería del {self.marca_fono} {self.modelo_fono} al {self.capacidad_bateria}%."

class MiIPhone(DispositivoMovil):
    def __init__(self, marca_fono, modelo_fono, capacidad_bateria, isla_dinamica):
        super().__init__(marca_fono, modelo_fono, capacidad_bateria)
        self.isla_dinamica = isla_dinamica
    def usar_camara(self):
        return f"a mi me gusta prestar mi celular por la camara {self.modelo_fono}. Isla dinámica: {self.isla_dinamica} dicen que toma bien las fotos."

mi_cel = MiIPhone("Apple", "iPhone 14 Pro", 83, "Activa")
print(mi_cel.revisar_bateria())
print(mi_cel.usar_camara())