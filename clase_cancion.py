class Cancion:
    def __init__(self, titulo, artista, album, duracion):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_artista(self):
        return self.artista

    def set_artista(self, artista):
        self.artista = artista

    def get_album(self):
        return self.album

    def set_album(self, album):
        self.album = album

    def get_duracion(self):
        return self.duracion

    def set_duracion(self, duracion):
        self.duracion = duracion

    def reproducir(self):
        print(f"Reproduciendo '{self.titulo}' de {self.artista}...")

cancion = Cancion("Tití Me Preguntó", "Bad Bunny", "Un Verano Sin Ti", "4:03")
cancion.reproducir()
