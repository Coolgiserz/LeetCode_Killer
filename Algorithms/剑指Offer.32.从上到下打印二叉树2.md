# 剑指Offer.32.从上到下打印二叉树2

##### 难度：简单

##### 关键词：树、广度优先搜索

##### 链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof

## 题目描述

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
给定二叉树: `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

返回其层次遍历结果：

```
[
  [3],
  [9,20],
  [15,7]
]
```

提示：

节点总数 <= 1000
注意：本题与主站 102 题相同：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

与[「剑指Offer.32.从上到下打印二叉树1」](./剑指Offer.32.从上到下打印二叉树1.md)相比，差别仅在于该题要求将节点层次分明地打印（知道哪些节点在哪一层）。

所以只需要考虑如何添加一些变量，让我们能够分辨哪些节点属于哪一层即可。

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
        deque<TreeNode*> _queue;
        _queue.push_back(root);
        int ind = 0;
        while(!_queue.empty()){
            int size = _queue.size();
            result.push_back(vector<int>());
            while(size){
                TreeNode* node = _queue.front();
                _queue.pop_front();
                if(node->left){
                    _queue.push_back(node->left);
                }
                if(node->right){
                    _queue.push_back(node->right);
                }
                result[ind].push_back(node->val);
                --size;
            }
            ++ind;
        }
        return result;

    }
};
```

4 ms, 在所有 C++ 提交中击败了88.98%的用户

内存消耗：12.7 MB, 在所有 C++ 提交中击败了28.60%的用户

## 题解

