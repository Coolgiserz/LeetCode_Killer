# 剑指Offer.55-2.平衡二叉树

##### 难度：简单

##### 关键词：树

##### 链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/

## 题目描述

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

```
    3
   / \
  9  20
    /  \
   15   7
```


返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

         1
        / \
       2   2
      / \
     3   3
     / \
    4   4
返回 false 。

限制：

1 <= 树的结点个数 <= 10000
注意：本题与主站 110 题相同：https://leetcode-cn.com/problems/balanced-binary-tree/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

### 思路1: 自顶向下，递归

计算左右子树的高度差，如果相差绝对值大于1则不平衡，若小于等于1则递归判断左右子树是否平衡。所有子树均满足左右子树高度差在1之内才表明二叉树是平衡二叉树。

### 思路2: 后序遍历，自底向上

思路1虽然简单直白，但是自顶向下的计算会出现重复计算的情况，可以考虑如何避免重复计算子树的深度：自底向上。

### 测试用例

```
[3,9,20,null,null,15,7]
[1,2,2,3,3,null,null,4,4]
[1]
[1,2]
```



## 代码实现

### 实现1

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
    bool isBalanced(TreeNode* root) {
        if(!root){
            return true;
        }
        int left = getDepth(root->left);
        int right = getDepth(root->right);
        int diff = left - right;
        if(diff > 1 || diff < -1){
            return false;
        }
        return isBalanced(root->left) && isBalanced(root->right);
    }

    int getDepth(TreeNode* root){
        if(nullptr == root){
            return 0;
        }
        return 1+max(getDepth(root->left), getDepth(root->right));
    }
};
```

执行用时：16 ms, 在所有 C++ 提交中击败了84.67%的用户

内存消耗：20.3 MB, 在所有 C++ 提交中击败了92.18%的用户

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
    bool isBalanced(TreeNode* root) {
        if(!root){
            return true;
        }
        int depth = 0;
        return isBalancedCore(root, depth);
    }

    bool isBalancedCore(TreeNode* root, int& depth){
        if(nullptr == root){
            depth = 0;
            return true;
        }
        int left, right;
        bool lt = isBalancedCore(root->left, left);
        bool rt = isBalancedCore(root->right, right);
        int diff = left - right;
        if(lt && rt){
             if(diff>1 || diff<-1){
                return false;
            }else{
                depth = 1+max(left, right);
                return true;
            }
        }
       
        return false;
        
    }
};
```

执行用时：8 ms, 在所有 C++ 提交中击败了99.24%的用户

内存消耗：21.1 MB, 在所有 C++ 提交中击败了64.48%的用户

## 题解

