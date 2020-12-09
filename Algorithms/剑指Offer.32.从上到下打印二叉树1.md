# 剑指Offer.32.从上到下打印二叉树1

##### 难度：中等

##### 关键词：树、广度优先搜索

##### 链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/

## 题目描述

从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    		3
       / \
      9  20
        /  \
       15   7
    
 返回：

[3,9,20,15,7]


提示：

- 节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

实际上是广度优先遍历。

可思考：

1. 需要什么样的容器辅助遍历？

   栈还是队列？

2. 如何将下一层的元素添加到容器中？

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
    vector<int> levelOrder(TreeNode* root) {
        if(!root){
            return vector<int>();
        }
        deque<TreeNode*> _queue;
        vector<int> result;
        _queue.push_back(root);
        while(!_queue.empty()){
            TreeNode* node = _queue.front();
            _queue.pop_front();
            result.emplace_back(node->val);
            if(node->left){
                _queue.push_back(node->left);
            }
            if(node->right){
                _queue.push_back(node->right);
            }
            
        }
        return result;
    }
};
```

执行用时：4 ms, 在所有 C++ 提交中击败了88.02%的用户

内存消耗：12.3 MB, 在所有 C++ 提交中击败了18.98%的用户

时间复杂度空间复杂度均为O(N)

## 题解

