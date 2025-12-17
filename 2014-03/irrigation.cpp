#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    freopen("irrigation.in", "r", stdin);
    freopen("irrigation.out", "w", stdout);

    // std::cout << "Hello World" << std::endl;

    int n;
    int c;
    cin >> n >> c;

    vector<pair<int,int>> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i].first >> a[i].second;
    }

    long long BIG = int(1e18);
    vector<long long> key(n, BIG);
    vector<bool> inMST(n, false);

    key[0] = 0;

    int ans = 0;
    for (int i = 0; i < n; i++) {
        int u = -1;
        for (int v = 0; v < n; v++) {
            if (!inMST[v] && (u == -1 || key[v] < key[u])) {
                u = v;
            }
        }
        
        if (key[u] == BIG) {
            cout << -1;
            exit(0);
        }

        inMST[u] = true;
        ans += key[u];

        for (int v = 0; v < n; v++) {
            long long alt = (a[u].first - a[v].first) * (a[u].first - a[v].first) + (a[u].second - a[v].second) * (a[u].second - a[v].second);
            if (alt < c) {
                continue;
            }
            if (!inMST[v] && alt < key[v]) {
                key[v] = alt;
            }
        }
    }
    
    cout << ans;
}
