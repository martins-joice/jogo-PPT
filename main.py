'''
Projeto Jogo Pedra-Papel-Tesoura
2024/08/13
Joice Martins
'''

# --> Bibliotecas
# importa funções do arquivo modules.py
from modules import clrScreen, displayLine, displayMsg, displayMsgCenter, displayHeader, getUserOption, validateUserOption 
# importa funções do arquivo ppt.py
from ppt import startPPT
from parimpar import startIOP

# --> Constantes, Variáveis e Listas

# --> Funções

# --> Main
msgs = ['Seja Bem-vind@ aos Jogos', 'PEDRA-PAPEL-TESOURA', 'PAR OU ÍMPAR']
displayHeader(msgs) # mostra a mensagem quando inicia o jogo
msgs = ['Digite 0 --> Sair', # digite 0 para sair do jogo
        'Digite 1 --> Pedra-Papel-Tesoura',
        'Digite 2 --> Par ou Ímpar']
displayHeader(msgs)
opUser = getUserOption('Sua escolha')
while not validateUserOption(opUser, ['0','1','2']):
  opUser = getUserOption('Sua escolha')
if(opUser == '1'):
  startPPT() # Inicia o jogo
elif(opUser == '2'):
  startIOP()
else:
  displayMsgCenter('Até a Próxima...')