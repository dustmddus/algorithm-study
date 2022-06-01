#include<iostream>
#include<algorithm>
using namespace std;

int n, m;
int board[10];
int arr[10];
bool isused[10];

void func(int k) {
	if (k == m) {
		for (int i = 0; i < m; i++) {
			cout << board[arr[i]]<<' ';
		}
		cout << "\n";
		return;
	}
	int st = 0;
	if (k != 0)st = arr[k - 1] + 1;
	for (int i = st; i < n; i++) {
		if (isused[i])continue;
		arr[k] = i;
		isused[i] = 1;
		func(k + 1);
		isused[i] = 0;
	}
}

int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> board[i];
	}
	sort(board, board + n);
	func(0);
}