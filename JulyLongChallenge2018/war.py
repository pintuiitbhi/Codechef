#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define ld long double
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
const int M=1002;
int val[M][M],vis[M],ct[M];
int main()
{
	int test,n,i,j,a,b,p,q;
	cin>>test;
	while(test--)
	{
		cin>>n>>a>>b;
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++)
				cin>>val[i][j];
		int x=-1;
		for(i=1;i<=n;i++)
		{
			bool f=0;
			ct[i]=0;
			for(j=1;j<=n;j++)
			{
				if(val[i][j]==0 && i!=j)
					f=1;
			}
			if(f==0)
				x=i;
		}
		if(x!=-1)
		{
			for(i=1;i<=n;i++)
			{
				if(x==i)
					cout<<n<<" ";
				else
					cout<<"0 ";
			}
			cout<<"\n";
			fflush(stdout);
			for(i=1;i<=n;i++)
			{
				cin>>p;
				ct[i]+=p;
			}
			int y=n/(a+b);
			j=1;
			while(y--)
			{
				for(i=1;i<=a;i++)
				{
					while(ct[j]==0)
						j++;
					cout<<x<<" "<<j<<"\n";
					fflush(stdout);
					ct[j]--;
				}
				for(i=1;i<=b;i++)
				{
					cin>>p>>q;
					ct[q]--;
				}
			}
		}
		else
		{
			for(i=1;i<=n;i++)
			{
				vis[i]=0;
				ct[i]=0;
				cout<<1<<" ";
			}
			cout<<"\n";
			fflush(stdout);
			for(i=1;i<=n;i++)
			{
				cin>>p;
				ct[i]+=p;
			}
			int x=1;
			int curr=1;
			int ptr=1;
			int y=n/(a+b);
			while(y--)
			{
				for(i=1;i<=a;i++)
				{
					bool f=0;
					while(vis[x] && x<=n)
					{
						x++;
					}
					if(x<=n)
					{
						for(j=1;j<=n;j++)
						{
							if(val[x][j] && ct[j])
							{
								cout<<x<<" "<<j<<"\n";
								fflush(stdout);
								ct[j]--;
								vis[x]=1;
								f=1;
								break;
							}
						}
					}
					if(f==0)
					{
						while(vis[curr])
							curr++;
						while(ct[ptr]==0)
							ptr++;
						cout<<curr<<" "<<ptr<<"\n";
						fflush(stdout);
						ct[ptr]--;
						vis[curr]=1;
					}
				}
				for(i=1;i<=b;i++)
				{
					cin>>p>>q;
					vis[p]=1;
					ct[q]--;
				}
			}
		}
	}
	return 0;
} 
