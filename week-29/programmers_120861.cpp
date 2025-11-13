// https://school.programmers.co.kr/learn/courses/30/lessons/120861

#include <string>
#include <vector>
#include <cmath>

using namespace std;

vector<int> solution(vector<string> keyinput, vector<int> board) {
    vector<int> answer({0,0});
    
    auto x = answer.begin();
    auto y = answer.begin() + 1;
    
    int width = board[0] / 2;
    int height = board[1] / 2;
    
    for (string key : keyinput) {
        switch (key[0]) {
            case 'l' :
                if (*x > (width*-1)) --*x;
                break;
            case 'r' :
                if (*x < width) ++*x;
                break;
            case 'u' :
                if (*y < height) ++*y;
                break;
            case 'd' :
                if (*y > (height*-1)) --*y;
                break;
        }
    }
    
    return answer;
}