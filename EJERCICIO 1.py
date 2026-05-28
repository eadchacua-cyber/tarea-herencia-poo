class InstitutoYavirac:
    def __init__(self, institucion, carrera, jornada):
        self.institucion = institucion
        self.carrera = carrera
        self.jornada = jornada
    def mostrar_info(self):
        return f"Bienvenido al {self.institucion}, carrera de {self.carrera}."

class SegundoSemestre(InstitutoYavirac):
    def __init__(self, institucion, carrera, jornada, paralelo):
        super().__init__(institucion, carrera, jornada)
        self.paralelo = paralelo
    def matricular_estudiante(self):
        return f"yo ya estoy matriculado en el segundo semestre, paralelo {self.paralelo}."

# Ejecución en consola
mi_matricula = SegundoSemestre("Yavirac", "Desarrollo de Software", "vespertina", "c")
print(mi_matricula.mostrar_info())
print(mi_matricula.matricular_estudiante())