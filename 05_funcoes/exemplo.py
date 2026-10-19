# 1. Criando uma função simples
def saudacao_simples():
    print("Olá, seja bem-vindo")

saudacao_simples()


# 2. Função com parâmetro
def saudacao_com_nome(nome):
    print(f"Olá, {nome}")

saudacao_com_nome("Ana")
saudacao_com_nome("Carlos")


# 3. Mais de um parâmetro
def apresentar(nome, idade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")

apresentar("Maria", 17)


# 4. Função que exibe um resultado
def somar_e_imprimir(numero1, numero2):
    resultado = numero1 + numero2
    print(f"Resultado: {resultado}")

somar_e_imprimir(10, 5)


# 5. Retornando um valor com return
def somar(numero1, numero2):
    return numero1 + numero2

resultado = somar(10, 5)
print(resultado)


# 6. Função com condição
def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

resultado = verificar_idade(20)
print(resultado)


# 7. Função com valor padrão (parâmetro opcional)
def saudacao_padrao(nome: str = "Aluno"):
    print(f"Olá, {nome}")

saudacao_padrao()
saudacao_padrao("João")
#8. varios parametros