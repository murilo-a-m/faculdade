#Classe preposição
import numpy as np

class Propositon:

    #Construtor da classe preposição
    def __init__(self, proposition):
        self.__proposition = proposition               #preposição (formula) do objeto preposição
        self.__variables = []                          #Lista com as variáveis da fórmula

        self.__list_variables(self.__proposition)      #Chama a funcao para listar as variáveis da proposicao
        
        #Variáveis controle da tabela verdade
        self.__truthtable = []                         #Tabela verdade propriamente dita
        self.__order = 2**len(self.__variables)        #Define o grau da tabela verdade


    #Setter para a fórmula que constroi a preposição
    def set_proposition(self,proposition):
        self.__proposition = proposition
        self.__list_variables(self.__proposition)

    #Propriedade para retorno do valor da preposição 
    @property
    def proposition(self):
        return self.__proposition

    #Método para retornar a lista de variáveis da proposição
    @property
    def variables(self):
        return self.__variables

    #Método para listar as variáveis da preposicao atual
    def __list_variables(self,proposition):
        self.__variables = []
        #Para cada caracter na string da preposicao
        for element in (proposition):
            #Se ele é alpha e ainda nao está na lista
            if (element.isalpha()) and element not in(self.__variables):
                self.__variables.append(element)
        
        self.__order = 2**len(self.__variables)        #Define o grau da tabela verdade

    #Método para calcular o resultado da tabela verdade
    def calc(self):            
        self.__build_truth_table()

    #Método para construir a tabela verdade
    def __build_truth_table(self):
        #Para cada variavel da preposicao cria uma coluna para a tabela verdade e suas operações
        for character in (self.__proposition):
            if character != ' ' and character.isalpha() :
                line = [character]
                #Cria linha de acordo com a ordem da tabela
                for i in range(self.__order):
                    line.append(False)

                self.__truthtable.append(line)

        for colum in self.__truthtable:

            if colum[0].isalpha():
                if self.__variables.index(colum[0])  == 0: 
                    for item in range (0,int(self.__order/2)):
                        colum[item+1]=True

                else:
                    sequence = 


        print(np.array(self.__truthtable).T)

equacao = Propositon("pqrstu")
equacao.calc()