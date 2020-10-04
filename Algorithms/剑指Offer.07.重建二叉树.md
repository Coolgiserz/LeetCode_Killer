# 剑指Offer.07.重建二叉树

##### 难度：中等

##### 关键词：树、递归

##### 链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/

## 题目描述

输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出

```
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
```

返回如下的二叉树：

```
    3
   / \
  9  20
    /  \
   15   7
```

**限制：**

```
0 <= 节点个数 <= 5000
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

略

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
    unordered_map<int, int> _map;
    //测试用例: 1)功能测试： 2）特殊输入：序列为空；序列不能还原为二叉树（长度不同/长度相同但不一致）

    //思路
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int n = preorder.size();
        int m = inorder.size();
        if(m==0 || n==0 || m!=n ){
            return nullptr;
        }
        for(int i=0;i<m;i++){
            _map[inorder[i]] = i;
        }
        return dfs(preorder, inorder, 0, n-1, 0, n-1);
    }

    TreeNode* dfs(vector<int>& preorder, vector<int> inorder, int startPreorder, int endPreorder, int startInorder, int endInorder){
        if(startInorder>endInorder || startPreorder >endPreorder){
            return nullptr;
        }
        int rootVal = preorder[startPreorder]; //识别出根节点的值
        int rootIndex = _map[rootVal];//找到根节点在中序遍历结果中的索引
        int leftSize = rootIndex - startInorder;//计算左子树长度
        TreeNode* root = new TreeNode(rootVal);
        root->left = dfs(preorder, inorder, startPreorder+1, startPreorder+leftSize, startInorder, rootIndex-1);
        root->right = dfs(preorder, inorder, startPreorder+leftSize+1, endPreorder, rootIndex+1, endInorder);
        return root;
    }
};
```

执行用时：36 ms, 在所有 C++ 提交中击败了74.34%的用户

内存消耗：121.3 MB, 在所有 C++ 提交中击败了9.65%的用户

## 题解

