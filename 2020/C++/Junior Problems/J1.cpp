#include <iostream>
#include <string>
using namespace std;

int main() {
    int S,M,L;
    cin >> S >> M >> L;
    int score = 1*S+2*M+3*L;
    if (score>=10){
        cout << "happy";
    }
    else{
        cout << "sad";
    }
    return 0;
}
