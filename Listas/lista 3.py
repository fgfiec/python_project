# Peça ao usuário um número, e imprima todos os números de um aonúmero dado:
"""
num = 1
soma = 0
user = int(input('Entre um inteiro: '))
while num <=user:
    soma = soma + num
    num = num + 1
    
print('A somatoria até o numero %d é %d '%(user,soma))
"""

#Peça ao usuário para digitar um número e imprima o fatorial de n.
'''
num = 1
fat = 1
user=int(input("Entre um inteiro para calculo fatorial: "))
while num <=user:
    fat=fat*num
    num=num+1
print("O fatorial de %d é %d"%(user,fat))
'''

#Faça um programa que imprima a tabuada de 9 (de 9*1 a 9*10) usando loops.
'''
num=1
tab=1
while num <=10:
    tab=num*9
    print('9 x %d = %d' %(num,tab))
    num=num+1
'''

#Dado um número, imprima na tela todos os seus divisores.
'''
num=1
user=int(input('Entre o número inteiro para encontrar os divisores: '))
while num <=user:
    if user%num ==0:
        print(num)
        num=num+1
    else:
        num=num+1
'''

# Desafio 1
'''
num = 0
soma = 0
while num<1000:
    soma = soma + (1/2**num)
    num = num + 1
print("A soma dos mil primeiros termos é: ",soma)
'''
#Desafio 2
'''
num = 1
soma = 0
fat=1
while num<1000:
    soma = soma + (1/fat)
    fat=fat*num
    num = num + 1
print("A soma dos mil primeiros termos é: ",soma)
'''
