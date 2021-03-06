
mod = int(1e9)+7




C = [[0 for x in range(5000+1)] for x in range(5000+1)]
# A Dynamic Programming based Python Program that uses table C[][]
# to calculate the Binomial Coefficient

# Returns value of Binomial Coefficient C(n, k)
def nCr():


	# Calculate value of Binomial Coefficient in bottom up manner
	for i in range(5001):
		for j in range(min(i, 5000)+1):
			# Base Cases
			if j == 0 or j == i:
				C[i][j] = 1

			# Calculate value using previosly stored values
			else:
				C[i][j] = (C[i-1][j-1] % 1000000006+ C[i-1][j] % 1000000006)% 1000000006

nCr()
T = int(input())

def modInv(a,m=1000000007):
    m0=m
    y=0
    x=1
    if m==1:
        return 0
    while (a>1):
        q=a//m
        t=m
        m=a%m
        a=t
        t=y
        y=x-q*y
        x=t

    if (x<0):
        x+=m0
    return x


def modDivide(a,b,m=1000000007):
    a=a%m
    inv=modInv(b,m)
    return (inv*a)%m





def power(x, y, p) :
    res = 1     # Initialize result


    x = x % p

    while (y > 0) :

        if ((y & 1) == 1) :
            res = (res * x) % p


        y = y >> 1      # y = y/2
        x = (x * x) % p

    return res % p

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
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

#def table():



for test_case in range(T):

    N,K=map(int,input().split())

    seq = list(map(int,input().split()))

    quickSort(seq,0,N-1)


    prod=1
    a=C[N-1][K-1]
    for i in range(0,N):

        c=0
        b=0
        if ((N-i-1)>=(K-1)):
            b= C[N-i-1][K-1]

        if i>=(K-1) :
            c = C[i][K-1]

        #print(str(i+1)+" "+str(a)+" "+str(b)+" "+str(c))
        a1=power(seq[i],a , mod)
        a2=power(seq[i],(b+c)%1000000006 , mod)
        ans=modDivide(a1,a2,1000000007)

        prod=((prod %mod) * (ans % mod))%mod

    print(prod)
