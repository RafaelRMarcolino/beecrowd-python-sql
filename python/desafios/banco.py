nome = input('Digite seu nome ')
saldo = 1000000

sair = True
while sair != False:
    
    case = int(input('Sacar(1), Depositar(2), extrato(3), sair(4)'))
    if case == 1:
        sub = int(input('Quanto deseja sacar ?'))
        saldo -= sub

    elif case == 2:
        sum = int(input('Quanto deseja sacar ?'))
        saldo += sum

    elif case == 3:
        print('{nome} seu saldo é {saldo}\n')
    
    elif case == 4:
        print(f'{nome} seu saldo é {saldo}\n')
        sair = True
        break

    else:
        continue

    print(f'{nome} seu saldo é {saldo}\n')

print('Obrigado por usar nosso banco')