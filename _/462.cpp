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

#define inf 0x3F3F3F3F
#define fst first
#define snd second
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
template <typename T> T gcd(T x, T y) {for (T t; x; ) t = x, x = y % x, y = t; return y; }

template<class edge> struct Graph {
    vector<vector<edge> > adj;
    Graph(int n) {adj.clear(); adj.resize(n + 5);}
    Graph() {adj.clear(); }
    void resize(int n) {adj.resize(n + 5); }
    void add(int s, edge e){adj[s].push_back(e);}
    void del(int s, edge e) {adj[s].erase(find(iter(adj[s]), e)); }
    vector<edge>& operator [](int t) {return adj[t];}
};

const int64 N = 1e18;

real fac[210];
int v[100][100];

int main(int argc, char **argv) {
    ios_base::sync_with_stdio(false);
 
    real ans = 0;
    int cnt = 0;
    for (int64 i = 0, pi = 1; pi <= N; ++i, pi *= 2) {
        for (int64 j = 0, pj = pi; pj <= N; ++j, pj *= 3) {
            v[i][j] = 1;
            ++cnt;
            ans += log(cnt);
        }
    }
    cout << cnt << endl;
    
    fac[0] = 1;
    for (int i = 1; i <= 200; ++i)
        fac[i] = fac[i - 1] * i;
    for (int i = 0; i <= 70; ++i)
        for (int j = 0; j <= 70; ++j)
            if (v[i][j]){
                int t = 0;
                for (int k = i; v[k][j]; ++k)
                    ++t;
                for (int k = j; v[i][k]; ++k)
                    ++t;
                ans -= log(t - 1);
            }
    cout << setprecision(20) << exp(ans) << endl;

    return 0; 
}
