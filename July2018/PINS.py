
import math
T = int(input())

for test_case in range(T):
    N = int(input())
    half = N - math.ceil(N/2)
    print(str(1)+" "+str(10**half))
