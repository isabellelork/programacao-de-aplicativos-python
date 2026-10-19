# 1. Definição da Classe Cachorro
class Cachorro:
    def __init__(self, nome, raca, idade):
        # Atributos do objeto
        self.nome = nome
        self.raca = raca
        self.idade = idade

    # Métodos (comportamentos)
    def latir(self):
        print(f"{self.nome} diz: Au Au!")

    def mostrar_info(self):
        print(f"Nome: {self.nome} | Raça: {self.raca} | Idade: {self.idade} anos")


# 2. Criando dois objetos diferentes da classe Cachorro
cachorro1 = Cachorro("Rex", "Pastor Alemão", 3)
cachorro2 = Cachorro("Mel", "Poodle", 5)

# Chamando os métodos para o primeiro cachorro
cachorro1.latir()
cachorro1.mostrar_info()

# Chamando os métodos para o segundo cachorro
cachorro2.latir()
cachorro2.mostrar_info()

# 3. Alterando a idade do cachorro1 diretamente pelo atributo
cachorro1.idade = 4

# Conferindo a mudança chamando mostrar_info() novamente
cachorro1.mostrar_info()