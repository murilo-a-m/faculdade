
print("Sistema para calculo do tempo medio de voo para os avioes dos tipos 'pequeno' 'medio' 'grande'")

tempo_somado_aviao_pequeno = 0 #Variavel com o tempo somado das viagens do aviao pequeno
tempo_somado_aviao_medio = 0 #Variavel com o tempo somado das viagens do aviao medio
tempo_somado_aviao_grande = 0 #Variavel com o tempo somado das viagens do aviao grande

print("Avioes de pequeno porte:")
#Leitura dos 10 valores para aviões de pequeno porte
for contador in range(1,11):
    while True:
        #Leitura do valor de tempo do usuário
        print("Tempo em horas da ",contador,"º viagem do aviao de pequeno porte:")
        tempo_aviao_pequeno = float(input("Valor:"))

        #Se o valor do tempo informado é valido
        if tempo_aviao_pequeno > 0 :
            #Soma o valor do tempo
            tempo_somado_aviao_pequeno+= tempo_aviao_pequeno
            break
        #Informa ao usuário caso seja invalido
        else:
            print("Tempo em horas informado inválido")

print("Avioes de medio porte:")
#Leitura dos 10 valores para aviões de médio porte
for contador in range(1,11):
    while True:
        #Leitura do valor de tempo do usuário
        print("Tempo em horas da ",contador,"º viagem do aviao de medio porte:")
        tempo_aviao_medio = float(input("Valor:"))

        #Se o valor do tempo informado é valido
        if tempo_aviao_medio > 0 :
            #Soma o valor do tempo
            tempo_somado_aviao_medio+= tempo_aviao_medio
            break
        #Informa ao usuário caso seja invalido
        else:
            print("Tempo em horas informado inválido")

#Leitura dos 10 valores para aviões de grande porte
print("Avioes de grande porte:")
for contador in range(1,11):
    while True:
        #Leitura do valor de tempo do usuário
        print("Tempo em horas da ",contador,"º viagem do aviao de grande porte:")
        tempo_aviao_grande = float(input("Valor:"))

        #Se o valor do tempo informado é valido
        if tempo_aviao_grande > 0 :
            #Soma o valor do tempo
            tempo_somado_aviao_grande+= tempo_aviao_grande
            break
        #Informa ao usuário caso seja invalido
        else:
            print("Tempo em horas informado inválido")

#Determina o tempo médio com base no tempo somado nas 10 leituras
tempo_medio_aviao_pequeno = tempo_somado_aviao_pequeno / 10
tempo_medio_aviao_medio = tempo_somado_aviao_medio / 10
tempo_medio_aviao_grande = tempo_somado_aviao_grande / 10

#Imprime o tempo médio de cada tipo de avião
print("O tempo médio das viagens de uma aviao pequeno é de:", tempo_medio_aviao_pequeno," horas")
print("O tempo médio das viagens de uma aviao medio é de:", tempo_medio_aviao_medio," horas")
print("O tempo médio das viagens de uma aviao grande é de:", tempo_medio_aviao_grande," horas")
