#include <iostream>

int main()
{
    int a = 240;            // десятеричная запись
    int b = 0360;           // восьмеричная запись (0)
    int c = 0b11110000;     // двоичная запись (0b)
    int d = 0xF0;           // шестнадцатеричная запись (0x)

    int e = 110U;           // беззнаковый тип литерала
    int f = 110L;           // long
    int g = 110LL;          // long long
    int h = 110UL;          // беззнаковый long
    int i = 110ULL;         // беззнаковый long long

    std::cout << a << std::endl;
    std::cout << b << std::endl;
    std::cout << c << std::endl;
    std::cout << d << std::endl;
}
