def commonElements (A, B, C, n1, n2, n3):
        # your code here
        common=[]
        i,j,k=0,0,0
        n=max(n1,n2,n3)
        while i<n or j<n or k<n:
            print(i,j,k)
            if i==n1-1 and j==n2-1 and k==n3-1:
                break
            if i==n1-1 and j<n2-1 and k<n3-1:
                mi=min(B[j],C[k])
            elif j==n2-1 and i<n1-1 and k<n3-1:
                mi=min(A[i],C[k])
            elif k==n3-1 and i<n1-1 and j<n2-1:
                mi=min(A[i],B[j])
            elif i<n1-1 and j<n2-1 and k<n3-1:
                mi=min(A[i],B[j],C[k])
            if A[i]==B[j]==C[k]:
                common.append(A[i])
                if i<n1-1:
                    i+=1
                if j<n2-1:
                    j+=1
                if k<n3-1:
                    k+=1
            else:
                if mi==A[i]:
                    i+=1
                elif mi==B[j]:
                    j+=1
                elif mi==C[k]:
                    k+=1
        return common

# n1 = 6
# A = [1, 5, 10, 20, 40, 80]
# n2 = 5 
# B = [6, 7, 20, 80, 100]
# n3 = 8
# C = [3, 4, 15, 20, 30, 70, 80, 120]

n1=3
n2=3
n3=3
A=[1, 2, 3]
B=[4, 5, 6]
C=[7, 8, 9]

print(commonElements(A,B,C,n1,n2,n3))