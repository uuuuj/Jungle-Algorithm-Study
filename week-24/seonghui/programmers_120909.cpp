// https://school.programmers.co.kr/learn/courses/30/lessons/120909

#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int n) {
    double result = sqrt(n);
    if (floor(result) == result) return 1;
    
    return 2;
}