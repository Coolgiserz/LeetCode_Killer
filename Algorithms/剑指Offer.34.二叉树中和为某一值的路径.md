# 剑指Offer.34.二叉树中和为某一值的路径

##### 难度：中等

##### 关键词：

##### 链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/

## 题目描述

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

```
[
   [5,4,11,2],
   [5,8,4,5]
]
```

提示：

节点总数 <= 10000
注意：本题与主站 113 题相同：https://leetcode-cn.com/problems/path-sum-ii/



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

递推参数： 当前节点 root ，当前目标值 target 。
终止条件： 若节点 root 为空，则直接返回。
递推工作：
路径更新： 将当前节点值 root.val 加入路径 path ；
目标值更新： target = target - root.val（即目标值 target 从 sum 减至 0 ）；
路径记录： 当 ① root 为叶节点 且 ② 路径和等于目标值 ，则将此路径 path 加入 result 。
先序遍历： 递归左 / 右子节点。
路径恢复： 向上回溯前，需要将当前节点从路径 path 中删除，即执行 path.pop() 。

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
    vector<vector<int>> result;
    //是叶子节点就看看路径和是否满足条件，否则回溯
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<int> res;
        helper(root, sum, res);
        return result;

    }

    void helper(TreeNode* root, int sum, vector<int>& res){
        if(!root){//空结点
            return;
        }
        res.emplace_back(root->val);
        //判断是否是叶子节点
        if(!root->left && !root->right){
            if(root->val==sum){
                //满足条件
                result.emplace_back(res);
            }else{
                //不满足条件
                res.pop_back();
                return;
            }
        }
        helper(root->left, sum-root->val, res);
        helper(root->right, sum-root->val, res);
      
        res.pop_back();
        return;
    }
};
```

执行用时：20 ms, 在所有 C++ 提交中击败了40.96%的用户

内存消耗：19.9 MB, 在所有 C++ 提交中击败了49.61%的用户

#### 优化

减少不必要的判断。

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
    vector<vector<int>> result;
    //是叶子节点就看看路径和是否满足条件，否则回溯
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<int> res;
        helper(root, sum, res);
        return result;

    }

    void helper(TreeNode* root, int sum, vector<int>& res){
        if(!root){//空结点
            return;
        }
        res.emplace_back(root->val);
        //判断是否是叶子节点
        if(!root->left && !root->right){
            if(root->val==sum){
                //满足条件
                result.emplace_back(res);
            }
        }
        helper(root->left, sum-root->val, res);
        helper(root->right, sum-root->val, res);
        
        res.pop_back();
        return;
    }
};
```

执行用时：12 ms, 在所有 C++ 提交中击败了85.70%的用户

内存消耗：20 MB, 在所有 C++ 提交中击败了42.17%的用户

## 题解

