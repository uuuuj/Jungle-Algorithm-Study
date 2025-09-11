// https://school.programmers.co.kr/learn/courses/30/lessons/120895

#include <string>
#include <vector>

using namespace std;

string solution(string my_string, int num1, int num2) {
    char temp = my_string[num1];
    my_string[num1] = my_string[num2];
    my_string[num2] = temp;
    
    return my_string;
}