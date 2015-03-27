#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

float fill_tetrahedron (int num)
{
    return pow (num, 3) / ((sqrt (2)) * 6 * 1000);
}

int main(){
    int number;
    cin >> number;

    cout << fixed << setprecision(2) << fill_tetrahedron(number);

    return 0;
}
