#include<iostream>
using namespace std;

int n, m;
int r, c, d;
int board[51][51];

int dx[4] = { -1,0,1,0 };
int dy[4] = { 0,1,0,-1 };

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> n >> m;
	cin >> r >> c >> d;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> board[i][j];
		}
	}
	int cnt = 0;
	while (true) {
		if (board[r][c] == 0)cnt++;
		board[r][c] = -1;
		bool check = false;
		for (int i = 0; i < 4; i++) {
			d = (d + 3) % 4;
			if (board[r + dx[d]][c + dy[d]] == 0) {
				r += dx[d];
				c += dy[d];
				check = true;
				break;
			}
		}
		if (check)continue;
		if (board[r - dx[d]][c - dy[d]] == 1) {
			break;
		}
		r -= dx[d];
		c -= dy[d];
	}
	cout << cnt;
}