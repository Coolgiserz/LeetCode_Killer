# 剑指Offer.22.链表中倒数第k个节点

##### 难度：简单

##### 关键词：链表、双指针

##### 链接：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/

## 题目描述

输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

示例：

```
给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.
```



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

### 思路： 双指针

让一个指针先走k步，然后两个指针继续向前，等到前面那个指针到null时，后面那个指针便指向了第n-k+1个节点

要注意特殊情况：链表为空或者k大于链表长度

时间复杂度为O(2N-k+1)

空间复杂度O(1)

## 代码实现

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
    //特殊输入：链表为空或者k大于链表长度
    //
    //思路： 双指针：一个指针先走k步，然后两个指针继续向前，等到前面那个指针到null时，后面那个指针便指向了第n-k+1个节点
    ListNode* getKthFromEnd(ListNode* head, int k) {
        if(!head || k < 1){
            return nullptr;
        }
        ListNode* p = head;
        int i = 0;
        while(i<k-1){
            p = p->next;
            
            ++i;
        }
        if(!p){
            return nullptr;
        }
        ListNode* q = head;
        while(p->next){
            p = p->next;
            q = q->next;
        }
        return q;

    }
};
```

执行用时：8 ms, 在所有 C++ 提交中击败了54.04%的用户

内存消耗：10.8 MB, 在所有 C++ 提交中击败了7.91%的用户

## 小结

