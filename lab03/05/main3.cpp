#include <iostream>

int main() {
    int x = 100;

    decltype(x) y = 200;
    std::cout << "x = " << x << ", y = " << y << std::endl;
    std::cout << "Сумма: " << x + y;
}