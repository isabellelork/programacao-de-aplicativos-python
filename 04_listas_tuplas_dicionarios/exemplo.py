#Listas, Tuplas e Dcionários

#1. Listas

#Listas são utilizadas para armazenar vários valores
#dentro de uma única variável

nomes = ["Ana" , "Carlos" , "João" , "Maria"]
print(nomes)

#2. Acessando elementos da lista

print(nomes[0])
print(nomes[1])

#Podemos acessar o ultimo elemento usando -1

print(nomes[-1])

#3. Alterando elementos
#As listas são mutáveis, ou seja, os elementos podem ser alterados

nomes[0] = "Pedro"
print(nomes)

#4. Adicionando elementos
#append() - adiciona um elemento no final da lista.

nomes.append("Lucas")
print(nomes)

#insert() - adiciona um elemento em uma posição

nomes.insert(1, "Mariana")
print(nomes)

#5. Removendo Elementos
#remove() - remove um elemento pelo seu valor

nomes.remove("Lucas")
print(nomes)

#pop () - remove um elemento pelo indice

nomes.pop(0)
print(nomes)

# 6.Tamanho da lista

# len() informa a quantidade de elementos.
print(len(nomes))

#7
for none in nomes:
    print(nome)

#8 verificando se um elemento existe

if "João" in nomes:
    print("João está na lista.")

else:
    print("João não está na lista.")


#9 lista com diferentes tipos de dados

dados = ["João", 18, 1.75. True]
print(dados)

#10 lista de numeros

notas [7.5, 8.0, 6.5, 9.0]
soma = 0

for nota in notas:
    soma += nota

media = soma /len(notas)

print(f"Média: {media:.1f}")

#11 tuplas

coordenadas (10, 20)
print(coordenadas)

#acessando elementos

print(coordenadas[0])
print(coordenadas[1])

#12 dicionarios

aluno = {
    "nome": "Carlos",
    "idade": 17
    "nota": 8.5

}

print(aluno)

#13 acessando os valores do dicionario

print(aluno["nome"])
print(aluno["idade"])
print(aluno["nota"])