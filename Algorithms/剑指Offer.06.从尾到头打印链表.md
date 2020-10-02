# 剑指Offer.06.从尾到头打印链表

##### 难度：简单

##### 关键词：链表

##### 链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/

## 题目描述

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：

```
输入：head = [1,3,2]
输出：[2,3,1]
```

限制：

0 <= 链表长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

分两种情况讨论，更改链表结构进行打印 或 不更改链表结构进行打印。

通常认为打印操作是只读操作，所以先考虑后一种情况

### 思路1

借助栈这一后进先出的数据结构实现从尾到头打印。

使用栈来存储的空间复杂度O(n)。遍历栈+链表时间复杂度O(n)

### 思路2

递归本质也是借助栈，考虑在打印之前先递归打印链表的下一个节点。

【注】可能存在的问题是链表过长时无法正常工作，因为函数调用栈空间有限

### 思路3

从头到尾遍历，反转结果数组。

好处是不需要引入栈。最大的开销在于反转数组。

### 思路4

先反转链表，再从头到尾遍历。

## 代码实现

### 实现1：栈

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
    //思路：递归/栈
    vector<int> reversePrint(ListNode* head) {
        vector<int> result;
        if(head == nullptr){
            return result;
        }
        stack<int> _stack;
        ListNode* node = head;
        _stack.push(node->val);
        while(node->next){
            node = node->next;
            _stack.push(node->val);
        }
        while(!_stack.empty()){
            result.emplace_back(_stack.top());
            _stack.pop();
        }
        return result;
    }
};
```

执行用时：8 ms, 在所有 C++ 提交中击败了71.47%的用户

内存消耗：8.8 MB, 在所有 C++ 提交中击败了36.08%的用户

### 实现2：递归

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
    vector<int> reversePrint(ListNode* head) {
        vector<int> result;
        helper(head, result);
        return result ;
    }
    void helper(ListNode* node, vector<int>& result){
        
        if(node == nullptr){
            return;
        }
        helper(node->next, result);
        result.emplace_back(node->val);

    }
  
};
```

执行用时：8 ms, 在所有 C++ 提交中击败了71.47%的用户

内存消耗：8.9 MB, 在所有 C++ 提交中击败了29.60%的用户

### 实现3：遍历一遍，反转数组

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
  vector<int> reversePrint(ListNode* head) {
        vector<int> result;
        if(head == nullptr){
            return result;
        }
        ListNode* node = head;
        result.emplace_back(node->val);
        while(node->next){
            node = node->next;
            result.emplace_back(node->val);
        }
        reverse(result.begin(), result.end());
        return result ;
    }
};
```

执行用时：4 ms, 在所有 C++ 提交中击败了96.56%的用户

内存消耗：8.6 MB, 在所有 C++ 提交中击败了68.71%的用户

### 实现4:  反转链表再打印

暂略

## 小结

### 关于std::reverse

https://en.cppreference.com/w/cpp/algorithm/reverses



