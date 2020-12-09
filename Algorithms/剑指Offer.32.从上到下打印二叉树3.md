# 剑指Offer.32.从上到下打印二叉树3

##### 难度：中等

##### 关键词：树、广度优先遍历

##### 链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/

## 题目描述

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    		3
       / \
      9  20
        /  \
       15   7

返回其层次遍历结果：

```
[
  [3],
  [20,9],
  [15,7]
]
```


提示：

- 节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

打印奇数层时，从左到右将子节点存入一个栈中；打印偶数层时，从右到左将子节点存入另一个栈中。



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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if(!root){
            return result;
        }

        stack<TreeNode*> _stack[2];
        int current = 0;
        int next = 1;
        _stack[current].push(root);
        result.push_back(vector<int>());
        int ind = 0;
        while(!_stack[0].empty() || !_stack[1].empty()){

            if(current == 0){//打印奇数层
                TreeNode* node = _stack[current].top();
                _stack[current].pop();
                result[ind].emplace_back(node->val);
                if(node->left){
                    _stack[next].push(node->left);
                }
                if(node->right){
                    _stack[next].push(node->right);
                }
            }else if(current == 1){
                TreeNode* node = _stack[current].top();
                _stack[current].pop();
                result[ind].emplace_back(node->val);
                if(node->right){
                    _stack[next].push(node->right);
                }
                if(node->left){
                    _stack[next].push(node->left);
                }
            }
            if(_stack[current].empty()){ //表明当前层已经打印完
                result.push_back(vector<int>());
                ++ind;
                current = 1- current;
                next = 1-next;
            }
            
        }
        result.pop_back();
        return result;
    }
};
```

执行用时：4 ms, 在所有 C++ 提交中击败了89.75%的用户

内存消耗：12.6 MB, 在所有 C++ 提交中击败了56.84%的用户

## 题解

