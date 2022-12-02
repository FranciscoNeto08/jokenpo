from random import randint 
from time import sleep


itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Suas opções: [0]Pedra, [1]Papel, [2]Tesoura')
jogador = int(input('Qual é a sua escolha?'))
print('O jogador escolheu {}'. format(itens[jogador]))

print('=-'*14)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')

print('=-'*14)

print('O computador escolheu {}'. format(itens[computador]))

print('=-'*14)

if computador == 0: #computador escolhe pedra
  if jogador == 0:
   print('!!! EMPATE !!!')
  elif jogador == 1:
   print('!!! JOGADOR VENCE !!!') 
  elif jogador == 2:
   print('!!! COMPUTADOR VENCE !!!')
  else:
   print('!!! JOGADA INVALIDA !!!')

if computador == 1: #computador escolhe papel
  if jogador == 0:
    print('!!! JOGADOR VENCE !!!')
  elif jogador == 1:
    print('!!! EMPATE !!!')
  elif jogador == 2:
    print('!!! COMPUTADOR VENCE !!!')
  else: 
    print('JOGADA INVALIDA')

if computador == 2:
  if jogador == 0:
    print('!!! COMPUTADOR VENCE !!!')
  elif jogador == 1:
    print('!!! JOGADOR VENCE !!!')
  elif jogador == 2:
    print('!!! EMPATE !!!')
  else:
    print('JOGADA INVALIDA')
  

