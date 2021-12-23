#include <algorithm>
#include "fmt/format.h"
using namespace std;
using namespace fmt;

namespace PE397 {
    const int K = 1e6, X = 1e9;

    int primes[K * 2 + 10], lnk[K * 2 + 10];
    int top;
    int dvs[50], expo[50];
    long current, ans = 0, rt_ans = 0;

    int test(long k, long a, long b, long c) {
        return (k + (a + b)) * (k - (b + c)) == 2 * k * k;
        long v = k * k + (b + c) * (b + a);
        // if (v * (b - c) * (b - a) < 0) return false;
        if (v == k * (a - c)) {
            // print("{} {} {} {}: {} {}\n", k, a, b, c, k * k * 2, (k + (a + b)) * (k - (b + c)));
            return 1;
        }
        return 0;
    }

    void bf() {
        long ans = 0;
        for (int k = 1; k <= K; ++k)
            for (int a = -X; a <= X; ++a)
                for (int b = a + 1; b <= X; ++b)
                    for (int c = b + 1; c <= X; ++c) {
                        if (test(k, a, b, c) || test(k, b, c, a) || test(k, c, a, b)) {
                            if (test(k, a, b, c) + test(k, b, c, a) + test(k, c, a, b) >= 2) {
                                print("{} {} {}: {} {} {} {}\n", test(k, a, b, c), test(k, b, c, a), test(k, c, a, b), k, a, b, c);
                            }
                            ++ans;
                            // print("{} {} {}\n", a, b, c);
                        }
                        // ans += test(k, a, b, c) + test(k, b, c, a) + test(k, c, a, b);
                    }
        print("bf ans = {}\n", ans);
    }

    struct Interval {
        long L, R;

        long length() {
            return max(0l, R - L + 1);
        }

        Interval(long l, long r) : L(l), R(r) {}

        Interval cap(Interval b) {
            return Interval(max(L, b.L), min(R, b.R));
        }
    };

    Interval global(-X, +X);

    void update(long value) {

        long a_b = value - current, b_c = current - 2l * current * current / value;
        // a + b = a_b, b + c = b_c
        // not necessarily a < b < c

        // Case 1: a < b < c
        long L = ceil((a_b + 1) / 2.), R = floor((b_c - 1) / 2.);

        Interval feasible = global.cap(Interval(a_b - X, a_b + X)).cap(Interval(b_c - X, b_c + X));
        ans += feasible.cap(Interval(L, R)).length();
        // ans += feasible.length();
        // for (int b = feasible.L; b <= feasible.R; ++b) {
        //     print("{} {} {}\n", a_b - b, b, b_c - b);
        // }

        if (a_b > b_c) {
            // Case 2: b < c < a
            ans += feasible.cap(Interval(-X, R)).length();

            // Case 3: c < a < b
            ans += feasible.cap(Interval(L, +X)).length();
        }

        long P = value, Q = -2l * current * current / value;
        if (P % 2 == 0) {
            long k = current;
            P /= 2;
            if (P != k && (P - Q) * k % (P - k) == 0) {
                long b = P + (P - Q) * k / (P - k);
                if (b % 2 == 0) {
                    b /= 2;

                    long a = P - b, c = Q - b;
                    if (-X <= a && a < b && b < c && c <= X) {
                        // print("RT1 {} {} {}\n", a, b, c);
                        ++rt_ans;
                    }
                }
            }

            // print("RT {} {} {}\n", P, Q, k);
            // P = -18, Q = 2, k = 6;
            if (P != -k && (P - Q) * k % (P + k) == 0) {
                long b = P - (P - Q) * k / (P + k);
                if (b % 2 == 0) {
                    b /= 2;

                    long a = P - b, c = Q - b;
                    if (-X <= b && b < a && a < c && c <= X) {
                        // print("RT2 {} {} {}\n", a, b, c);
                        rt_ans += 2;
                    }
                }
            }
        }
    }

    void dfs(int depth, long value) {
        if (depth == 0) {
            // print("{} {}\n", 2l * current * current, value);
            update( value);
            update(-value);
            return;
        }
        for (int i = 0; i <= expo[depth]; ++i) {
            dfs(depth - 1, value);
            value *= dvs[depth];
        }
    }

    void main() {
        // bf();
        for (int i = 2; i <= K * 2; ++i) {
            if (!primes[i]) primes[++primes[0]] = i, lnk[i] = 1;
            for (int j = 1, t, k = 2 * K / i; primes[j] <= k; ++j) {
                primes[t = i * primes[j]] = 1, lnk[t] = i;
                if (i % primes[j] == 0) break;
            }
        }
        lnk[1] = 1;

        for (int i = 1; i <= K; ++i) {
            if (i % 100000 == 0) {
                print("#i = {}\n", i);
            }
            current = i;
            top = 0;
            for (int x = i * 2; x != 1; ) {
                ++top;
                int p = x / lnk[x], e = 0;
                for (; x % p == 0; x /= p)
                    ++e;
                expo[top] = e * 2 - (p == 2), dvs[top] = p;
                // print("dvs: {}\n", p);
            }
            dfs(top, 1);
        }
        print("#angle = {}, rt_ans = {}, ans = {}\n", ans, rt_ans, ans - rt_ans);
    }
}

int main() {
    PE397::main();
    return 0;
}
