#include<bits/stdc++.h>
#define X first
#define Y second
using namespace std;

int dx[4] = { 1,-1,0,0 };
int dy[4] = { 0,0,1,-1 };

int main() {
	int T;	//테스트 케이스
	cin >> T;
	while (T--) {
		int m, n, k;//가로길이, 세로길이, 배추 위치
		cin >> m >> n >> k;
		int board[52][52] = { 0 };
		int vis[52][52] = { false };
		int a, b;
		int cnt = 0;
		queue<pair<int, int>> Q;
		for (int i = 0; i < k; i++) {
			cin >> a >> b;
			board[b][a] = 1;
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (board[i][j] == 1&&!vis[i][j]) {
					Q.push({ i,j });
					vis[i][j] = true;
					while (!Q.empty()) {
						auto cur = Q.front(); Q.pop();
						for (int i = 0; i < 4; i++) {
							int nx = cur.X + dx[i];
							int ny = cur.Y + dy[i];
							if (nx<0 || nx>n || ny<0 || ny>m)continue;
							if (vis[nx][ny] || board[nx][ny] != 1)continue;
							Q.push({ nx,ny });
							vis[nx][ny] = true;
						}
					}
					cnt++;
				}
			}
		}
		cout << cnt<<"\n";
	}
}