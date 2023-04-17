import random

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)
print(f'd1: {d1}')
print(f'd2: {d2}')
print(f'd3: {d3}')
if (d1 > d2) and (d1 > d3):
    print('O valor do dado 1 é, ' + str(d1) + ', que é maior que d2 e d3')

elif (d2 > d1) and (d2 > d3):
    print('O valor do dado 2 é, ' + str(d2) + ', que é maior que d1 e d3')

elif (d3 > d1) and (d3 > d2):
    print('O valor do dado 3 é, ' + str(d3) + ', que é maior que d1 e d3')

elif (d1 == d2) and (d1 == d3) and (d2 == 3):
    print('os valores são iguais')
else:
    print('dois valores são iguais')
