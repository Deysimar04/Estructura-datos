class Libro:
    def __init__(self, titulo, autor, genero, año_de_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año_de_publicacion = año_de_publicacion

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_autor(self):
        return self.autor

    def set_autor(self, autor):
        self.autor = autor

    def get_genero(self):
        return self.genero

    def set_genero(self, genero):
        self.genero = genero

    def get_año_de_publicacion(self):
        return self.año_de_publicacion

    def set_año_de_publicacion(self, año_de_publicacion):
        self.año_de_publicacion = año_de_publicacion

    def mostrar_detalles(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Género: {self.genero}")
        print(f"Año de Publicación: {self.año_de_publicacion}")


libro = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 1967)
libro.mostrar_detalles()