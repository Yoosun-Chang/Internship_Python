#include <iostream>
#include <string>
#include <vector>

class Student {
public:
    Student(const std::string& name, int age) : name(name), age(age) {}

    void displayInfo() const {
        std::cout << "이름: " << name << ", 나이: " << age << std::endl;
    }

private:
    std::string name;
    int age;
};

int main() {
    std::vector<Student> students;

    while (true) {
        std::cout << "1. 학생 정보 입력, 2. 전체 학생 목록 출력, 3. 종료: ";
        int choice;
        std::cin >> choice;

        if (choice == 1) {
            std::string name;
            int age;

            std::cout << "이름 입력: ";
            std::cin >> name;
            std::cout << "나이 입력: ";
            std::cin >> age;

            students.emplace_back(name, age);
            std::cout << "학생 정보가 입력되었습니다." << std::endl;
        } else if (choice == 2) {
            std::cout << "전체 학생 목록:" << std::endl;
            for (const Student& student : students) {
                student.displayInfo();
            }
        } else if (choice == 3) {
            std::cout << "프로그램을 종료합니다." << std::endl;
            break;
        } else {
            std::cout << "잘못된 선택입니다. 다시 선택하세요." << std::endl;
        }
    }

    return 0;
}
