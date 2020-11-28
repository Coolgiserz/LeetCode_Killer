# 剑指Offer.24.反转链表

##### 难度：简单

##### 关键词：

##### 链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/

## 题目描述

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:

```
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```


限制：

- 0 <= 节点个数 <= 5000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

### 思路1

需要一个指针遍历链表，但要进行反转需要在遍历的时候同时保存前一个节点和后一个节点。

## 代码实现

### 实现1

```c++
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
    //特殊输入: nullptr
   
    ListNode* reverseList(ListNode* head) {
        if(!head || !head->next){
            return head;
        }

        ListNode* prev = nullptr;
        ListNode* curr = head;
        while(curr->next){
            ListNode* tmp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = tmp;
        }
        if(!curr->next){
            curr->next = prev;
        }
        return curr;
    }
};
```

执行用时：4 ms, 在所有 C++ 提交中击败了99.87%的用户

内存消耗：8.6 MB, 在所有 C++ 提交中击败了13.13%的用户

## 题解

