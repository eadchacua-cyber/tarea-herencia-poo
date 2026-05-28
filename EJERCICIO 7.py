class ActividadLibre:
    def __init__(self, pasatiempo, horas_dedicadas, lugar):
        self.pasatiempo = pasatiempo
        self.horas_dedicadas = horas_dedicadas
        self.lugar = lugar
    def iniciar_actividad(self):
        return f"Empezando a practicar: {self.pasatiempo} en mi {self.lugar}."

class ProgramarTiemposLibres(ActividadLibre):
    def __init__(self, pasatiempo, horas_dedicadas, lugar, lenguaje):
        super().__init__(pasatiempo, horas_dedicadas, lugar)
        self.lenguaje = lenguaje
    def desarrollar_codigo(self):
        return f"yo aprovecho mis tiempos libres para programar proyectos en {self.lenguaje} durante {self.horas_dedicadas} minutos."

mi_hobby = ProgramarTiemposLibres("Programación Web", 30, "Escritorio", "Python y JavaScript")
print(mi_hobby.start_actividad() if hasattr(mi_hobby, 'start_actividad') else mi_hobby.iniciar_actividad())
print(mi_hobby.desarrollar_codigo())