class RedSocialMundo:
    def __init__(self, aplicacion, nickname, total_seguidores):
        self.aplicacion = aplicacion
        self.nickname = nickname
        self.total_seguidores = total_seguidores
    def ver_perfil(self):
        return f"Perfil @{self.nickname} cargado en la plataforma {self.aplicacion}."

class MiYouTube(RedSocialMundo):
    def __init__(self, aplicacion, nickname, total_seguidores, canal_favorito):
        super().__init__(aplicacion, nickname, total_seguidores)
        self.canal_favorito = canal_favorito
    def ver_videos(self):
        return f"yo abri {self.aplicacion} para ver tutoriales de código en el canal: {self.canal_favorito}."

mi_yt = MiYouTube("YouTube", "edu_chacua", 120, "MoureDev")
print(mi_yt.ver_perfil())
print(mi_yt.ver_videos())