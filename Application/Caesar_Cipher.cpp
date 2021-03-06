#include <iostream>
#include <string.h>

using namespace std;
// Function which returns an encrypted string, given the 'shift' n
string caesar_encrypt(char* str, int n)
{
    int i = 0;
    while (str[i] != '\0')
    {
        //Big letters' clause
        if(((int)str[i] > 64 && (int)str[i] < 91))
        {
            int temp = 0;
            temp = (((int) str[i]) + n - 65) % 26 + 65;
            str[i] = (char)temp;
        }

        //Small letters' clause
        if(((int)str[i] > 96 && (int)str[i] < 123))
        {
            int temp = 0;
            temp = (((int) str[i]) + n - 97) % 26 + 97;
            str[i] = (char)temp;
        }

        ++i;
    }

    return string(str);
}

int main(){

        char *str = new char;
        cin >> str;

        int n;
        cin >> n;

        cout << caesar_encrypt(str, n);

    return 0;
}
