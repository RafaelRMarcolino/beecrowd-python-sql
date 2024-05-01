N = int(input())


while(N > 0):
  
  A, B = map(str, input().split())
  
  if A.endswith(B):
      print("encaixa")
  else:
      print("nao encaixa")

