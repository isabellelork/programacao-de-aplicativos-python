#1. classe: o modelo (planta)

class Celular:
    def __init__(self, marca, modelo, cor, bateria = 100):
        # atributos: as caracteristicas do objeto
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

#numero Metodos: os comportamentos do objeto
def ligar (self):
    if self.bateria == 0:
        print("sem bateria! coloque para carregar")

    else:
        self.ligado = True
        print("Ligado")

#2. Objetos: criados a partir da classe (as casas)

celular1 = Celular("Samsung", "Galaxy s23", "preto")
celular2 = Celular("Motorola", "Moto g54", "azul", 30)

#3. acessando e alterando atributos
#usamos objeto.atributo

print(celular1.marca)
print(celular1.modelo)
print(celular2.bateria)

#chamando metodos
#usamos objeto.metodo() para pedir que o objeto faca algo

celular2.ligar()