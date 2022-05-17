#TDE-2 Desenvolvido por - Murilo Analiel Machado

parciais = [] #Lista de notas parciais
pesos = [] #Pesos das notas
notas = [] #Notas divididas pelos seus pesos
nota_final = 0.0 #Nota final a sem calculada

print("Calculadora média ponderada")
print("Será necessário infomar quantas notas parciais deseja inserir e os repectivos valores de notas e pesos\n\n")

while True:
    #Coleta do usuário a quantidade de notas que necessita calcular
    qtd_notas = int(input("Informe a quantidade de notas que deseja inserir:"))

    #Coleta do usuário as notas e os pesos:
    for i in range (0,qtd_notas):
        parciais.append(float(input("Informe a {}º nota:".format(i+1))))
        pesos.append(float(input("Informe o {}º peso em porcentagem %:".format(i+1))))
        notas.append(parciais[i]/pesos[i])

    #Realiza o calculo da média ponderada
    for i in range (0,qtd_notas):
        nota_final += parciais[i] * pesos[i]

    nota_final = nota_final/sum(pesos)   


    #Retorna a nota final para o usuário
    print("Sua nota final é/:{}\n".format(nota_final))

    continuar_processo = str(input("Deseja realizar outra operação? [N] para não e Enter para continuar"))
    continuar_processo = continuar_processo.upper()

    if continuar_processo =='N':
        break
            


