/*
연구소에 벽을 세우려고!
nxm 직사각형. 바이러스는 상하좌우 퍼져나감
새로 세울 수 있는 벽의 개수 3개. 꼭 3개 세워야 함. 
0은 빈칸, 1은 벽, 2는 바이러스
안전영역 크기의 최댓값. 

문제 풀이 방법
- 우선 빈칸중에 벽을 세울 수 있는 3개의 조합을 구한다. 
- 해당 경우에 따라 벽을 세워서 2가 퍼져나가는 것을 구하고
- 빈칸의 개수를 세어 안전영역을 구한다. -> 최댓값. 
*/

#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#define X first
#define Y second
using namespace std;

int n, m;	//세로 크기 n과 가로 크기 m
int board1[10][10];	//원본 
int board2[10][10];	//복사본
vector<pair<int, int>> emp;	//빈칸 저장할 벡터
queue<pair<int, int>> vir;//바이러스 저장 벡터
queue<pair<int, int>> vir_tmp;	//바이러스 저장벡터 복사하기
bool vis_tmp[10][10];	//방문했는지 체크

int dx[4] = { 1,0,-1,0 };
int dy[4] = { 0,1,0,-1 };

//2로부터 감염
void bfs() {
	while (!vir_tmp.empty()) {
		pair<int, int> cur = vir_tmp.front(); vir_tmp.pop();
		
		for (int dir = 0; dir < 4; dir++) {
			int nx = cur.X+dx[dir];
			int ny = cur.Y+dy[dir];
			if (nx < 0 || nx >= n || ny < 0 || ny >= m)continue;
			if (board2[nx][ny] == 1 || vis_tmp[nx][ny] == 1)continue;
			vis_tmp[nx][ny] = 1;
			board2[nx][ny] = 2;
			vir_tmp.push({ nx,ny });
		}
	}
	

}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> board1[i][j];
			if (board1[i][j] == 0) {
				emp.push_back({ i,j });
			}
			if (board2[i][j] == 2)vir.push({ i,j });
		}
	}
	//벽 벡터에서 3개씩 고르기
	vector<int>brute(emp.size(), 1);
	fill(brute.begin(), brute.end() - 3, 0);
	int mx = 0;
	do {
		for (int i = 0; i < n; i++)fill(vis_tmp[i], vis_tmp[i] + m, 0);
		//board2에 값 복사하기
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				board2[i][j] = board1[i][j];
				if (board1[i][j] == 2) {
					vir_tmp.push({ i,j });
					vis_tmp[i][j] = 1;
				}
			}
		}
		//고른 3개에 벽세우기
		for (int i = 0; i < emp.size(); i++) {
			if (brute[i] == 0)continue;
			int x = emp[i].X;
			int y = emp[i].Y;
			board2[x][y] = 1;
		}
		//벽 세우고 나서 바이러스 감염시키고
		bfs();
		int cnt = 0;
		//안전지역 체크
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (board2[i][j] == 0)cnt++;
			}
		}
		mx = max(mx, cnt);
	} while (next_permutation(brute.begin(), brute.end()));
	cout << mx;
}