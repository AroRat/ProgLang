#include <iostream>
#include <typeinfo>

int main() {
    bool x = true, y = false;
    auto a = x & y;
    std::cout << "x & y: " << typeid(a).name() << std::endl;
    auto b = x && y;
    std::cout << "x && y: " << typeid(b).name() << std::endl;
}