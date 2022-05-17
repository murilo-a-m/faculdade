
''' EX1 AULA 5
altura_anacleto = 1.50
altura_felisberto = 1.10

contagem_anos = 0

while altura_felisberto <= altura_anacleto :
    altura_anacleto+=0.2
    altura_felisberto+=0.3
    contagem_anos+=1

    print(altura_anacleto,altura_felisberto,contagem_anos)

print("Foram necessários ", contagem_anos," anos para Felisberto ser maior que Anacleto")
'''

''' EX2 AULA 5
print("Sistema de média")
print("Informe o peso dos pratos um a um. Digite 0 (zero) para encerrar")

pesos_acumulados = 0        # Pesos dos pratos acumulados (somatórios)
quantidade_de_pratos = 0    # Quantidade de pesos informados
pratos_maiores_800 = 0      #Pratos que pesam mais que 800 gramas

while True:
    peso_informado =  float(input("Informe o peso do prato:"))

    #Se o peso do prato for 0 encerra a leitura
    if peso_informado == 0:
        break

    #Se o peso do prato for negativo
    elif peso_informado < 0:
        print("Peso invalido, ele não será contabilizado, insira novamete")

    else:
        #Soma o peso informado e incrementa a quantidade de pratos lidos
        pesos_acumulados+= peso_informado
        quantidade_de_pratos+=1

        #Se o prato pesa mais que 800 gramas
        if peso_informado > 800 :
            pratos_maiores_800+=1


#Calcula a média dos pesos
media_pesos =  pesos_acumulados/quantidade_de_pratos
#Imprime a média dos pesos
print("A média dos pesos dos pratos é de:", media_pesos )
print("Um total de ", pratos_maiores_800, " pratos possuem mais que 800 gramas")
'''

'''AULA 5 Fibonacci
print("Série de Fibonacci")

atual = 0
anterior = 1
serie = 0
for i in range (1,21):
    serie = atual + anterior
    anterior = atual
    atual = serie
    print("Termo ",i, " = ",atual)
'''

desejado = int (input("Digite o numero do fatorial"))
fatorial = 1

for i in range (desejado,0,-1):
    fatorial *= i

print(fatorial)

