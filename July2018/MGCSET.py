import math

T = int(input())

for test_case in range(T):
    n,m=map(int,input().split())
    seq = list(map(int,input().split()))
    count=0
    for i in seq:
        if i% m==0:
            count+=1

    print(int(math.pow(2,count)-1))       
