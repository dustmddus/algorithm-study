#include<iostream>
#include<string>
#include<queue>
#include<tuple>
#define X first
#define Y second
using namespace std;

int n, m;
pair<int, int> red, blue; // 빨간 구슬과 파란 구슬의 위치
string board[11];
// dist[a][b][c][d] : 빨간 구슬이 (a, b)이고 파란 구슬이 (c, d)에 위치한 상황에 도달하기 위한 동작의 횟수
int dist[11][11][11][11];
int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

int bfs() {
	queue<tuple<int, int, int, int>> q;
	q.push({ red.X, red.Y, blue.X, blue.Y });
	dist[red.X][red.Y][blue.X][blue.Y] = 0;
	while (!q.empty()) {
		int rx, ry, bx, by;
		tie(rx, ry, bx, by) = q.front();
		q.pop();
		int cnt = dist[rx][ry][bx][by];
		// 10번 넘게 탈출 못하면 -1
		if (cnt >= 10)
			return -1;
		for (int i = 0; i < 4; i++) {
			int n_rx = rx, n_ry = ry, n_bx = bx, n_by = by;

			
			while (board[n_bx + dx[i]][n_by + dy[i]] == '.') {
				n_bx += dx[i];
				n_by += dy[i];
			}
			// Blue가 탈출했다면 실패이므로 continue
			if (board[n_bx + dx[i]][n_by + dy[i]] == 'O') continue;

			while (board[n_rx + dx[i]][n_ry + dy[i]] == '.') {
				n_rx += dx[i];
				n_ry += dy[i];
			}
			// Red가 탈출했다면 종료, 바로 정답을 반환
			if (board[n_rx + dx[i]][n_ry + dy[i]] == 'O') return cnt + 1;

			if ((n_rx == n_bx) && (n_ry == n_by)) {
				//아래
				if (i == 0) {
					ry < by ? n_ry-- : n_by--;
				}
				//오른쪽
				else if (i == 1) {
					rx < bx ? n_rx--: n_bx--;
				}
				//위
				else if (i == 2) {
					ry > by ? n_ry++ : n_by++;
				}
				//왼쪽
				else if (i == 3) {
					rx > bx ? n_rx++ : n_bx++;
				}
			}
			
			if (dist[n_rx][n_ry][n_bx][n_by] != -1)continue;
			dist[n_rx][n_ry][n_bx][n_by] = cnt + 1;
			q.push({ n_rx,n_ry,n_bx,n_by });
		}
	}
	return -1;
}

int main() {
	
	cin >> n >> m;

	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			for (int k = 0; k < 10; k++) {
				fill(dist[i][j][k], dist[i][j][k] + 10, -1);
			}
		}
	}


	for (int i = 0; i < n; i++) {
		cin >> board[i];
		for (int j = 0; j < m; j++) {
			if (board[i][j] == 'B') {
				blue = { i, j };
				board[i][j] = '.';
			}
			else if (board[i][j] == 'R') {
				red = { i, j };
				board[i][j] = '.';
			}
		}
	}

	cout << bfs();
}