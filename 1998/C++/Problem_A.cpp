#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    cin.ignore();
    while(n--) {
        string s;
        vector<string> v(1);
        getline(cin, s);
        for(char c : s) {
            if(c != ' ') {
                v.back() += c;
            } else {
                v.push_back("");
            }
        }
        for(string w : v) {
            cout << (w.length() == 4 ? "****" : w) << " ";
        }
        cout << "\n";
    }
}
