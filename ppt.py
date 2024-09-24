'''
Jogo do Pedra-Papel-Tesoura
2024/08/13
Joice Martins
'''

# Bibliotecas
from modules import clrScreen, displayHeader, getUserOption, validateUserOption, displayLine, displayMsg, displayMsgCenter, displayHeaderT
from random import randint
from time import sleep

# Constantes, Variáveis e Listas
msgsInicio = ['Seja Bem Vindo ao',
              'Jogo do PEDRA-PAPEL-TESOURA',
              'desenvolvido por: Joice Martins',
              'BOA SORTE!'] # mensagem que vai ser mostrada no inicio do jogo
msgs = []
playAgain = ''
playerScore = 0
computerScore = 0

# Funções
def startPPT(): # Funcao para iniciar o jogo
  while(True): 
    clrScreen() # Linha de caracteres
    displayHeader(msgsInicio)
    playPPT()
    playAgain = getUserOption('Deseja jogar novamente [s/n]')
    while not validateUserOption(playAgain, ['s', 'n', 'S', 'N']):
      playAgain = getUserOption('Deseja jogar novamente [s/n]')
    if playAgain.lower() != 's':
      break

def displayMenu():
  msgs = ['escolha: ', '[0] --> Pedra','[1] --> Papel','[2] --> Tesoura']
  displayLine()
  for msg in msgs:
    displayMsg(msg)
  displayLine()

def displayScore(typeScore, playerScore, computerScore):
  msgs = []
  msgs.append(typeScore)
  msgs.append(f'Player: {playerScore} --- PC: {computerScore}')
  displayHeaderT(msgs)
  
def determineWinner(playerChoice, computerChoice):
  play = ''
  result = ''
  choices = ['PEDRA', 'PAPEL', 'TESOURA']
  playerChoiceStr = choices[int(playerChoice)]
  computerChoiceStr = choices[int(computerChoice)]
  if playerChoice == computerChoice:
    result = 'Empate!'
  elif (playerChoice == '0' and computerChoice == '2', playerChoice == '1'and computerChoice == '0', playerChoice == '2' and computerChoice == '1'):
    play = f'{playerChoiceStr} vence {computerChoiceStr}'
    result = 'Você Ganhou'
  else:
    play = f"{computerChoiceStr} vence {playerChoiceStr}"
    result = 'Você Perdeu'
  msgs = ['Jogada do player: ' + playerChoiceStr,
       'Jogada do PC: ' + computerChoiceStr,
       play, result]
  displayHeaderT(msgs)
  return result

def playPPT():
  playerScore = 0
  computerScore = 0
  while playerScore < 2 and computerScore < 2:
    displayMenu()
    playerChoice = getUserOption('Sua escolha ')
    while not validateUserOption(playerChoice, ['0', '1', '2']):
      displayMenu()
      playerChoice = getUserOption('Sua escolha')
    computerChoice = str(randint(0,2))
    result = determineWinner(playerChoice, computerChoice)
    if 'Ganhou' in result:
      playerScore += 1
    elif 'Perdeu' in result:
      computerScore += 1
    if playerScore < 2 and computerScore < 2:
      displayScore('PLACAR', playerScore, computerScore)
    sleep(1)
  displayScore('PLACAR FINAL', playerScore, computerScore)
  if playerScore > computerScore:
    displayHeader(['Parabéns', 'YOU WIN!'])
  else:
    displayHeader(['Parabéns', 'YOU LOSE!'])
    
# Main