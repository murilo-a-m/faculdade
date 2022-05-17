caracteres_por_pagina = 1000 # Determina os caracteres por pagina para o calculo

#Reaiza a leitura de quantos caracteres por minuto o "Mister Digitação" consegue digitar
while True:
    #Leitura do valor informado de caracteres por minuto
    caracteres_por_minuto =  int(input("Informe quantos caracteres digitados são em 1 minuto:"))

    #Verifica se o valor informado e valido
    if caracteres_por_minuto> 0 :
        break

    #Caso invalido informa ao usuario
    else:
        print("Valor de caracteres informado inválido")

#Calcula o valor de caracteres em uma hora com base no valor em minutos
caracteres_por_hora =  caracteres_por_minuto * 60

#Calcula quantas paginas por hora com base nos caracteres por hora
paginas_por_hora  = caracteres_por_hora / caracteres_por_pagina

#Imprime o valor de paginas por hora calculado
print("O Mister Digitação digita:", paginas_por_hora , "páginas por hora")


