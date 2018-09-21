import operator
import sys

T = int(input())

for test_case in range(T):
    N,A,B = map(int,input().split())
    A_temp=A
    df=[]
    freq={}
    for i in range(N):
        temp=list(map(int,input().split(' ')))
        df.append(temp)
        freq[i+1]=temp.count(1)
        temp=[]

    sorted_x = sorted(freq.items(), key=operator.itemgetter(1))

    buy={}
    total=0
    remaining=N
    index=N-1
    bought_num=0
    for i in range(N-1,-1,-1):
        total+=sorted_x[i][1]

        if total<=N and sorted_x[i][1] >0:
            buy[sorted_x[i][0]] = sorted_x[i][1]
            bought_num+=sorted_x[i][1]
            remaining=N-bought_num
            index=i
        else:
            buy[sorted_x[i][0]] = remaining
            bought_num+=remaining
            remaining=N-bought_num
            index=i
            break
    if bought_num == N:
        for i in range(index-1,-1,-1):
            buy[sorted_x[i][0]]=0
    else:
        remaining=N-bought_num
        for i in range(index-1,-1,-1):
            buy[sorted_x[i][0]]=remaining
            bought_num+=remaining
            remaining=N-bought_num

    buy={}
    for i in range(0,5):
        buy[i+1] = 0
    for i in range(5,11):
        buy[i+1]=  3
    for  i in range(11,N):
        buy[i+1]=int((N-18)/(N-11))

    sorted_y = sorted(buy.items(), key=operator.itemgetter(0))

    player=[]
    for i in range(N):
        print(sorted_y[i][1],end=' ',flush=False)
        player.append(sorted_y[i][1])
    print('')
    sys.stdout.flush()


    taran=list(map(int,input().split(' ')))

    times=N/(A+B)
    while times:
        my=[]
        your=[]
        c=0
        loop=0
        while  loop <A and A!=0 and c<=N-1:

            j=sorted_x[N-c-1][0]-1
            while player[j]==0 and c<=N-1:
                j=sorted_x[N-c-1][0]-1
                c+=1
            k=0
            while k <N :

                if df[j][k] ==1 and (taran[k]!=0 and player[j] !=0):
                    if A !=0:

                        my.append(j+1)
                        your.append(k+1)
                        A-=1
                        taran[k]-=1
                        player[j]-=1

                    else:
                        break

                    if taran[k] ==0 or player[j]==0:
                        k+=1
                else:
                    k+=1
            loop+=1
            c+=1


        loop=0
        c=0
        while  loop <A and A!=0 and c<=N-1:

            j=sorted_x[N-c-1][0]-1
            while player[j]==0 and c<=N-1:
                j=sorted_x[N-c-1][0]-1
                c+=1
            k=0
            while k <N :

                if (df[j][k] ==0 or df[j][k]==1) and (taran[k]!=0 and player[j] !=0):

                    if A !=0:

                        my.append(j+1)
                        your.append(k+1)
                        A-=1
                        taran[k]-=1
                        player[j]-=1
                    else:
                        break

                    if taran[k] ==0 or player[j]==0:

                        k+=1

                else:

                    k+=1
            loop+=1
            c+=1



        #sys.stdout.flush()
        if (len(my) !=A_temp):
            needed=A_temp-len(my)
            for x in range(needed):
                get_in=next(q[0] for q in enumerate(player) if q[1] > 0)

                my.append(get_in+1)
                player[get_in]-=1

                get_in=next(q[0] for q in enumerate(taran) if q[1] > 0)

                your.append(get_in+1)
                taran[get_in]-=1


        fixure_chef=[]
        fixure_chef = list(zip(my, your))


        for i in range(A_temp):
             print(fixure_chef[i][0],end=' ',flush=False)
             print(fixure_chef[i][1],end='',flush=False)
             print('')
             checker=i
             sys.stdout.flush()

        for i in range(B):
            fixture_taranA,fixture_taranB= map(int,input().split(' '))
        times-=1
