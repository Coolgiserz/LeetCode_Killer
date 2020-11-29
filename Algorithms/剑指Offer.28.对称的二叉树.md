# 剑指Offer.28.对称的二叉树

##### 难度：简单

##### 关键词：树

##### 链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/

## 题目描述

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

        1
       / \
      2   2
     / \ / \
    3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

        1
       / \
      2   2
       \   \
       3    3
    
示例 1：

```
输入：root = [1,2,2,3,4,4,3]
输出：true
```

示例 2：

```
输入：root = [1,2,2,null,3,null,3]
输出：false
```


限制：

0 <= 节点个数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

### 思路1

简单粗暴的方法是，镜像翻转后判断两颗树是否相等，如是，则原树是对称的二叉树。

### 思路2

前序遍历与对称前序遍历得到的序列相同则表明树是对称的二叉树。

实现过程可以是递归的。

## 代码实现

### 实现1

### 实现2

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
    bool isSymmetric(TreeNode* root) {
        return helper(root, root);
    }

    bool helper(TreeNode* root1, TreeNode* root2){
        //全为空
        if(!root1 && !root2){
            return true;
        }
        //有一个为空
        if(!root1 || !root2){
            return false;
        }

        //都不为空
        if(root1->val != root2->val){
            return false;
        }
        return helper(root1->left, root2->right) &&  helper(root1->right, root2->left);

    }
};
```

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户

内存消耗：16.4 MB, 在所有 C++ 提交中击败了17.43%的用户

## 题解

