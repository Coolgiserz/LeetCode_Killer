# 剑指Offer.54.二叉搜索树的第k大节点

##### 难度：简单

##### 关键词：树

##### 链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/

## 题目描述

给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:

```
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
```

示例 2:

```
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
```

**限制：**

1 ≤ k ≤ 二叉搜索树元素个数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

中序遍历的过程中记录遍历顺序。

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
    int count = 0;
    int kthLargest(TreeNode* root, int k) {
        if( k==0 || !root){
            return -1;
        }
        int result = -1;
        helper(root, k, result);
        return result;
    }

    void helper(TreeNode* node, int k, int& result){
       
        if(node->right){
            helper(node->right, k, result);
        }
        if(++count == k){
            result = node->val;
            return;
        }
        if(node->left){
            helper(node->left, k, result);
        }

    }
};
```

执行用时：16 ms, 在所有 C++ 提交中击败了98.19%的用户

内存消耗：23.4 MB, 在所有 C++ 提交中击败了95.03%的用户

## 题解

