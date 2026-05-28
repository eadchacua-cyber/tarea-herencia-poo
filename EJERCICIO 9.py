class InstrumentoMusica:
    def __init__(self, nombre_inst, familia_inst, precio_inst):
        self.nombre_inst = nombre_inst
        self.familia_inst = familia_inst
        self.precio_inst = precio_inst
    def afinar_notas(self):
        return f"simpre me percato de tener afinado las cuerdas de la {self.nombre_inst} antes de tocar."

class PracticaSabados(InstrumentoMusica):
    def __init__(self, nombre_inst, familia_inst, precio_inst, horario_fijo):
        super().__init__(nombre_inst, familia_inst, precio_inst)
        self.horario_fijo = horario_fijo
    def tocar_melodia(self):
        return f"Llega el sábado ({self.horario_fijo}). entonces viene el etrenador y ya todo debe salr bien con la {self.nombre_inst}."

mi_practica = PracticaSabados("Guitarra", "Cuerdas", 150.00, "3:00 PM")
print(mi_practica.afinar_notas())
print(mi_practica.tocar_melodia())