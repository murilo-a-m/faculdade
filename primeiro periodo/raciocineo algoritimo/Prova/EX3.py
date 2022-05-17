numero_de_parcelas = 3 # Determina o numero de parcelas para o calculo

#Leitura de um valor válido para o produto
while True:

    #Le o valor do usuário
    valor_produto = float(input("Informe o valor do produto:"))

    #Verifica se o mesmo é valido
    if valor_produto >0:
        #Encerra o laco de leitura do valor
        break
    #Caso não seja válido
    else:
        #Informa ao usuario que não é valido
        print("O valor", valor_produto, "não é válido!!!")

#Calcula o valor da parcela com base no valor do produto
valor_parcela = valor_produto/numero_de_parcelas

#Imprime o valor da parcela calculado
print("O valor da cada parcela deve ser", valor_parcela," reais")
