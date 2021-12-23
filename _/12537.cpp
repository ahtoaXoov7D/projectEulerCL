#include <algorithm>
#include <cstdio>

using namespace std;

const int NN = 200048;
int D1[NN], D2[NN];
int hx[NN], hy[NN];
int ax, ay, bx, by, q;

int bin_search(int key, int *z, int n){
	int low = 0, mid, high = n;
	while(low < high){
		mid = (low + high) >> 1;
		if(z[mid] <= key) low = mid + 1;
		else high = mid;
	}
	return low;
}

inline int sqr(int x){ return x * x; }

int main(void){
	for(int cnum = 0, n; scanf("%d", &n) == 1 && n; ){
		for(int i = 0; i < n; ++i) scanf("%d %d", hx + i, hy + i);
		scanf("%d %d %d %d %d", &ax, &ay, &bx, &by, &q);
		for(int i = 0; i < n; ++i){
			D1[i] = sqr(hx[i] - ax) + sqr(hy[i] - ay);
			D2[i] = sqr(hx[i] - bx) + sqr(hy[i] - by);
		}
		sort(D1, D1 + n);
		sort(D2, D2 + n);
		int r1, r2;
		printf("Case %d:\n", ++cnum);
		for(int i = 0; i < q; ++i){
			scanf("%d %d", &r1, &r2);
			r1 *= r1;
			r2 *= r2;
			printf("%d\n", max(n - bin_search(r1, D1, n) - bin_search(r2, D2, n), 0));
		}


	}
	return 0;
}

