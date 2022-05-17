
#Laço de leitura do valor da nota
while True:
    #Leitura do valor da nota
    nota = float(input("Informe a nota do aluno:"))

    #Se a nota é um valor valido
    if nota >= 0 and nota <= 100 :
        break
    #Se a nota não é um valor valido
    else:
        print("O valor informado para a nota é inválido")

#Se a nota é maior que 82
if nota >= 86:
    print("O conceito para a nota informada é A")

#Se a nota é maior que 61
elif nota >= 61 :
    print("O conceito para a nota informada é B")

#Se a nota é maior que 36
elif nota >= 36 :
    print("O conceito para a nota informada é C")

#Se a nota é maior que 1
elif nota >= 1 :
    print("O conceito para a nota informada é D")

#Se a nota NÃO é maior que nenhum dos outros conceitos:
else:
    print("O conceito para a nota informada é E")
