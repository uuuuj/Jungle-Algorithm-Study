// https://school.programmers.co.kr/learn/courses/30/lessons/120848

#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int i = 1;
    while (n >= i) {
        n /= i++;
    }
    
    return i-1;
}