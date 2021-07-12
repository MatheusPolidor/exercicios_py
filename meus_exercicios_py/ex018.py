from math import cos, sin, tan, radians
print('{:=^100}'.format(' DESAFIO 18 '))
ang = float(input('\nDigite um angulo para saber seu seno cosseno e tangente! '))
print('\nCom base no angulo {:.2f}° temos:\n\n{:.<10}{:.>10.2f}\n{:.<10}{:.>10.2f}\n{:.<10}{:.>10.2f}\n'.format(ang, 'Seno', sin(radians(ang)), 'Cosseno', cos(radians(ang)), 'Tangente', tan(radians(ang))))
print('{:=^100}'.format(' FIM DESAFIO 18 '))
