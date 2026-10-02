#include <iostream>

int main() {
    int total = 15;
    int count = 4;

    double average = static_cast<double>(total) / count;
    std::cout << "Среднее значение: " << average;
}