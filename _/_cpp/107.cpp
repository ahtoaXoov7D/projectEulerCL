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

const int n = 40, N = n + 10;

int ufs[N];
char s[1000];

int find(int x) {
    return ufs[x] ? ufs[x] = find(ufs[x]) : x;
}

int main(int argc, char **argv) {
    ios_base::sync_with_stdio(false);
    vector<pair<int, pair<int, int>>> E;
    for (int i = 1; i <= n; ++i) {
        gets(s);
        char *p = s;
        for (int j = 1; j <= n; ++j) {
            if (*p != '-') {
                int x = 0;
                for (; isdigit(*p); ++p)
                    x = x * 10 + *p - '0';
                if (i > j)
                    E.push_back(make_pair(x, make_pair(i, j)));
                cout << x << " " << i << " " << j << endl;
            } else
                ++p;
            ++p;
        }
    }
    sort(ALL(E));

    int ans = 0;
    for (auto e : E) {
        int x = find(e.snd.fst), y = find(e.snd.snd);
        if (x == y) ans += e.fst;
        else {
            ufs[x] = y;
        }
    }
    cout << ans << endl;

    return 0; 
}
