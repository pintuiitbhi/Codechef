#include <bits/stdc++.h>
#include <algorithm>


using namespace std;

#define ll long long
const int mod = 1e9+7;

ll C[5001][5001];
ll modInv(ll a, ll m=1000000007)
{
    ll m0 = m;
    ll y = 0, x = 1;

    if (m == 1)
      return 0;

    while (a > 1)
    {
        // q is quotient
        ll q = a / m;
        ll t = m;

        // m is remainder now, process same as
        // Euclid's algo
        m = a % m, a = t;
        t = y;

        // Update y and x
        y = x - q * y;
        x = t;
    }

    // Make x positive
    if (x < 0)
       x += m0;

    return x;
}

ll modDivide(ll a, ll b, ll m=1000000007)
{
        a = a % m;
        ll inv = modInv(b,m);
        return (inv*a)%m;
}


int min(int a, int b);

// Returns value of Binomial Coefficient C(n, k)
ll nCr(ll n, ll k)
{
    ll C[n+1][k+1];
    ll i, j;

    // Caculate value of Binomial Coefficient in bottom up manner
    for (i = 0; i <= n; i++)
    {
        for (j = 0; j <= min(i, k); j++)
        {
            // Base Cases
            if (j == 0 || j == i)
                C[i][j] = 1;

            // Calculate value using previosly stored values
            else
                C[i][j] = ((C[i-1][j-1] % 1000000006) + (C[i-1][j] % 1000000006))% 1000000006;
        }
    }

    return (C[n][k] % 1000000006);
}

// A utility function to return minimum of two integers
ll min(ll a, ll b)
{
    return (a<b)? a: b;
}


ll power(ll x, unsigned ll y, ll p)
{
    ll res = 1;      // Initialize result

    x = x % p;  // Update x if it is more than or
                // equal to p

    while (y > 0)
    {
        // If y is odd, multiply x with result
        if (y & 1)
            res = (res*x) % p;

        // y must be even now
        y = y>>1; // y = y/2
        x = (x*x) % p;
    }
    return res;
}


int main()
{

int T = 0;
cin >> T;

while(T)
{
  long int N=0,K=0;
    cin >> N >> K;

    ll seq[N];

for (long int i=0;i<N;i++)
    cin>>seq[i];


    ll n = sizeof(seq)/sizeof(seq[0]);

sort(seq,seq+n);

    ll prod=1;
    ll a=0;
    a=nCr(N-1,K-1);


    for (long int i=1;i<N;i++){
      ll a1=0,a2=0,ans=0;
        ll c=0;
      ll  b=0;
        if ((N-i-1)>=(K-1))
            b= nCr(N-i-1,K-1);

        if (i>=(K-1))
            c = nCr(i,K-1);


        a1=power(seq[i],a , mod);
        a2=power(seq[i],(b+c)%1000000006 , mod);
        ans=modDivide(a1,a2,1000000007);

        prod=((prod %mod) * (ans % mod))%mod;
}
    cout<<prod<<"\n";
    T-=1;
}
return 0;
  }
