#include <bits/stdc++.h>
using namespace std;

int n;
string s;
vector<vector<int>> board(2000, vector<int>(2000, 0));
vector<vector<int>> visited(2000, vector<int>(2000, 0));

void flood(int i, int j) {
    vector<pair<int, int>> stack = {make_pair(i, j)};
    visited[i][j] = 1;
    while (stack.size()) {
        pair<int, int> p = stack.back();
        stack.pop_back();
        int dx[] = {0, 1, 0, -1};
        int dy[] = {1, 0, -1, 0};
        for (int d = 0; d < 4; d++) {
            int vX = (p.first + dx[d] + 2000) % 2000;
            int vY = (p.second + dy[d] + 2000) % 2000;
            if (board[vX][vY]) {
                continue;
            }
            if (!visited[vX][vY]) {
                stack.push_back(make_pair(vX, vY));
                visited[vX][vY] = 1;
            }
        }
    }
}

int main() {
    freopen("gates.in", "r", stdin);
    freopen("gates.out", "w", stdout);

    cin >> n;
    cin >> s;

    map<char, pair<int, int>> directionMap = {
        {'N', make_pair(0, 2)},
        {'S', make_pair(0, -2)},
        {'E', make_pair(2, 0)},
        {'W', make_pair(-2, 0)}
    };

    int curX = 0;
    int curY = 0;
    int prevX, prevY, betweenX, betweenY;
    for (int i = 0; i < n; i++) {
        prevX = curX; prevY = curY;
        curX = curX + directionMap[s[i]].first;
        curY = curY + directionMap[s[i]].second;
        betweenX = (prevX + curX) / 2;
        betweenY = (prevY + curY) / 2;
        board[(prevX + 2000) % 2000][(prevY + 2000) % 2000] = 1;
        board[(betweenX + 2000) % 2000][(betweenY + 2000) % 2000] = 1;
        board[(curX + 2000) % 2000][(curY + 2000) % 2000] = 1;
    }

    int components = 0;
    for (int i = 0; i < 2000; i++) {
        for (int j = 0; j < 2000; j++) {
            if (board[i][j]) {
                continue;
            }
            if (!visited[i][j]) {
                components++;
                flood(i, j);
            }
        }
    }
    cout << components - 1 << endl;
    return 0;
}
