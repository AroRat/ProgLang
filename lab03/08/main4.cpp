#include <iostream>

int main()
{
    int x = 5, y = 3, z = 1;
    if ((x == y) + (x == z) == true){
        std::cout << "true";
    } else
    {
        std::cout << "false";
    }
}