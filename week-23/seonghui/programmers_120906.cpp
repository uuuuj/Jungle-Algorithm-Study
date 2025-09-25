// https://school.programmers.co.kr/learn/courses/30/lessons/120906

#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    
    while (n > 0) {
        answer += n % 10;
        n /= 10;
    }
    
    return answer;
}