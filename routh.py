import numpy as np

deg = input("enter degree of characteristic polynomial:" )
deg = int(deg)

n = deg +1
epsilon = pow(10, -10)

table = np.zeros((n,n))
for i in range(n):
    message = 'enter coefficient of power ' + str(n-i-1) + " :"
    temp_input = input(message)
    table[i%2, (i)//2] = temp_input
    
if any(table[1,:])==False:
        table[1,:]=[table[0, j]*(n-1-2*j) for j in range(n)]
        
if table[1,0]==0:
    table[1,0]=epsilon
    
for i in range(2,n):
    j= 0
    
    for j in range(n-1):
        table[i,j] = table[i-2, j+1]-(table[i-2, 0]*table[i-1,j+1])/table[i-1, 0]
    if any(table[i,:])==False:
        table[i,:]=[table[i-1, j]*(n-i-2*j) for j in range(n)]
    
    if table[i, 0]==0:
        table[i,0]=epsilon
print()
print("no of roots strictly on right hand side plane = ")
changes = 0
for i in range(1,n):
    if table[i-1, 0]*table[i,0]<0:changes+=1
print(changes)


    

