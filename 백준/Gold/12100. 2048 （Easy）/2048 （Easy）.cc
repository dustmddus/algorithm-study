/*
이미 합쳐진 블록은 다시 합쳐질 수 없다. 
상하좌우로 움직일 수 있다. 
최대 5번 움직여서 만들 수 있는 가장 큰 블록의 값
*/
#include<iostream>
#include<algorithm>
using namespace std;

int n;
int board1[25][25];
int board2[25][25];

//시계 방향으로 90도 돌리기
void rotate() {
	int tmp[25][25];
	for (int i = 0; i < n; i++)
		for (int j = 0;j < n; j++)
			tmp[i][j] = board2[i][j];
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			board2[i][j] = tmp[j][n - i - 1];
}

void tilt(int dir) {
	while (dir--)rotate();
	//모든 행에 대해서 기울인다. 
	for (int i = 0; i < n; i++) {
		int tilted[25] = {};
		int idx = 0;
		for (int j = 0; j < n; j++) {
			if (board2[i][j] == 0)continue;
			if (tilted[idx] == 0) {
				tilted[idx] = board2[i][j];
			}
			else if (tilted[idx] == board2[i][j]) {
				tilted[idx++] *= 2;
			}
			else {
				tilted[++idx] = board2[i][j];
			}
		}
		for (int j = 0; j < n; j++) {
			board2[i][j] = tilted[j];
		}
	}
	

}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> board1[i][j];
		}
	}
	int mn = 0;
	//5번 돌리는 경우 각각 4가지의 경우
	for (int tmp = 0; tmp < 1024; tmp++) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				board2[i][j] = board1[i][j];
			}
		}
		int brute = tmp;
		for (int i = 0; i < 5; i++) {
			int dir = brute % 4;
			brute /= 4;
			tilt(dir);
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				mn = max(mn, board2[i][j]);
			}
		}
	}
	cout << mn;
}