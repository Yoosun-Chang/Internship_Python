#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <string>

int main() {
    std::string filename = "sample.txt"; // 분석할 파일 이름
    std::ifstream inputFile(filename);

    if (!inputFile.is_open()) {
        std::cerr << "파일을 열 수 없습니다." << std::endl;
        return 1;
    }

    std::map<std::string, int> wordFrequency;

    std::string line;
    while (std::getline(inputFile, line)) {
        std::istringstream iss(line);
        std::string word;
        while (iss >> word)) { // 여기서 괄호 위치 오류
            // 단어 처리: 구두점 제거 등
            // 여기서는 단순히 모든 문자를 소문자로 변환
            for (char &c : word) {
                c = std::tolower(c);
            }
            wordFrequency[word]++;
        }
    }

    inputFile.close();

    std::cout << "파일 내 단어 빈도:" << std::endl;
    for (const auto &pair : wordFrequency) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    return 0;
}
