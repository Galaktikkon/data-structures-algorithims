
def nextGreaterElement(nums1, nums2):
    I = {}
    n = len(nums1)
    m = len(nums2)

    # for i in range(n):
    #     I[nums2[i]] = i
    # print(I)

    stack = []
    i = 0
    while i < m:

        while len(stack) > 0 and nums2[i] > stack[len(stack)-1]:

            I[stack.pop()] = nums2[i]

        stack.append(nums2[i])

        i += 1
        print(stack)

    sol = [I[nums1[i]] if nums1[i] in I else -1 for i in range(n)]

    print(sol)


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]

nums1 = [1, 3, 5, 2, 4]
nums2 = [6, 5, 4, 3, 2, 1, 7]

nextGreaterElement(nums1, nums2)


def nextLargerElement(arr, n):
    sol = [-1 for i in range(n)]
    stack = [0]
    for i in range(n):

        while len(stack) > 0 and arr[i] > arr[stack[-1]]:

            sol[stack.pop()] = arr[i]

        stack.append(i)

    return sol


n = 4
arr = [1, 3, 2, 4]

print(nextLargerElement(arr, n))
