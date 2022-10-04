#include<iostream>
#include<deque>
#include<string>
using namespace std;

deque<int> dq[4];

void go(int num,int dir) {
	int dirs[4] = {};
	dirs[num] = dir;

	int idx = num;
	//왼쪽으로 전파
	while (idx > 0 && dq[idx][6] != dq[idx - 1][2]) {
		dirs[idx - 1] = -dirs[idx];
		idx--;
	}
	idx = num;
	//오른쪽으로 전파
	while (idx < 3 && dq[idx][2] != dq[idx + 1][6]) {
		dirs[idx + 1] = -dirs[idx];
		idx++;
	}
	for (int i = 0; i < 4; i++) {
		if (dirs[i] == 1) {
			dq[i].push_front(dq[i].back());
			dq[i].pop_back();
		}
		else if(dirs[i]==-1) {
			dq[i].push_back(dq[i].front());
			dq[i].pop_front();
		}
	}


}

int main() {
	for (int i = 0; i < 4; i++) {
		string s;
		cin >> s;
		for (int j = 0; j < s.size(); j++) {
			dq[i].push_back(s[j]-'0');
		}
		
	}

	int n;
	cin >> n;
	while (n--) {
		int num, dir;
		cin >> num >> dir;
		go(num-1, dir);
	}
	int ans = 0;
	for (int i = 0; i < 4; i++) {
		if (dq[i][0] == 1) {
			ans += (1 << i);
		}
		
	}
	cout << ans;
}