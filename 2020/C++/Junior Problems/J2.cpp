#include <iostream>
#include <string>
using namespace std;

int main()
{
    int P,N,R;
    cin >> P >> N >> R;
    int num = N;
    int num2 = N;
    int c = 0;
    while (true){
        c++;
        num2 = num2*R;
        num+=num2;
        if (num>P){
            cout << c;
            break;
        }
    }
    return 0;
}
