#include <bits/stdc++.h>
using namespace std;

int main(){
  int T;
  cin>>T;
  while(T){
    int N;
    cin>>N;
    vector <int> num;
    int temp;
    cin>>temp;
    num.push_back(temp);
    N-=1;
    int p=1,c=0;

    while(N){
        cin>>temp;
      if(temp<num[num.size()-1]){
        c+=1;
      }

      if(c>1 && p==1){
          cout<<"NO"<<endl;
          p=0;
      }
      if (c==1 && p==1){
        if(temp>num[0])
        {
          cout<<"NO"<<endl;
          p=0;
        }
      }

      num.push_back(temp);
      N-=1;
      }


    if(p==1)
    {
      cout<<"YES"<<endl;
      p=0;
    }

    T-=1;
  }
  return 0;
}
