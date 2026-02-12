#include <iostream>
#include <vector>

using namespace std;

int r, c, k;
int x;
int main() {
    freopen("hopscotch.in", "r", stdin);
    freopen("hopscotch.out", "w", stdout);
    int MOD = 1000000007;
    cin >> r >> c >> k;
    vector<vector<int>> board(r, vector<int>(c));
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> x;
            board[i][j] = x;
        }
    }
    // for (int i = 0; i < r; i++) {
    //     for (int j = 0; j < c; j++) {
    //         cout << board[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    vector<vector<int>> dp(r, vector<int>(c));
    dp[0][0] = 1;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            for (int x = 0; x < i; x++) {
                for (int y = 0; y < j; y++) {
                    if (board[i][j] != board[x][y]) {
                        dp[i][j] += dp[x][y];
                        dp[i][j] %= MOD;
                    }
                }
            }
        }
    }
    cout << dp[r - 1][c - 1];
    return 0;
}
