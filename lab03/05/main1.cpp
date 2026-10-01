#include <iostream>

typedef int IntArray[5];

int main() {
    IntArray numbers = {10, 20, 30, 40, 50};
    int sum = 0;

    for (int i = 0; i < 5; i++) {
        sum += numbers[i];
    }
    std::cout << "Сумма элементов: " << sum;
}