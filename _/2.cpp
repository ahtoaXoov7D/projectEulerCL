// Ans - 4613732
//           
#include<bits/stdc++.h>
using namespace std;
#define ll                        long long
#define vi                        vector<ll int>
#define pb                        emplace_back
#define rep(i,a,b)                for(int i = a; i<b; ++i)
#define rrep(i,a,b)               for(int i = a; i>=b; --i)
#define p(a)                      cout << a << "\n";
#define p2(a,b)                   cout << a << " " << b << "\n";
#define fast_io                   ios_base::sync_with_stdio(false);cin.tie(NULL);
//:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::://

// Method 1 - Normal fibonacci till n 
ll SumFib(ll n) {
    ll sum = 0;
    ll a = 0, b = 1, c;
    for (ll i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
        if(b>=n) break;
        if(b%2==0)  sum += b;
    }
    return sum;
}

// Method 2 -  Every third term of this series is even 
// F(N) = 4*F(N-1) + F(N-3)

ll ModFib(ll n) {
    ll sum=0;
    ll a = 2, b = 8, c;
    while(sum<=n) {
        sum += b;
        c = 4*b + a;
        a = b;
        b = c;
    }
    return sum+2;
}


int32_t main() {
    fast_io;
    ll tt;  cin >> tt;
    while(tt--) {
        ll n;   cin >> n;
        cout << SumFib(n) << "\n";
    }
    return 0;
}
