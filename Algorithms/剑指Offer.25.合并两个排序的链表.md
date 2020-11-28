# 剑指Offer.25.合并两个排序的链表

##### 难度：简单

##### 关键词：

##### 链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/

## 题目描述

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

```
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```

限制：

0 <= 链表长度 <= 1000

注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

测试用例：

```
特殊情况：l1或l2为空。
```

### 思路

递归合并。

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
    
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
      	//处理特殊情况
        if(!l1){
            return l2;
        }else if(!l2){
            return l1;
        }
      	//递归进行合并
        if(l1->val < l2->val){
            l1->next = mergeTwoLists(l1->next, l2);
            return l1;
        }else{
            l2->next = mergeTwoLists(l1, l2->next);
            return l2;
        }
    }
};
```

执行用时：40 ms, 在所有 C++ 提交中击败了84.96%的用户

内存消耗：19.2 MB, 在所有 C++ 提交中击败了31.40%的用户

## 题解

