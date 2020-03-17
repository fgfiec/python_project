#Faça uma função que recebe um número e ​imprime ​seu dobro.
'''
def dobro(num1):
    a = num1*2
    print(a)

dobro(2)

'''

#Faça uma função que receba um valor do raio de um círculo e ​retorne ​o
#valor do comprimento de sua circunferência: C = 2*pi*r.
'''
def circuferencia(raio):
    circ = 2*3.1416*raio
    return (circ)

a = circuferencia(float(input("entre o raio do circulo a ser calculado: ")))
print(a)
'''

#Faça uma função para cada operação matemática básica
#(soma, subtração,multiplicação e divisão).
#As funções devem receber dois números eretornar ​o resultado da operação.
'''
def calculator(num1,num2):
     return num1+num2,num1-num2,num1*num2,num1/num2
'''

#Faça uma função que recebe um nome e ​imprima ​“ola [nome]”.
'''
def saudacao(nome):
    print("ola, %s" %nome)
'''

#Faça uma função que recebe um nome e um horário e ​imprime ​“Bom dia[nome]”, caso seja antes de 12h,
#“Boa Tarde [nome]”, caso seja entre 12h e18h e “boa noite [nome]” se for após
#às 18h.
'''
def saudacao(nome,hora):
    if hora < 12:
        print("Bom dia, %s" %nome)
    elif hora>=12 and hora<=18:
        print("Boa tarde, %s" %nome)
    else:
        print("Boa noite, %s" %nome)
nome = input("Entre seu nome: ")
hora = int(input("Entre o horario (24h): "))
saudacao(nome,hora)
'''

#Faça uma função que recebe um número e ​retorne True ​se ele é par ou False​, se não.
'''
def checa_par(num1):
    if num1%2==0:
        return True
    else:
        return False
'''

#Faça uma função que sorteie 10 números aleatórios entre 0 e 100 e ​retorne o maior entre eles.
'''
def max_rnd():
    lista = []
    import random
    for n in range(10):
        a = random.randrange(1,100,1)
        lista.append(a)
    return max(lista)
'''

#Faça uma função que receba um número ​n ​de entrada, sorteie ​n​ números aleatórios entre 0 e 100 e ​retorne ​a média deles.
'''
def media_rnd(n1):
    lista = []
    import random
    soma=0
    for n in range(n1):
        a = random.randrange(1,100,1)
        lista.append(a)
        soma = soma + lista[n]
    return soma/len(lista)
'''

#Desafio(1/2) Faça uma função que receba um número e calcule seu fatorial.
'''
def fat(n):
    if n == 0:
        return 1
    else:
        return n*fat(n-1)

'''
    
#Desafio 4

def blackjack():
    num_player = int(input("Entre o número de jogadores: "))
    players=[]
    for n in range(player):
        players.append(input("Entre o nome do jogadore n%d: " %n))
        
                       
