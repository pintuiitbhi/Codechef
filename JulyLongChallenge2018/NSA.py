
T = int(input())

def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low , high):

        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


import numpy as np

# Python Program to find
# prefix sum of 2d array
#R = 4
#C = 5

# calculating new array
def prefixSum2D(a,R,C) :
    #global C, R
    psa = [[0 for x in range(C)]
              for y in range(R)]
    psa[0][0] = a[0][0]

    # Filling first row
    # and first column
    for i in range(1, C) :
        psa[0][i] = (psa[0][i - 1] +
                       a[0][i])
    for i in range(0, R) :
        psa[i][0] = (psa[i - 1][0] +
                       a[i][0])

    # updating the values in
    # the cells as per the
    # general formula
    for i in range(1, R) :
        for j in range(1, C) :

            # values in the cells of
            # new array are updated
            psa[i][j] = (psa[i - 1][j] +
                         psa[i][j - 1] -
                         psa[i - 1][j - 1] +
                           a[i][j])

    # # displaying the values
    # # of the new array
    # for i in range(0, R) :
    #     for j in range(0, C) :
    #         print (psa[i][j],
    #                end = " ")
    #     print ()

    return psa


for test_case in range(T):
    S = input()
    #l=[ord(c) for c in S]
    N=len(S)
    #quickSort(l,0,N-1)

    matrix=np.zeros([26,N],dtype=int)
    for i in range(N):
        matrix[ord(S[i])-97][i]=1
    prefix_sum=prefixSum2D(matrix,26,N)

    for k in range(N):
        
        for i in range(1, R) :
            for j in range(1, C) :

                # values in the cells of
                # new array are updated
                psa[i][j] = (psa[i - 1][j] +
                             psa[i][j - 1] -
                             psa[i - 1][j - 1] +
                               a[i][j])
    print(matrix)
    print(prefix_sum)
