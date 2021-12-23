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
int findGCD(int a,int b) {    //assume a is greater than b
   if(a == 0 || b == 0)
      return 0;    //as a and b are 0, the greatest divisior is also 0
   if(a==b)
      return b;    //when both numbers are same
   if(a>b)
      return findGCD(a-b, b);
   else
      return findGCD(a, b-a);
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int x=n,h;
    for(int i=n-1;i>n/2;i--)
    {
        h=findGCD(x,i);
        x=(x*i)/h;
    }
    cout<<x<<"\n";
    }
    return 0;
}
