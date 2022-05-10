#include<iostream>
#include<algorithm>
using namespace std;

/*
1. 테이블 정의
d[i]=i까지 올라가는데 밟지 않을 최소 계단 수 단, i는 밟지 않는다. 

2. 점화식
d[i]=min(d[i-2],d[i-3])+s[i]

3. 초기식 
d[1]=s[1] d[2]=s[2] d[3]=s[3]
*/

int s[305];
int d[305];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n;
	cin >> n;
	int tot = 0;
	for (int i = 1; i <= n; i++) {
		cin >> s[i];
		tot += s[i];
	}
	if (n <= 2) {
		cout << tot;
		return 0;
	}
	d[1] = s[1]; d[2] = s[2]; d[3] = s[3];
	for (int i = 4; i < n; i++) {
		d[i] = min(d[i - 2], d[i - 3]) + s[i];
	}
	cout << tot - min(d[n - 1], d[n - 2]);
}