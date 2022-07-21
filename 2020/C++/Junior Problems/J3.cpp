#include <iostream>
#include <string>

using namespace std;

int main()
{
    int N;
    cin >> N;
    int min_x = 100;
    int min_y = 100;
    int max_x = 0;
    int max_y = 0;
    for (int i = 0; i < N; i++)
    {
        string line;
        cin >> line;
        int x = stoi(line.substr(0, line.find(",")));
        int y = stoi(line.substr(line.find(",")+1, -1));
        if (x < min_x)
        {
            min_x = x;
        }
        if (x > max_x)
        {
            max_x = x;
        }
        if (y < min_y)
        {
            min_y = y;
        }
        if (y > max_y)
        {
            max_y = y;
        }
    }
    min_x = (min_x > 0) ? min_x - 1 : min_x; // ternary operator in java
    min_y = (min_y > 0) ? min_y - 1 : min_y;
    max_x = (max_x < 100) ? max_x + 1 : max_x;
    max_y = (max_y < 100) ? max_y + 1 : max_y;
    cout << min_x << "," << min_y << endl;
    cout << max_x << "," << max_y << endl;
    return 0;
}
