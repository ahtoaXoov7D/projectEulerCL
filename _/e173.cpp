#include <cmath>
#include <cstdio>
#include <ctime>

long long sqr(long long x){ return x * x; }
bool is_sqr(long long x){ return sqr(floor(sqrt(x+.5))) == x; }
int main(void){
	clock_t ini = clock();
	int ans = 0;
	for(long long i = 1; i < 500000; ++i)
		for(long long j = i + 2; ; j += 2){
			long long d = j * j - i * i;
			if(d > 1000000) break;
			++ans;
		}
	printf("Time spent: %.3lfs\n", ((double)(clock() - ini))/CLOCKS_PER_SEC);
	printf("Answer: %d\n", ans);
	return 0;
}
