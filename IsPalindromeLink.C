// https://leetcode-cn.com/problems/palindrome-linked-list/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    /* space = O(n) */
    bool isPalindrome_n(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* pre = NULL;
        while (fast != NULL) {
            //cout << fast->val << "," << slow->val << endl;
            fast = fast->next;
            if (fast != NULL) {
                fast = fast->next;
                ListNode* tmp = pre;
                pre = new ListNode(slow->val);
                pre->next = tmp;
                //cout << pre->val << endl;
            }
            slow = slow->next;
        }
        //cout << "slow = " << slow->val << endl;
        while (slow != NULL) {
            //cout << slow->val << "," << pre->val << endl;
            if (slow->val != pre->val) {
                return false;
            }
            slow = slow->next;
            pre = pre->next;
        }
        return true;
    }
    
    /* space = O(1); reverse the first half part of the linked list*/
    bool isPalindrome(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* pre = NULL;
        while (fast != NULL) {
            //cout << "before: " << fast->val << "," << slow->val << endl;
            ListNode* tmp_slow = slow;
            slow = slow->next;
            fast = fast->next;
            if (fast != NULL) {
                fast = fast->next;
                ListNode* tmp_pre = pre;
                pre = tmp_slow;
                pre->next = tmp_pre;
            }
            //cout << "after: " << slow->val << "," << pre->val<< endl;
        }
        
        while (slow != NULL) {
            if (slow->val != pre->val) {
                return false;
            }
            slow = slow->next;
            pre = pre->next;
        }
        return true;
    }
};
