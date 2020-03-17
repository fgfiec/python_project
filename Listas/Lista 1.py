#Faça um programa que mostre a mensagem "Olá, mundo!" na tela.
'''
print("Olá, Mundo")

#Faça um programa que peça um número e mostre a mensagem "O número informado foi [número]"

numero = input("Digite um Número: ")
print("O número informado foi: ",numero)

# Faça um programa que peça um número para o usuário (string),
#converta-o para float e depois imprima-o na tela. Você consegue fazer a mesma coisa, porém convertendo para int

numero = int(input("Digite um Número: "))
print("O número informado foi: ",numero)

#Faça um programa que peça dois números e imprima a soma deles.

numero1 = int(input("Entre o primeiro número: "))
numero2 = int(input("Entre o segundo número: "))
soma=numero1+numero2
print("a soma dos números é: ",soma)

#Faça um programa que peça as 4 notas bimestrais de um aluno e mostre a média aritmética delas.

nota1 = float(input("insira a primeira nota"))
nota2 = float(input("insira a segunda nota"))
nota3 = float(input("insira a terceira nota"))
nota4 = float(input("insira a quarta nota"))

media = (nota1 + nota2 + nota3 + nota4)/4

print("a Média final é: ",media)


#Faça um programa que peça as 4 notas bimestrais de um aluno e mostre a média aritmética delas.

notas = float(input("insira a primeira nota: "))
notas = notas + float(input("insira a segunda nota: "))
notas = notas + float(input("insira a terceira nota: "))
notas = notas + float(input("insira a quarta nota": ))

notas = notas/4

print("a Média final é: ",notas)

# Faça  um  programa  que  converta  um  valor  em  metros  para centímetros.

m = float(input("Entre a medida em metros: "))
cm=m*100
print("O equivalente em centimentros da medida é ", cm ,"cm")


#Faça um programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input("Entre o raio desejado: "))
Area= 3.14*raio**2
print("A área do circulo com raio", raio, "é de ",Area)

#Faça um programa que pergunte quanto você ganha
#por hora e o número de horas trabalhadas no mês e depois, calcule e mostre o total do seu salário no referido mês.

salario = float(input("Informa seu salário por hora: "))
horas = int(input("/informe volume de horas trabalhas por mês: "))
rendimento=salario*horas
print("O salário mensal é de: ",rendimento)

#Faça um programa que peça a temperatura em graus Fahrenheit (F), transforme e mostre a temperatura em graus Celsius (°C).

Fahr = float(input("Entre a temperatura em Fahrenheit: "))
Celsius= (5*(Fahr-32)/9)
print("A temperatura em Celsius é: %f" %Celsius)

#Faça um programa que peça o dia, o mês e o ano para o usuário e imprima a data completa no formato dd/mm/aaaa

dia = int(input("Entre um dia (1-31): "))
mes = int(input("Entre o mes (1-12): "))
ano = int(input("Entre um ano com 4 dígitos: "))

print("a data selecionada é: %d/%d/%d" %(dia,mes,ano))
'''

#Faça um programa que peça 2 números inteiros e um número real, calcule e mostre:
#a)o produto do dobro do primeiro com metade do segundo.
#b)a soma do triplo do primeiro com o terceiro.
#c)o terceiro elevado ao cubo.

int1 = int(input("Entre o primeiro número inteiro: "))
int2 = int(input("Entre o segunto número inteiro: "))
real1 =float(input("Entre um número Real: "))

a = (2*int1)*(int2/2)
b = (3*int1)+real1
c = real1**3

print(a," ",b," ",c)
