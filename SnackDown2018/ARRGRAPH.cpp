#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b)
{
  if (b == 0)
      return a;
  return gcd(b, a % b);
}

int coprime(int x, int y){
  int g=gcd(x,y);
  if(g==1)
    return 1;
  else
    return 0;
}


int BFS(int adj[100][100], int start, int n)
{
    vector<bool> visited(100, false);
    queue<int> Q;
    Q.push(start);
    visited[start] = true;
    int count = 1;

    while(!Q.empty()){
        int top = Q.front(); Q.pop();

        for (int i = 0; i < n; ++i){
            if(adj[top][i] != 0 && (! visited[i]) ){
                Q.push(i);
                visited[i] = true;
                count++;
            }
        }
    }
    return count;
}


int main(){
  int T,temp=0;
  cin>>T;

  while(T){
    int N;
    cin>>N;
    int tempN=N;
    int adj[100][100];
    memset(adj,0,sizeof(adj));
    vector <int> num;

    int freq=0,co=0;
    while(N){
      cin>>temp;
      num.push_back(temp);
      N-=1;
    }

    for(int i=0;i<num.size()-1;i++){
      for(int j=i+1;j<num.size();j++){
        if(coprime(num[i],num[j])){
          adj[i][j]=1;
          adj[j][i]=1;
        }
      }
    }
    // cout << "test" <<endl;
    // for(int i=0;i<tempN;i++)
    // {
    //   for(int j=0;j<tempN;j++)
    //   {
    //     cout << adj[i][j] <<" ";
    //   }
    //   cout << endl;
    // }
    // cout << "test" <<endl;


    int travel=BFS(adj,0,num.size());
    if(travel==tempN){
    co=0;
    }

    else{
      for(int i=0;i<num.size();i++){
        if(num[i]==29){
          freq+=1;
        }
      }

      if (freq==0){
        num[0]=29;
        co++;
      }

      if(freq==tempN){
        num[0]=30;
        co++;
      }

    }

    cout<< co<<endl;
    for(int i=0;i<num.size();i++){
      cout<<num[i]<<" ";
    }
    cout<<endl;
    T-=1;
  }
  }
