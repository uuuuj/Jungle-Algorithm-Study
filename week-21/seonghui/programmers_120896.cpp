// https://school.programmers.co.kr/learn/courses/30/lessons/120896

#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(string s) {
    string answer = "";
    map<char, int> m;
    
    for (char c : s) {
        ++m[c];
    }
    
    for (auto [c, i] : m) {
        if (i == 1) answer +=c;
    }
    
    return answer;
}