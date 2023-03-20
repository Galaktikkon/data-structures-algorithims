# INSERTION SORT

def insertionSort(A):
    
    n=len(A)
    
    for i in range(n):
        
        j=i # miejsce gdzie jestesmy w tablicy
        
        while j>0 and A[j]<A[j-1]:
            # sortujemy rosnaco, wiec dopoki nasz element, ktory chcemy wstawic jest mniejszy to zamieniamy miejscami 
            A[j],A[j-1]=A[j-1],A[j]
            j-=1
        # i startujemy od kolejnego elementu, ktory nalezy rozwazyc w wstawianiu
    
    return A

A=[1,3,2,5,8,4,0,7,9,2,-1]
# print(insertionSort(A))



# def insert(alist, index, n):
#         #code here
#         i=index
#         while i>0 and alist[i]<alist[i-1]:
#             alist[i],alist[i-1]=alist[i-1],alist[i]
#             i-=1

# insert(A,4,4)

# print(A)

# def insertionSort(alist, n):
    
#     for i in range(1,n):
#         insert(alist,i,n)
    
#     return alist


