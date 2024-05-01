"""
Faça um programa que leia 5 valores numericos e guarde os em uma lista 

No final mostra qual foi o maior valor dogotado em sua poisção
"""

lista = []

for i in range(0, 5):
    lista.append(int(input(' Digite valor ')))

for c, v in enumerate(lista):
    print(f'{c} e {v} ')    
    
    ##28:18
    ## https://www.youtube.com/watch?v=N1hTsbW50eM



