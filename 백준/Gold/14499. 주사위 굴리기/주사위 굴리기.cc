#include<iostream>
using namespace std;

int board[25][25];
int ndice[6];
int dice[6];

int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };

void go(int dir) {
	//동:1 서:2 북:3 남:4
	switch (dir) {
		case 0:
			ndice[0] = dice[0];
			ndice[1] = dice[4];
			ndice[4] = dice[3];
			ndice[5] = dice[1];
			ndice[2] = dice[2];
			ndice[3] = dice[5];
			break;
		case 1:
			ndice[0] = dice[0];
			ndice[1] = dice[5];
			ndice[2] = dice[2];
			ndice[3] = dice[4];
			ndice[4] = dice[1];
			ndice[5] = dice[3];
			break;
		case 2:
			ndice[0] = dice[1];
			ndice[1] = dice[2];
			ndice[2] = dice[3];
			ndice[3] = dice[0];
			ndice[4] = dice[4];
			ndice[5] = dice[5];
			break;
		case 3:
			ndice[0] = dice[3];
			ndice[1] = dice[0];
			ndice[2] = dice[1];
			ndice[3] = dice[2];
			ndice[4] = dice[4];
			ndice[5] = dice[5];
			break;
	}
	for (int i = 0; i < 6; i++) {
		dice[i] = ndice[i];
	}
}

int main() {
	int n, m, sx, sy, k;
	cin >> n >> m >> sx >> sy >> k;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> board[i][j];
		}
	}

	while (k--) {
		int dir;
		cin >> dir;
		dir--;
		int nx = sx + dx[dir];
		int ny = sy + dy[dir];
		if (nx<0 || nx>=n || ny<0 || ny>=m)continue;
		go(dir);
		if (board[nx][ny] == 0) {
			board[nx][ny] = dice[3];
		}
		else {
			dice[3] = board[nx][ny];
			board[nx][ny] = 0;
		}
		sx = nx;
		sy = ny;
		cout << dice[1]<<"\n";
	}
}