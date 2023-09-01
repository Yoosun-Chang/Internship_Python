int main() {
    const int arraySize = 20;
    int numbers[arraySize;

    // 난수를 생성하여 배열에 저장
    std::srand(static_cast<unsigned>(std::time(nullptr)));
    for (int i = 0; i < arraySize; ++i) {
        numbers[i] = std::rand() % 100;
    }

    // 배열 요소 출력
    std::cout << "배열 요소: ";
    for (int i = 0; i < arraySize; ++i) {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;

    // 최대값 찾기
    int maxNumber = findMax(numbers, arraySize);
    std::cout << "최대값: " << maxNumber << std::endl;

    return 0;
}