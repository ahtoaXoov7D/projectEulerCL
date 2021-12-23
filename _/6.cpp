#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main()
{
    int t;
    cin>>t;
    while(t--)
    {
    long int n;
    cin>>n;    
   // long long int t=(n*(n+1)*(2*n+1))/6;
    //long long int h=pow(((n*(n+1))/2),2);
    cout<<(((n*((3*n)+2)*((n*n)-1)))/12)<<"\n";
    }
    return 0;
}
