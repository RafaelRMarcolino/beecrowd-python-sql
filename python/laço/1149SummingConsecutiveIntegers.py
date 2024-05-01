"""
Write an algorithm to read a value A and a value N. Print the sum of N numbers
from A (inclusive). While N is negative or ZERO, a new N (only N) must be read. 
All input values are in the same line.

Input
The input contains only integer values, ​​can be positive or negative.

Output
The output contains only an integer value.

"""

valores =  input().split()

a = int(valores[0])
ultimo_valor = len(valores) - 1
n = int(valores[ultimo_valor])

soma = 0

for i in range(0, n):
    soma += a + i
    
print(soma)    

