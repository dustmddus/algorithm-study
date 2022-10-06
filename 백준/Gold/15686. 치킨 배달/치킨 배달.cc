#include<iostream>
#include<algorithm>
#include<vector>
#define X first
#define Y second
using namespace std;

int board[50][50];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	vector<pair<int, int>> home;
	vector<pair<int, int>> chic;

	int n, m;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> board[i][j];
			if (board[i][j] == 1) home.push_back({ i,j });
			if (board[i][j] == 2) chic.push_back({ i,j });
		}
	}

	vector<int> v(chic.size(), 1);
	fill(v.begin(), v.end() - m, 0);
	int dis = 0x7f7f7f7f;
	do{
		int tot = 0;
		for (auto h : home) {
			int d = 0x7f7f7f7f;
			for (int i = 0; i < chic.size(); i++) {
				if (v[i] == 0)continue;
				d = min(d, abs(chic[i].X - h.X) + abs(chic[i].Y - h.Y));
			}
			tot += d;
		}
		dis = min(dis, tot);

	} while (next_permutation(v.begin(), v.end()));
	cout << dis;
}