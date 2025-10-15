// https://school.programmers.co.kr/learn/courses/30/lessons/120583

#include <string>
#include <vector>

using namespace std;

int solution(vector<int> array, int n) {
    int answer = 0;
    
    for (int a : array) {
        if(a == n) ++answer;
    }
    
    return answer;
}