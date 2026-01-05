// cheesed it :/ looks like 3 propagations was enough
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int n, m;
vector<vector<pair<int,int>>> adj1;
vector<vector<pair<int,int>>> adj2;

int main() {
    freopen("meeting.in", "r", stdin);
    freopen("meeting.out", "w", stdout);

    cin >> n >> m;
    adj1.resize(n);
    adj2.resize(n);

    int a, b, c, d;
    for (int i = 0; i < m; i++) {
        cin >> a >> b >> c >> d;
        a--;
        b--;
        pair<int,int> p1 = make_pair(b, c);
        pair<int,int> p2 = make_pair(b, d);
        adj1[a].push_back(p1);
        adj2[a].push_back(p2);
    }

    vector<int> ordering = {0};
    vector<int> stack;
    stack.push_back(0);
    vector<bool> visited(n, 0);
    visited[0] = 1;
    while (stack.size()) {
        int u = stack.back();
        stack.pop_back();
        for (auto [v, _] : adj1[u]) {
            if (!visited[v]) {
                visited[v] = 1;
                stack.push_back(v);
                ordering.push_back(v);
            }
        }
    }
    // for (int u : ordering) cout << u << " ";

    int mxDistance = 100 * (n - 1);
    vector<vector<int>> reachable(n, vector<int>(mxDistance, 0));
    vector<vector<int>> reachable2(n, vector<int>(mxDistance, 0));
    reachable[0][0] = 1;
    reachable2[0][0] = 1;
    for (int iterations = 0; iterations < 3; iterations++) {
        for (int u: ordering) {
            if (u == n - 1) {
                continue;
            }
            for (auto [v, w] : adj1[u]) {
                for (int i = mxDistance - 1; i >= 0; i--) {
                    if (i - w < 0) {
                        break;
                    }
                    reachable[v][i] |= reachable[u][i - w];
                }
            }
            for (auto [v, w] : adj2[u]) {
                for (int i = mxDistance - 1; i >= 0; i--) {
                    if (i - w < 0) {
                        break;
                    }
                    reachable2[v][i] |= reachable2[u][i - w];
                }
            }
        }
    }

    for (int i = 0; i < mxDistance; i++) {
        if (reachable[n - 1][i] && reachable2[n - 1][i]) {
            cout << i;
            exit(0);
        }
    }
    cout << "IMPOSSIBLE";
}
