class Livro:
    def __init__(self, titulo, autor, ano):
        if not titulo:
            raise ValueError("O título do livro não pode ser vazio.")
        if ano < 1450 or ano > 2026:
            raise ValueError("Ano invalido. O ano deve estar entre 1450 e 2026.")

        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor):
        if valor < 1450 or valor > 2026:
            raise ValueError("Ano invalido. O ano deve estar entre 1450 e 2026.")
        self._ano = valor



    def desctricao(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"

    def __str__(self):
        return self.desctricao()

    def idade(self):
        return 2026 - self.ano


class Usuario:
    def __init__(self, nome, matricula):
        if not nome:
            raise ValueError("O nome é obrigatório.")
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"Usuário: {self.nome}, Matrícula: {self.matricula}"

class Emprestimo:
    def __init__(self, livro, usuario, data):
        self.livro = livro
        self.usuario = usuario
        self.data = data 
        self.devolvido = False

    def devolver(self):
        if self.devolvido:
            raise ValueError("O livro já foi devolvido.")
        self.devolvido = True

    def __str__(self):
        estado = "devolvido" if self.devolvido else "em aberto"
        return f"{self.livro.titulo} -> {self.usuario.nome} ({estado})"

livro = Livro("Dom Casmurro", "Machado de Assis", 1899)

ana = Usuario("Ana Souza", "2026001")
emp = Emprestimo(livro, ana, "20-08-2026")


print(emp)
print(emp.livro.autor)
print(emp.usuario.matricula)

emp.devolver()
print(emp)
emp.devolver()

if __name__ == "__main__":
    acervo = [
        Livro("Dom Casmurro", "Machado de Assis", 1899),
        Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
    ]

    for livro in acervo:
        print(livro.desctricao())

    Livro ("Livro sem título", "Autor Desconhecido", 3000)