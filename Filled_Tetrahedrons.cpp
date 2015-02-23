#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;
// Function which calculates the volume of a regular tetrahedron in litres
float fill_tetrahedron (int num)
{
    return pow (num, 3) / ((sqrt (2)) * 6 * 1000);
}
// Function which returns the max number of tetrahedrons filled with the water given
int tetrahedron_filled (vector<int> tetrahedrons, int water)
{
    int numFilled = 0;
    int sizeOFTets = tetrahedrons.size();
    sort(tetrahedrons.begin(), tetrahedrons.end());

    for(int i = 0; i < sizeOFTets; ++i)
    {
        if(water >= fill_tetrahedron(tetrahedrons.at(i)))
        {
            water = (float)water - fill_tetrahedron(tetrahedrons.at(i));
            numFilled++;
        }
        else return numFilled;
    }

    return numFilled;
}

int main(){
    cout << "How many tetrahedrons: ";
    int numOfTetrahedron;
    cin >> numOfTetrahedron;

    vector<int> listOfInts;
    cout << "Enter the sides: ";
    for(int i = 0; i < numOfTetrahedron; ++i)
    {
        int number;
        cin >> number;
        listOfInts.push_back(number);
    }

    int water;
    cout << "Enter the amount of water: ";
    cin >> water;

    cout << tetrahedron_filled(listOfInts, water);

    return 0;
}
