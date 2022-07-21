#include <iostream>
using namespace std;

int compare(const void *pa, const void *pb)
{
    const int *a = *(const int **)pa;
    const int *b = *(const int **)pb;

    return a[0] - b[0];
}

int main()
{
    int n;

    cin >> n;

    int** data = new int*[n];

    for (int i = 0; i < n; i++)
        data[i] = new int[2];

    for (int i = 0; i < n; i++)
    {
        int time, distance;

        cin >> time >> distance;

        data[i][0] = time;
        data[i][1] = distance;
    }

    qsort(data, n, sizeof(data[0]), compare);

    float maxV = 0;

    for (int i = 1; i < n; i++)
    {
        float speed = abs(float(data[i - 1][1] - data[i][1]) / (data[i - 1][0] - data[i][0]));

        if (speed > maxV)
            maxV = speed;
    }

    for (int i = 0; i < n; ++i)
        delete data[i];

    delete data;

    cout << maxV;
}
