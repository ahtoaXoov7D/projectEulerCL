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
#ifdef DEBUG
#define cvar(x) cerr << "<" << #x << ": " << x << ">"
#define evar(x) cvar (x) << endl
template<class T> void DISP(const char *s, T x, int n) {cerr << "[" << s << ": "; for (int i = 0; i < n; ++i) cerr << x[i] << " "; cerr << "]" << endl;}
#define disp(x,n) DISP(#x " to " #n, x, n)
#else
#define cvar(...) ({})
#define evar(...) ({})
#define disp(...) ({})
#endif
#define car first
#define cdr second
#define PB push_back
#define SZ(x) (int)((x).size())
#define ALL(x) (x).begin(), (x).end()
#define FOR(i, a, b) for (int _end_ = (b), i = (a); i <= _end_; ++i)
#define ROF(i, a, b) for (int _end_ = (b), i = (a); i >= _end_; --i)

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

const int64 MOD = fpm(17, 7, 1e18), PHI = MOD - MOD / 17;

int64 inv(int64 x) {
    return fpm(x, PHI - 1, MOD);
}

int main(int argc, char **argv) {
#ifndef ONLINE_JUDGE
#endif
    ios_base::sync_with_stdio(false);

    int64 e = fpm(10, 1e18, PHI);
    cout << (fpm(MOD - 1, e, MOD) * inv(MOD - 15) % MOD + fpm(2, e, MOD) * 4 % MOD * inv(MOD - 3) % MOD + 2 * inv(5) % MOD * fpm(4, e, MOD) % MOD + 1) % MOD << endl;

    return 0; 
}
