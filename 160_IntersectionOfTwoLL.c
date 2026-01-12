#include <stdio.h>

 //Definition for singly-linked list.
 struct ListNode {
     int val;
     struct ListNode *next;
 };
 
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode *tempB = headB;
    while(headA) {
        while(tempB) {
            if (headA == tempB) {
                return headA;
            }
            tempB = tempB->next;
        }
        tempB = headB;
        headA = headA->next;
    }
    return NULL;
}