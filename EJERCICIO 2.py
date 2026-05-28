class VideojuegoMovil:
    def __init__(self, juego, desarrollador, peso_gb):
        self.juego = juego
        self.desarrollador = desarrollador
        self.peso_gb = peso_gb
    def iniciar_juego(self):
        return f"Cargando {self.juego} por {self.desarrollador}... (Peso: {self.peso_gb} GB)"

class MiFreeFire(VideojuegoMovil):
    def __init__(self, juego, desarrollador, peso_gb, rango_clasificatoria):
        super().__init__(juego, desarrollador, peso_gb)
        self.rango_clasificatoria = rango_clasificatoria
    def jugar_partida(self):
        return f"yo me pongo a juagr en escuadra. ¡Buscando el Booyah! Rango actual: {self.rango_clasificatoria}."

mi_partida = MiFreeFire("Free Fire", "Garena", 3.5, "gran maestro elite")
print(mi_partida.iniciar_juego())
print(mi_partida.jugar_partida())