num = [2, 3, 5, 11]
num[2] = 38989898

num.append(7)
num.sort(reverse=True)

print(num)

#inserindo valor
num.insert(2, 89)
print(num)



if 38989898 in num:
    num.remove(38989898)
else:
    print('Não achei o valor ')
    
print(f'Essa lista {len(num)} elementos. ')        



###########################################

valores = []

valores.append(5)
valores.append(8)
valores.append(98)
valores.append(14)


for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}! ')
 
print('Cheguei ao final da lista. ')    

print()
############################


for i in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} o valor {v}:! ')

print('Cheguei  ao final  da lista')

