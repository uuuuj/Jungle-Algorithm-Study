// https://school.programmers.co.kr/learn/courses/30/lessons/120844

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers, string direction) {
    vector<int> answer;
    
    if (direction == "right") { // right

        answer.push_back(*(numbers.end()-1));
        answer.insert(answer.end(), numbers.begin(), numbers.end()-1);
    }
    else { // left
        answer.insert(answer.end(), numbers.begin()+1, numbers.end());
        answer.push_back(*(numbers.begin()));
    }
    
    return answer;
}