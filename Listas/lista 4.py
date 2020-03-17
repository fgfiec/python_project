#Crie uma lista qualquer e faça um programa que imprima cada elementoda lista usando o ​for
'''
lista = [1,2,3,4,5,6,7]
print(lista)
for n in lista:
    print(n)
'''

#Faça um programa que peça para o usuário digitar um número n eimprima uma lista com todos os números de 0 a n-1
'''
lista =[]
ent = int(input("entre o número limite: "))
for n in range(0,ent):
    print(n)
'''

#Faça um programa que olhe todos os itens de uma lista e diga quantos deles são pares.
'''
teste = range(1,100,1)
conta=0
for n in teste:
    if n%2==0:
        conta = conta+1
print("Existem %d pares na lista" %conta)
'''

#Faça um programa que imprima o maior número de uma lista, sem usarmax()​.
'''
teste = range(1,100,1)
maior = 0
for n in teste:
    if n > maior:
        maior = n
print(maior)
'''

#Agora usando ​max() ​faça um programa que imprima os três maioresnúmeros de uma lista.
'''
teste = [1,2,3,4,5,6,7,8,9]
n=1
while n <=3:
    a = max(teste)
    print(a)
    teste.remove(a)
    n=n+1
'''

#Faça um programa que, dadas duas listas de mesmo tamanho,
#crie umanova lista com cada elemento igual a soma dos elementos da lista 1 com alista 2, na mesma posição
'''
lista1 = [2,3,4]
lista2 = [3,2,1]
lista3=[]
n=0
a = 0
soma = 0
while n < len(lista1):
    a = lista1[n] + lista2[n]
    lista3.append(a)
    n = n + 1

print(lista3)
'''

#Faça um programa que dadas duas listas de mesmo tamanho, imprima o produto escalar entre elas.
'''
lista1 = [2,3,4]
lista2 = [3,2,1]
lista3=[]
n=0
a = 0
soma = 0
while n < len(lista1):
    a = lista1[n] * lista2[n]
    lista3.append(a)
    soma = soma + lista3[n]
    n = n + 1

print(soma)
'''
#Faça um programa que pede para o usuário digitar 5 números e, ao final,imprime uma lista com os 5 números digitados pelo usuário
'''
lista = []

for n in range(0,5,1):
    lista.append(input("Entre o %d numero: " %n))
print(lista)

# Pegue a lista gerada no exercício anterior e transforme cada um dos itens dessa lista em um ​float

for n in range(0,len(lista)):
    lista[n] = float(lista[n])
print(lista)

'''
#Faça um Programa que peça as 4 notas bimestrais e mostre a média,usando listas.

lista = []
soma = 0
for n in range(4):
    lista.append(float(input("Entre a %d nota: " %n)))
    soma = soma + lista[n]
media = soma/len(lista)
print(lista)
print(media)
