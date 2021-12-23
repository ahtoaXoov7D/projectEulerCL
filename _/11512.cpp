#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

/* {{{ Suffix array */
#define N 1024
char w[N];
int H = 0, bucket[N], lcp[N], new_bucket[N], rank[N];
struct suffix {
	int z;
	bool operator<(const suffix& s) const {
		if(!H) return w[z] < w[s.z];
		if(bucket[z] == bucket[s.z]) return bucket[z + H] < bucket[s.z + H];
		return bucket[z] < bucket[s.z];
	}
	bool operator==(const suffix& s) const {
		return !(*this < s) && !(s < *this);
	}
} pos[N]; 
bool update_buckets(int L){
	int i, id;
	for(i = id = 0; i < L; ++i)
		new_bucket[pos[i].z] = (id += i && !(pos[i] == pos[i - 1]));
	memcpy(bucket, new_bucket, L << 2);
	return id != L - 1;
}

void suffix_array(int L){
	int c = 1;
	memset(bucket, -1, sizeof bucket);
	for(int i = H = 0; i < L; ++i) pos[i].z = i;
	for(H = 0; c; H = (H << 1) | !H){
		sort(pos, pos + L); 
		c = update_buckets(L);
	}
}

void compute_lcp(int L){
	for(int i = 0; i < L; ++i) rank[pos[i].z] = i;
	for(int h = 0, i = 0, j; i < L; ++i)
		if(rank[i]){
			j = pos[rank[i] - 1].z;			
			while(w[i + h] != '$' && w[i + h] == w[j + h]) ++h;
			lcp[rank[i]] = h;
			h -= h > 0;
		}
}
/* }}} */

int main(void){
	int t; scanf("%d", &t);
	while(t-- && scanf("%s", w) == 1){
		int L, maxlcp = 0;
		for(L = 0; w[L]; ++L);
		suffix_array(L);
		compute_lcp(L);
		for(int i = 0; i < L; ++i) maxlcp = max(maxlcp, lcp[i]);
		if(!maxlcp) puts("No repetitions found!");
		else for(int i = 0, j; i < L; ++i) if(lcp[i] == maxlcp){
			for(j = i; j < L && lcp[j] >= lcp[i]; ++j);
			w[pos[i].z + lcp[i]] = 0;
			printf("%s %d\n", w + pos[i].z, j - i + 1);
			break;
		}
	}
	return 0;
}

