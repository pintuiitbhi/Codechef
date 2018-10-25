#include <bits/stdc++.h>
using namespace std;

vector <int> sievePrime(int n){
  bool prime[n+1];
  memset (prime, true, sizeof(prime));

  for (int i=2;i*i<=n;i++){
    if(prime[i]==true){
      for(int j=i*2;j<=n;j=j+i)
      prime[j]=false;
    }
  }

  vector <int> primeN;
  for(int i=2;i<=n;i++){
    if(prime[i])
    primeN.push_back(i);
    // printf("%d ",i);
  }
  // printf("\n");
  // primeN.push_back(i);
  return primeN;
}

int semiPrime(int x){
  vector <int> primeN = sievePrime(x);
  int flag=0;
  for(int i=0;i<primeN.size();i++){
    if(x%primeN[i]==0){
      int q=x/primeN[i];
      flag=0;
      for(int j=0;j<primeN.size();j++){
        if(q==primeN[j] && q!=primeN[i]){
          flag=1;
          break;
        }
      }
    }
    if(flag==1)
    break;
  }
  return flag;
}

int main(){

  int T;
  scanf("%d",&T);

  while(T){
    int N;
    scanf("%d",&N);
    // if(semiPrime(N))
    // printf("YES\n");
    // else
    // printf("NO\n");
    int flag=0;
    for(int i=2;i<N-1;i++){
      int sub=N-i;
      if(semiPrime(i) && semiPrime(sub))
      {printf("YES\n");
      flag=1;
      break;}
    }
      if(flag==0)
      printf("NO\n");

    T-=1;
  }
  return 0;
}
