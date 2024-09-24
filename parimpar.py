'''
Jogo do Ímpar ou Par
2024/08/20
Joice Martins
'''

# Bibliotecas
from modules import clrScreen, displayHeader, getUserOption, validateUserOption, displayLine, displayMsg, displayMsgCenter, displayHeaderT
from random import randint
from time import sleep

# Constantes, Variáveis e Listas
msgsInicio = ['Seja Bem Vindo ao',
              'Jogo do ÍMPAR OU PAR',
              'desenvolvido por: Joice Martins',
              'BOA SORTE!'] # mensagem que vai ser mostrada no inicio do jogo
playAgain = '' # para jogar de novo
playerScore = 0 # pontuacao do usuario
computerScore = 0 # pontuacao do computador

# Funções
def startIOP(): # Função para iniciar o jogo
    while(True): # 
        clrScreen() # Limpar a tela
        displayHeader(msgsInicio) # mensagem de inicio
        playIOP() # chama a funcao para iniciar o jogo
        playAgain = getUserOption('Deseja jogar novamente [s/n]') # pergunta se deseja jogar dnv
        while not validateUserOption(playAgain, ['s', 'n', 'S', 'N']): # respostas validas
            playAgain = getUserOption('Deseja jogar novamente [s/n]') # se resposta for invalida pergunta dnv 
        if playAgain.lower() != 's': # se resposta for sim
            break # para a funcao

def displayMenu(): # funcao para a escolha do usuario
    msgs = ['Escolha sua opção:', '[0] --> Ímpar', '[1] --> Par'] # escolha do usuario
    displayLine() # linha de caracteres
    for msg in msgs: # enquanto houver mensagens dentro de mensagens
        displayMsg(msg) # mensagem do jogo
    displayLine() # linha de caracteres

def displayScore(typeScore, playerScore, computerScore): # pontuacao do jogo
    msgs = [] # lista de mensagens
    msgs.append(typeScore) # apeend == adiciona novos elementos a lista
    msgs.append(f'Player: {playerScore} --- PC: {computerScore}') # mostra na tela a pontuacao
    displayHeaderT(msgs) 

def determineWinner(playerChoice, playerNumero, computerNumero): 
    play = '' # inicio
    result = '' # resultado
    choices = ['ÍMPAR', 'PAR'] # escolha do par ou impar
    playerChoiceStr = choices[int(playerChoice)] 

    total = playerNumero + computerNumero # a soma da escolha de ambas as respostas
    resultado = 'PAR' if total % 2 == 0 else 'ÍMPAR' # calcular para saber se o resultado é impar ou par

    if resultado.lower() == playerChoiceStr.lower(): # resultado
        result = 'Você Ganhou' # Se voce ganhar
    else:
        result = 'Você Perdeu' # Se voce perder

    msgs = [f'Sua escolha: {playerChoiceStr}', 
            f'Seu número: {playerNumero}',
            f'Número do PC: {computerNumero}',
            f'Total: {total} ({resultado})',
            result] # lista de mnsgs
    displayHeaderT(msgs)
    return result # retorna ao resultado

def playIOP(): # começa o jogo impar ou par
    playerScore = 0 # pontuacao do usuario
    computerScore = 0 # pontuacao do computador
    while playerScore < 2 and computerScore < 2: # enquanto a pontuacao for dois
        displayMenu() # funcao para escolha do numero
        playerChoice = getUserOption('Sua escolha ') # escolha do usuario
        while not validateUserOption(playerChoice, ['0', '1']): # enquanto as respostas nao sao validas
            displayMenu() # retorna para a funcao de escolha
            playerChoice = getUserOption('Sua escolha') # escolha

        playerNumero = int(getUserOption('Escolha um número de 0 a 10: ')) # usuario escolhe u numero de 1 a 10
        computerNumero = randint(0, 10) # opcoes validas q o vomputador pode escolha

        result = determineWinner(playerChoice, playerNumero, computerNumero) # resultado

        if 'Ganhou' in result: # se o usuario ganhar
            playerScore += 1 # some 1 a pontuacao
        elif 'Perdeu' in result: # se o computador ganhar
            computerScore += 1 # some 1 a pontuacao

        if playerScore < 2 and computerScore < 2: # se a pontuacao
            displayScore('PLACAR', playerScore, computerScore) # placar
        sleep(1) # espere um segundo

    displayScore('PLACAR FINAL', playerScore, computerScore)
    if playerScore > computerScore: # se o usuario ganhar vai aparecer essa mensagem
        displayHeader(['Parabéns', 'YOU WIN!']) # mensagem
    else: # Se voce perdeu ira aparecer esta mensagem
        displayHeader(['Parabéns', 'YOU LOSE!']) # mensagem

# Main
