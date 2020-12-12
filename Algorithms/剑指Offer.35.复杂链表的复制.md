# 剑指Offer.35.复杂链表的复制

##### 难度：中等

##### 关键词：

##### 链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/

## 题目描述

请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

**示例 1：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e1.png) 

```
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
```



**示例 2：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e2.png)

```
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
```

**示例 3：**

**![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e3.png)**

```
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
```

**示例 4：**

```
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
```

 提示：

- -10000 <= Node.val <= 10000
- Node.random 为空（null）或指向链表中的节点。
- 节点数目不超过 1000 。


注意：本题与主站 138 题相同：https://leetcode-cn.com/problems/copy-list-with-random-pointer/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

复杂链表的复制过程中，难点在于对随机指针的复制。

### 思路1: 暴力

最简单直接的思路是：

1. 首先遍历一次链表，并进行节点的复制（确定next指针）
2. 确定random指针：计算原链表中每一个节点的random指针相对于头节点的位移，然后按照该位移对链表的副本进行random指针的赋值。该过程需要$O(N^2)$的时间复杂度

### 思路2: 引入新空间换时间

引入一个哈希表，记录原链表节点到其副本的映射，便可将复制random指针的步骤时间复杂度降低到O(1)

### 思路3: 借用空间换时间

借用原链表节点的next指针作为原链表节点到齐副本的映射，省去额外空间的引入，同样可以将时间复杂度降低到O(1)

### 测试用例

功能测试：

1. random指针指向自身；
2. 两个节点由random指针形成环

特殊输入：

1. 空链表
2. random指针为nullptr

## 代码实现

### 实现2

```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(!head){
            return nullptr;
        }
        unordered_map<Node*, Node*> _nodeMap;
        // 复制头节点
        Node* p = head;
        Node* pClonedHead = new Node(p->val);
        p = p->next;
        Node* pCloned = pClonedHead;
        pCloned->random = new Node(0);
        _nodeMap[head] = pClonedHead;

        while(p!=nullptr){
            pCloned->next = new Node(p->val); //进行克隆
            _nodeMap[p] = pCloned->next;
            pCloned = pCloned->next;
            p = p->next;
        }
        pCloned = nullptr;
        p = nullptr;

        //复制random指针
        p = head;
        pCloned = pClonedHead;
        while(p!=nullptr){
            if(p->random != nullptr){
                pCloned->random = _nodeMap[p->random];

            }else{
                pCloned->random = nullptr;
            }
            pCloned = pCloned->next;
            p = p->next;
        }
        return pClonedHead;
    }
};
```

执行用时：20 ms, 在所有 C++ 提交中击败了52.23%的用户

内存消耗：11.2 MB, 在所有 C++ 提交中击败了38.71%的用户

### 实现3

```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(!head){
            return nullptr;
        }
        connectNext(head);
        connectRandom(head);
        Node* pc = splitLinkList(head);
        return pc;
    }
    //创建链表的副本
    void connectNext(Node* head){
        Node *p = head;
        Node* pc = new Node(p->val);
        while(p!=nullptr){
            pc = new Node(p->val);
            pc->next = p->next;
            p->next = pc;
            p = pc->next;
        }
        
    }
    //将随机指针连接起来
    void connectRandom(Node* head){
        Node* p = head;
        while(p!=nullptr){
            Node* pc = p->next;
            if(p->random != nullptr){
                if(p->random->next != nullptr){
                    pc->random = p->random->next;
                }else{
                    pc->random = nullptr;
                }       
            }else{
                pc->random = nullptr;
            }

            p = pc->next;
            
        }
    }
    //将链表拆开
    Node* splitLinkList(Node* head){
        Node* p = head;
        Node* ph = p->next;
        Node* pc = ph;
        p->next = pc->next;
        p = p->next;
        while(p!=nullptr){
            pc->next = p->next;
            pc = pc->next;
            p->next = pc->next;
            p = p->next;
                    }

        return ph;
    }
};
```

执行用时：12 ms, 在所有 C++ 提交中击败了96.31%的用户

内存消耗：11.2 MB, 在所有 C++ 提交中击败了45.33%的用户

## 题解

