// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/

/**
 * Definition for singly-linked list. 
 */
 struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
 
class Solution {
public:
    int getDecimalValue(ListNode* head) {
        int result = head->val;
        auto nextNode = head->next;
        while(nextNode) {
            result <<= 1;
            result += nextNode->val;

            nextNode = nextNode->next;
        }

        return result;
    }
};
