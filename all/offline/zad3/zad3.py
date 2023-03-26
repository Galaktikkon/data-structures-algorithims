from zad3testy import runtests

def strong_string(T):
    # tu prosze wpisac wlasna implementacje
    
    curr_count=0
    max_count=0
    
    for i in range(len(T)):
        
        curr_count=0
        for j in range(len(T)):
            if T[i]==T[j] or T[i]==T[j][::-1]:
                curr_count+=1
        if curr_count>len(T)//2:
            return curr_count
        max_count=max(curr_count,max_count)
        
    return max_count

# T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]

# print(strong_string(T))
# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=False )
