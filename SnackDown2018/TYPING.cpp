#include <bits/stdc++.h>
using namespace std;

int main(){
  int T;
  scanf("%d",&T);
  while(T){
    int N=0;
    cin>>N;
    double tm=0.0;
    vector <string> wordC;

    while(N){
      string word;
      cin >> word;
      int flag=0;
      for(int i=0;i<wordC.size();i++){
        if (!wordC[i].compare(word)){
          flag=1;
          break;
        }
      }
      if (flag==0)
      {
        wordC.push_back(word);
      }
      double t=0.2;
      char c =word[0];
      char hand;
      if (c == 'd' || c=='f')
        hand ='l';
      else
        hand ='r';

      for(int i=1;i<word.length();i++){
        c=word[i];
        if (c == 'd' || c=='f'){
          if (hand == 'l')
            t=t+0.4;
          else
            t=t+0.2;
          hand='l';
        }
        else{
          if (hand == 'r')
            t=t+0.4;
          else
            t=t+0.2;
          hand='r';
        }
      }

      if (flag==1)
     {
       flag=0;
       t=t/2.0;
     }

      tm=tm+t;

      N-=1;
    }
    cout << tm*10 <<endl;
    T-=1;
  }
  return 0;
}
