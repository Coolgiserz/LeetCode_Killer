# 剑指Offer.26.树的子结构

##### 难度：中等

##### 关键词：树

##### 链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/

## 题目描述

输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

```
     3
    / \
   4   5
  / \
 1   2
```

给定的树 B：

```
   4 
  /
 1
```

返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

```
输入：A = [1,2,3], B = [3,1]
输出：false
```

示例 2：

```
输入：A = [3,4,5,1,2], B = [4,1]
输出：true
```

限制：

0 <= 节点个数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

首先判断两个根节点是否相同，若相同则继续判断对应的子节点是否相同，如果不同则递归处理A的子树与B；

什么时候退出递归（返回false）？

1. 遍历完A同时B还没遍历完；

   这个时候说明A不足以包含B，B自然不可能是A的子结构

2. 遍历完B（但不一定需要遍历完A）

   此时，足以确认是否B是A的子结构，如果是则返回true；若不是，则递归判断B是否是A->left或A->right的子结构

3. A和B的值不同

   说明匹配失败，返回false

## 代码实现

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSubStructure(TreeNode* A, TreeNode* B) {
        if(B==nullptr || A==nullptr){
            return false;
        }
        return helper(A, B) || isSubStructure(A->left, B) || isSubStructure(A->right, B);
    }

    bool helper(TreeNode* ra, TreeNode* rb){
        if(rb == nullptr){
            return true;
        }
        if(ra == nullptr){
            return false;
        }
        if(ra->val == rb->val){
            return helper(ra->left, rb->left) && helper(ra->right, rb->right);
        }else{
            return false;
        }
    }
};
```

执行用时：72 ms, 在所有 C++ 提交中击败了64.42%的用户

内存消耗：33.6 MB, 在所有 C++ 提交中击败了14.87%的用户

## 题解

