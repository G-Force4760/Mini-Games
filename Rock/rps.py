from random import choice
import datetime
from Projects.Rock import results

movimentos = ('pedra', 'papel', 'tesoura')
wr = results.ganhaste
lr = results.perdeste
dr = results.empataste
w = 0
l = 0
d = 0
cont = 'sim'
while cont == 'sim':
    op = choice(movimentos)
    pl = input('Escolha de entre: pedra, papel, tesoura. \n--> ').strip().lower()
    print('{} VS {}'.format(op, pl))

    if pl != 'pedra' and pl != 'papel' and pl != 'tesoura':
        print('Desculpe não conheço esse movimento.')
    if op == pl:
        d = d + 1
        print('Empatou.')
    if op == 'pedra' and pl == 'papel' or op == 'papel' and pl == 'tesoura' or op == 'tesoura' and pl == 'pedra':
        w = w + 1
        print('Ganhaste')
    if op == 'pedra' and pl == 'tesoura'or op == 'papel' and pl == 'pedra' or op == 'tesoura' and pl == 'papel':
        l = l + 1
        print('Perdeste')
    cont = input('Queres jogar outra vez? (sim ou não).  '.strip().lower())

wr = wr + w
lr = lr + l
dr = dr + d
p = (wr / (wr + lr + dr)) * 100
print('Nesta vez Ganhaste {}, Perdeste {} e Empataste {}.'.format(w, l, d))
print('No total Ganhaste: {}, Perdeste {} e Empataste {} \nA tua percentagem de vitórias é {:.02f}%.'.format(wr, lr, dr, p))

if p > 75:
    print('Parabéns és um ótimo jogador!')

with open('score.txt', 'a+') as file:
    today = datetime.date.today()
    file.write('Data: {} \nGanhaste: {} \nPerdeste: {} \nEmpataste: {} \n \n'.format(today, w, l, d))

with open('results.py', 'w') as file:
    file.write('ganhaste = {} \nperdeste = {} \nempataste = {}'.format(wr, lr, dr))

