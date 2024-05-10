"""
TWEET 140 Caracteres

"""

T = ''
while True:
  
  T = input()
  if len(T) <= 140:
    T = 'TWEET'
    break
  else:
    T = 'MUTE'
    break

    ''' 
    TODO Ler a variável de entrada e verificar se ela possui mais ou menos que 140 caracteres.
    Se for maior imprima "MUTE" e se for igual ou menor imprima "TWEET".
    '''
print(T)







