//not fast enough
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    vector<int> lines;
    int x;
    while (cin >> x) {
        lines.push_back(x);
    }
    sort(lines.begin(), lines.end());
    lines.erase(unique(lines.begin(), lines.end()), lines.end());
    int initNum;
    for (int i = 0; i < lines.size(); i++) {
        initNum += lines[i];
        if (find(lines.begin(), lines.end(), initNum) == lines.end()) {
            cout << initNum << endl;
        } else {
            initNum += lines[i];
        }
    }
    return 0;
}