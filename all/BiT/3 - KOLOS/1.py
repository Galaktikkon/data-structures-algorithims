def convert(num):
    
    C=[0 for _ in range(10)]
    
    while num !=0:
        C[num%10]+=1
        num//=10
    multi,single=0,0
    
    for i in C:
        if i>1:
            multi+=1
        elif i==1:
            single+=1
    
    return (single,multi)

def countingSort(A,T,k,type):
    n=len(A)
    C=[0 for _ in range(10)]
    B=[0]*n
    for i in range(n):              
        C[A[i][k]]+=1
    if type==1:      
        for i in range(1,10):          
            C[i]+=C[i-1]        
        for i in range(n-1,-1,-1):       
            B[C[A[i][k]]-1]=T[i]           
            C[A[i][k]]-=1
    elif type==0:
        for i in range(8,-1,-1):          
            C[i]+=C[i+1]  
        for i in range(n):       
            B[C[A[i][k]]-1]=T[i]           
            C[A[i][k]]-=1
    return B    

def prettySort(T):
    
    B=[]
    
    for el in T:
        B.append(convert(el))
        
    T=countingSort(B,T,0,0)
    T=countingSort(B,T,1,1)
    
    return T

T=[123,445,28,22,4456]

print(prettySort(T))
