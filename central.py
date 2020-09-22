# Importar tabela CSV:

import csv

class Ler:

    def __init__(self, tabela):
        self.tabela = tabela

    def lookup(self,info, dado):
        with open(self.tabela,'r') as csvfile:
            lookup = csv.reader(csvfile)
            for linha in lookup:
                if linha[dado] == info:
                    csvfile.close
                    return linha
        return []


class Escrever:
    def __init__(self, tabela):
        self.tabela = tabela
        
# E-mail:

class Mailer:

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        

    def solicitarEmail(self):
        criar = Criador(self.nome)
        listOp = criar.opcoes()
        return listOp

    def criarEmail(self, tabela, email, matricula):
        pass

class Criador:

    def __init__(self, nome):
        self.nome = nome.lower()
        self.mail = "@id.uff.br"

    def opcoes(self):

        namelist = self.nome.split()
        op1 = namelist[0]+'_'+namelist[1]+self.mail
        op2 = namelist[0]+namelist[1][0]+namelist[2][0]+self.mail
        op3 = namelist[0]+namelist[2]+self.mail
        op4 = namelist[0][0]+namelist[2]+self.mail
        op5 = namelist[0][0]+namelist[1]+namelist[2]+self.mail
        return [op1,op2,op3,op4,op5]

def opcoes(nome, listaOp):
    print(nome,', por favor escolha uma das opções abaixo para o seu UFFMail')
    contador = 1
    for op in listaOp:
        print(contador,' - ',op)
        contador += 1