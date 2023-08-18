class Autor:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


autor_jk_rowling = Autor(nome="J.K. Rowling", data_nascimento="31 de julho de 2005")
livro_harry_potter = Livro(titulo="Harry Potter e a Pedra Filosofal", autor=autor_jk_rowling)

print(f"O autor do livro '{livro_harry_potter.titulo}' é {livro_harry_potter.autor.nome}, nascido em {livro_harry_potter.autor.data_nascimento}")
