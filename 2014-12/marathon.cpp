#include <iostream>
#include <vector>

using namespace std;

int n, k;
vector<pair<int,int>> checkpoints;
vector<vector<int>> memo;

int dp(int i, int skips) {
    if (i >= n - 1) {
        return 0;
    }
    if (memo[i][skips] != -1){
        return memo[i][skips];
    }
    int ret = 1000000;
    for (int newSkips = 1; newSkips < k - skips + 1; newSkips++) {
        int newLoc = i + newSkips + 1;
        if (newLoc > n - 1) {
            continue;
        }
        int d = abs(checkpoints[newLoc].first - checkpoints[i].first) + abs(checkpoints[newLoc].second - checkpoints[i].second);
        ret = min(ret, d + dp(newLoc, skips + newSkips));
    }
    int d = abs(checkpoints[i + 1].first - checkpoints[i].first) + abs(checkpoints[i + 1].second - checkpoints[i].second);
    ret = min(ret, d + dp(i + 1, skips));
    return memo[i][skips] = ret;
}

int main() {
    freopen("marathon.in", "r", stdin);
    freopen("marathon.out", "w", stdout);

    cin >> n >> k;
    checkpoints.resize(n);
    
    for (int i = 0; i < n; i++) {
        cin >> checkpoints[i].first >> checkpoints[i].second;
    }

    memo.assign(n, vector<int>(k + 1, -1));

    int ans = dp(0, 0);
    cout << ans;
}
