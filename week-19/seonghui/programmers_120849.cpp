// https://school.programmers.co.kr/learn/courses/30/lessons/120849

#include <string>
#include <vector>

using namespace std;

string solution(string my_string) {
    string vowel = "aeiou", answer = "";
    
    for (char c : my_string ) {
        if (vowel.find(c)==string::npos) answer += c;
    }
    
    return answer;
}