//not fast enough
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <cassert>

using namespace std;
bool isValid(const string &word) {
    size_t length = word.length();
    vector<string> subs;
    for (size_t i = 0; i < length - length / 2 + 1; i++) {
        subs.push_back(word.substr(i, length / 2));
    }

    set<string> uniqueSubs;
    copy(begin(subs), end(subs), inserter(uniqueSubs, end(uniqueSubs)));

    return uniqueSubs.size() == subs.size();
}

void perms(const string &head, const string &tail) {
    if (head.empty()) {
        if (isValid(tail)) {
            cout << tail << endl;
            exit(0);
        }
        return;
    }

    for (size_t i = 0; i < head.length(); i++) {
        perms(head.substr(0, i) + head.substr(i + 1), tail + head[i]);
    }
}
int main() {
    vector<string> lines;
    string word;
    getline(cin, word);
    lines.push_back(word);

    string tail = "";
    perms(word, tail);
    cout << -1 << endl;

    return 0;
}


