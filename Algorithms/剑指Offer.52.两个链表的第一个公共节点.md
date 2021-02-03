# 剑指Offer.52.两个链表的第一个公共节点

##### 难度：简单

##### 关键词：链表、栈

##### 链接：https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/

## 题目描述

输入两个链表，找出它们的第一个公共节点。

如下面的两个链表**：**

[![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png)](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png)

在节点 c1 开始相交。

**示例 1：**

[![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_1.png)](https://assets.leetcode.com/uploads/2018/12/13/160_example_1.png)

```
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
```

**示例 2：**

[![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_2.png)](https://assets.leetcode.com/uploads/2018/12/13/160_example_2.png)

```
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
```

示例 3：

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_3.png)

```
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。
```

注意：

- 如果两个链表没有交点，返回 null.
- 在返回结果后，两个链表仍须保持原有的结构。
- 可假定整个链表结构中没有循环。
- 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
- 本题与主站 160 题相同：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

对于单链表而言，具有公共节点的两个链表有什么特点？自公共节点后面是重合的。

可以利用这个特点寻找两个链表的第一个公共节点。

1. 计算链表A、链表B的长度与长度差
2. 让较长的链表往前走几步（恰好为长度差的步数）
3. 长链表和短链表同时前进，直到找到公共节点

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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        //特殊情况：链表A或B为空
        if(!headA || !headB){
            return nullptr;
        }
        int lengthA = 1;
        int lengthB = 1;
        ListNode* pa = headA;
        ListNode* pb = headB;
        while(pa->next){
            ++lengthA;
            pa = pa->next;
        }
        while(pb->next){
            ++lengthB;
            pb = pb->next;
        }
        ListNode* headLong = nullptr;
        ListNode* headShort = nullptr;
        int d = 0;
        if(lengthA>lengthB){
            headLong = headA;
            headShort = headB;
            d = lengthA-lengthB;
        }else{
            headLong = headB;
            headShort = headA;
            d = lengthB-lengthA;
        } 
        for(int i=0;i<d;++i){
            headLong = headLong->next;
        }

        while(headLong && headShort && headLong!=headShort){
            headLong = headLong->next;
            headShort = headShort->next;
        }

        if(headLong == nullptr){
            return nullptr;
        }else{
            return headLong;
        }
    }
};
```

执行用时：52 ms, 在所有 C++ 提交中击败了62.70%的用户

内存消耗：14.2 MB, 在所有 C++ 提交中击败了91.94%的用户

## 题解

