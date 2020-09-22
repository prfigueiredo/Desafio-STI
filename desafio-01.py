#!/usr/bin/env python3

import central
from central import opcoes
import sys


# Inicio

matricula = input("Digite sua matricula: ")


# Verificando informacoes do usuario

reader = central.Ler("dados/alunos.csv")
listaAluno = reader.lookup(matricula, 1)


if not listaAluno:
    
    print("A matrícula informada não existe.")
    sys.exit('ERRO: Valor inválido')


elif listaAluno[-1] == "Inativo":

    print('Apenas alunos ativos podem criar um UFFMail')
    sys.exit('ERRO: Aluno inativo')
    
else:

    criadorEmail = central.Mailer(listaAluno[0],matricula)
    opEmail = criadorEmail.solicitarEmail()

    opcoes(listaAluno[0], opEmail)

    opcao = int(input())

    while opcao <= 0 or opcao >= 6:
        print (opcao,' não é um numero válido ')
        opcoes(listaAluno[0], opEmail)
        opcao = int(input())


    print("A criação de seu e-mail ",opEmail[opcao-1],
          " será feita nos próximos minutos. Um SMS foi enviado para",
          listaAluno[2]," com a sua senha de acesso.")
