class Livro:
    def __init__(self, titulo, autor, ano_publicacao, preco):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.preco = preco


# Criando dois livros diferentes
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899, 39.90)
livro2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 29.50)

# Mostrando informações
print(f"Título: {livro1.titulo}, Autor: {livro1.autor}, Ano: {livro1.ano_publicacao}, Preço: R${livro1.preco}")
print(f"Título: {livro2.titulo}, Autor: {livro2.autor}, Ano: {livro2.ano_publicacao}, Preço: R${livro2.preco}")
