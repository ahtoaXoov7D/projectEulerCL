#include <algorithm>
#include <cstdio>

using namespace std;

struct point {
	int x, y;
	inline int sqr(int k){ return (k*k);}
	int d2(point p){ return sqr(x - p.x) + sqr(y - p.y);}
	point(int _x=0, int _y=0):x(_x),y(_y){}
	point operator-(point p){ return point(x-p.x,y-p.y);}
	int operator*(point p){ return (x*p.y)-(y*p.x);}
}p[2048];
int N;

bool ord(point a, point b){
	int k = (a - p[0]) * (b - p[0]);
	return k ? k > 0 : p[0].d2(a) < p[0].d2(b);
}
bool grahamScan(){
	int idx, miny = 1<<25, t = 0, x;
	point *q[2048];
	for(int i = 0; i < N; ++i){
		if(i == N) break;
		if(p[i].y < miny || (p[i].y == miny && p[i].x < x))
			miny = p[i].y, x = p[i].x, idx = i;
	}
	if(N < 3) return 0;
	swap(p[0],p[idx]);
	sort(p+1, p+N, ord);
	q[t++] = &p[0];
	q[t++] = &p[1];
	for(int i = 2; i < N; ++i){
		while(t > 1 && ((*q[t-1]- *q[t-2])*(p[i] - *q[t-2])) <= 0) t--;
		q[t++] = &p[i];
	}
	printf("%d\n", t + 1);
	for(int x = 0; x < t; ++x) printf("%d %d\n", q[x]->x, q[x]->y);
	printf("%d %d\n", q[0]->x, q[0]->y);
	return N > 0 && t > 2;
}

int main(void){
	int a, b, c;
	scanf("%d", &a);
	printf("%d\n", a);
	while(a--){
		scanf("%d", &b);
		for(N = 0; N < b; ++N) scanf("%d %d", &p[N].x, &p[N].y);
		scanf("%d",&c);
		grahamScan();
		if(a) printf("-1\n");
	}
	return 0;
}

