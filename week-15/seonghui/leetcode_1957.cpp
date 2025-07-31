// https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/

#include <string>

using namespace std;

class Solution {
public:
    string makeFancyString(string s) {
        char prev= 'A';
        int cnt= 1;
        string result="";
        for (char c : s) {
            if ( prev== c) { 
                ++cnt;
            }
            else { 
                prev= c;
                cnt= 1; 
            }
            if( cnt < 3) result += c;
        }
        return result;
    }
};