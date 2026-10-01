#include <iostream>

int main()
{
    int x = 5, y = 5, z = 3;
    if ((x == y) + (x == z) == true){
        std::cout << "true";
    } else
    {
        std::cout << "false";
    }
}