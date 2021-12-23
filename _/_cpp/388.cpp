#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#if __cplusplus > 201103L
#include <initializer_list>
#include <unordered_map>
#include <unordered_set>
#endif

using namespace std;

#ifndef ONLINE_JUDGE
#define DEBUG
#endif

#define oo 0x3F3F3F3F
#define car first
#define cdr second
#define PB push_back
#define SZ(x) (int)((x).size())
#define ALL(x) (x).begin(), (x).end()
#define For(i, a, b) for (int _end_ = (b), i = (a); i <= _end_; ++i)
#define Rof(i, a, b) for (int _end_ = (b), i = (a); i >= _end_; --i)
#define FOR(i, a, b) for (int _end_ = (b), i = (a); i != _end_; ++i)
#define ROF(i, a, b) for (int _end_ = (b), i = (a); i != _end_; --i)

typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;
typedef long double real;

int64 fpm(int64 b, int64 e, int64 m) { int64 t = 1; for (; e; e >>= 1, b = b * b % m) e & 1 ? t = t * b % m : 0; return t; }
template<class T> inline bool chkmin(T &a, T b) {return a > b ? a = b, true : false;}
template<class T> inline bool chkmax(T &a, T b) {return a < b ? a = b, true : false;}
template<class T> inline T sqr(T x) {return x * x;}
template <typename T> T gcd(T x, T y) {for (T t; x; t = x, x = y % x, y = t); return y; }

template<class edge> struct Graph {
    vector<vector<edge> > adj;
    Graph(int n) {adj.clear(); adj.resize(n + 5);}
    Graph() {adj.clear(); }
    void resize(int n) {adj.resize(n + 5); }
    void add(int s, edge e){adj[s].push_back(e);}
    void del(int s, edge e) {adj[s].erase(find(iter(adj[s]), e)); }
    vector<edge>& operator [](int t) {return adj[t];}
};

const int64 MOD = 1e9;
const int64 N = 1e10;
const int LMT = 3000000;

int H[LMT];
int S[LMT];
map<int64, int> f;

void add(int &a, int64 b) {if ((a += b) >= MOD) a -= MOD; }

int64 calc(int64 n) {
    if (n < LMT) return H[n];
    if (f.count(n)) return f[n];
    cerr << n << " " << SZ(f) << endl;
    int &t = f[n];
    for (int64 i = 2, j; i <= n; i = j) {
        j = n / (n / i) + 1;
        add(t, (j - i) * calc(n / i) % MOD);
    }
    t = ((n + 1) % MOD * (n + 1) % MOD * (n + 1) % MOD - 1 + MOD - t) % MOD;
    return t;
}

int main(int argc, char **argv) {
    ios_base::sync_with_stdio(false);

    // int sum = 0;
    // FOR (i, 1, LMT) {
    //     // add(H[i], (int64)(i + 1) * (i + 1) % MOD * (i + 1) % MOD - 1);
    //     add(sum, S[i]);
    //     H[i] = ((int64)(i + 1) * (i + 1) % MOD * (i + 1) % MOD - 1 + MOD - sum) % MOD;
    //     for (int j = i; (j += i) < LMT; ) {
    //         add(S[j], (MOD + H[i] - H[i - 1]) % MOD);
    //     }
    // }

    // cerr << calc(N) << endl;
    long double x = pow(N + 1, 3), zeta = (long double)1.202056903159594285399738161511449990764;
    // FOR (i, 1, 1e9) zeta += (long double)1.0 / i / i / i;
    cerr << setprecision(20) << x / zeta << endl;
    return 0;
}
