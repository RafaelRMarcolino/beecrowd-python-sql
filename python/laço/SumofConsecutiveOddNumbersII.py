#Read an integer N that is the number of test cases. Each test case is a line 
# containing two integer numbers X and Y. Print the sum of all odd values between them,
# not including X and Y.

#Input
#The first line of input is an integer N that is the number of test cases 
# that follow. Each test case is a line containing two integer X and Y.

#Output
#Print the sum of all odd numbers between X and Y.

N = int(input())
s1 = 0
s2 = 0

for i in range(0, N):
    print('I {}'.format(i) ) 
    n1, n2 = list(map(int, input().split()))
    
    if n1 %2==0:
        s1 += n1
        print('s1 {} é par'.format(s1))
    
        
    if n2 %2==0:
        print('s2 {} é par'.format(s2))
         

