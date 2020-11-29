# 剑指Offer.27.二叉树的镜像

##### 难度：简单

##### 关键词：树

##### 链接：https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/

## 题目描述

请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

```
     4
   /   \
  2     7
 / \   / \
1   3 6   9
```

镜像输出： 

```
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

示例 1：

```
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
```


限制：

0 <= 节点个数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

### 思路1: 递归

递归的过程中交换每个节点的左右子节点。

### 思路2: 循环

用一个辅助栈模拟递归过程的栈。遍历二叉树的过程中交换节点的左右子节点。

## 代码实现

### 实现1: 递归

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
    TreeNode* mirrorTree(TreeNode* root) {
        if(!root){
            return nullptr;
        }
        TreeNode* tmp = root->left;
        root->left = mirrorTree(root->right);
        root->right = mirrorTree(tmp);
        return root;
    }
};
```

执行用时：4 ms, 在所有 C++ 提交中击败了59.65%的用户

内存消耗：9.5 MB, 在所有 C++ 提交中击败了9.72%的用户

上面程序中效率较低的部分在对子树递归执行镜像操作中还进行了赋值操作。

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
    TreeNode* mirrorTree(TreeNode* root) {
        if(!root){
            return nullptr;
        }
        TreeNode* tmp = root->left;
        root->left = root->right;
        root->right = tmp;
        mirrorTree(root->right);
        mirrorTree(root->left);
        return root;
    }
};
```

执行用时：0ms, 在所有 C++ 提交中击败了100%的用户

内存消耗：9.5 MB, 在所有 C++ 提交中击败了9.72%的用户

### 实现2: 循环+辅助栈

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
    TreeNode* mirrorTree(TreeNode* root) {
        if(!root){
            return nullptr;
        }
        stack<TreeNode*> _stack;
        _stack.push(root);
        while(!_stack.empty()){
            TreeNode* node = _stack.top();
            _stack.pop();
            if(node->left){
                _stack.push(node->left);
            }
            if(node->right){
                _stack.push(node->right);
            }
            TreeNode* tmp = node->left;
            node->left = node->right;
            node->right = tmp;
        }
        return root;
    }
};
```

执行用时：4 ms, 在所有 C++ 提交中击败了59.65%的用户

内存消耗：9.5 MB, 在所有 C++ 提交中击败了5.21%的用户

## 小结

可以通过画图让抽象的（新）概念具体化。

