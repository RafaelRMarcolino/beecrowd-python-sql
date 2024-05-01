
i = True

j=1

while i:
    x = int(input())
    
    if x == 0:
        break
    
    j = 1
    while j <= x:
        if j ==x:
            print('%d'%(j),end="\n")
        
        else:
            print('%d'%(j),end=" ")    
    
        j+=1
