// https://school.programmers.co.kr/learn/courses/30/lessons/120845

#include <string>
#include <vector>

using namespace std;

int solution(vector<int> box, int n) {
    
    return (box[0] / n) * (box[1] / n) * (box[2] / n);
}