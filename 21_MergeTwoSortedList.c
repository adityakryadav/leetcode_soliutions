// Definition for singly-linked list.
struct ListNode {
     int val;
     struct ListNode *next;
};
 
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode *lt, *head;
    int k = 0;
    while (list1 || list2) {
        if (list1) {
            if (list2) {
                if (list1->val > list2->val) {
                    if (k == 0) {
                        head = list2;
                        list2 = list2->next;
                        lt = head;
                        k = 1;
                    }
                    else {
                        lt->next = list2;
                        lt = lt->next;
                        list2 = list2->next;
                    } 
                }
                else {
                    if (k == 0) {
                        head = list1;
                        list1 = list1->next;
                        lt = head;
                        k = 1;
                    }
                    else {
                        lt->next = list1;
                        lt = lt->next;
                        list1 = list1->next;
                    }
                    
                }
            }
            else {
                if (k == 0) {
                        head = list1;
                        list1 = list1->next;
                        lt = head;
                        k = 1;
                }
                else {
                    lt->next = list1;
                    lt = lt->next;
                    list1 = list1->next;
                }
            }
        }
        else {
            if (k == 0) {
                head = list2;
                list2 = list2->next;
                lt = head;
                k = 1;
            }
            else {
                lt->next = list2;
                lt = lt->next;
                list2 = list2->next;
            } 
        }
    }
    return head;
}