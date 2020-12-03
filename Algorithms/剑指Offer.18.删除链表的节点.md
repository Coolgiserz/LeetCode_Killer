# 剑指Offer.18.删除链表的节点

##### 难度：简单

##### 关键词：链表

##### 链接：https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/

## 题目描述

给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

```
输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
```

示例 2:

```
输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
```


说明：

- 题目保证链表中节点的值互不相同
- 若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

删除节点需要知道前一个节点，所以遍历链表的过程中需要记录当前节点cur的前一个节点pre，遍历到待删除节点时，将pre的next指针指为cur的下一个节点，并收回cur占用的内存，返回头节点即可。

考虑特殊情况，如果链表中没有相应节点怎么办？直接返回原链表

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
    //
    ListNode* deleteNode(ListNode* head, int val) {
        if(!head){
            return nullptr;
        }

        ListNode* pre = head;
        ListNode* cur = head->next;
        if(!cur){
            if(pre->val == val){
                return nullptr;
            }else{
                return head;
            }
        }else{
            if(pre->val == val){
                return cur;
            }
        }
        while(cur){
            if(cur->val == val){
                pre->next = cur->next;
                return head;
            }
            pre = cur;
            cur = cur->next;
        }
        return head;

    }
};
```

执行用时：20 ms, 在所有 C++ 提交中击败了25.83%的用户

内存消耗：9.4 MB, 在所有 C++ 提交中击败了41.93%的用户

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
    ListNode* deleteNode(ListNode* head, int val) {
        if(!head){
            return nullptr;
        }

        ListNode* pre = nullptr;
        ListNode* cur = head;
        while(cur){
            if(cur->val == val){
                if(pre == nullptr){
                    return cur->next;
                }else{
                    pre->next = cur->next;
                    return head;
                }
                
            }
            pre = cur;
            cur = cur->next;
        }
        return head;

    }
};
```

执行用时：16 ms, 在所有 C++ 提交中击败了60.73%的用户

内存消耗：9.5 MB, 在所有 C++ 提交中击败了18.04%的用户

## 题解

