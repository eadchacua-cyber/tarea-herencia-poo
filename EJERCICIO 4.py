class ServicioStreaming:
    def __init__(self, plataforma, usuario, tipo_plan):
        self.plataforma = plataforma
        self.usuario = usuario
        self.tipo_plan = tipo_plan
    def iniciar_cuenta(self):
        return f"Cuenta {self.tipo_plan} de {self.usuario} activa en {self.plataforma}."

class MiAppleMusic(ServicioStreaming):
    def __init__(self, plataforma, usuario, tipo_plan, calidad_audio):
        super().__init__(plataforma, usuario, tipo_plan)
        self.calidad_audio = calidad_audio
    def reproducir_musica(self):
        return f"yo escucho música en {self.plataforma} con audio {self.calidad_audio}."

mi_musica = MiAppleMusic("Apple Music", "Eduardo", "Plan Estudiante", "Hi-Res Lossless")
print(mi_musica.iniciar_cuenta())
print(mi_musica.reproducir_musica())