
        # code here
        n=len(arr)
        while i<n-1:
            # print(i)
            currMin=i
            j=i+1
            while j<n:
                if arr[currMin]>arr[j]:
                    currMin=j
                j+=1
                print(arr[currMin])
            i+=1