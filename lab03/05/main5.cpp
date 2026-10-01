#include <iostream>

int main() {
    int arr[] = {4, 8, 15, 16, 23, 42};

    int count = sizeof(arr) / sizeof(arr[0]);
    std::cout << "Размер массива в байтах: " << sizeof(arr) << std::endl;
    std::cout << "Количество элементов в массиве: " << count;
}