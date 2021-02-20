# 剑指Offer.68-1.二叉搜索树的最近公共祖先

##### 难度：简单

##### 关键词：树

##### 链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/

## 题目描述

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/binarysearchtree_improved.png)

 示例 1:

```
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。
```

示例 2:

```
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
```



说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。
注意：本题与主站 235 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

### 思路1：递归解法

###思路2: 循环

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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        //从根节点往下找，找到的第一个位于p和q之间的节点即为最近公共祖先
        if((root->val > p->val) && (root->val > q->val)){
            return lowestCommonAncestor(root->left, p, q);
        }else if((root->val < p->val) && (root->val < q->val)){
            return lowestCommonAncestor(root->right, p, q);
        }else{
            return root;
        }
    }
};
```

执行用时：36 ms, 在所有 C++ 提交中击败了75.76%的用户

内存消耗：22.8 MB, 在所有 C++ 提交中击败了73.11%的用户

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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        //从根节点往下找，找到的第一个位于p和q之间的节点即为最近公共祖先
        TreeNode* res = root;
        while(true){
            if((res->val > p->val) && (res->val > q->val)){
                 res = res->left;
            }else if((res->val < p->val) && (res->val < q->val)){
                 res = res->right;
            }else{
                break;
            }
        }
        

        return res;
        
    }
};
```

执行用时：36 ms, 在所有 C++ 提交中击败了75.76%的用户

内存消耗：22.8 MB, 在所有 C++ 提交中击败了66.36%的用户

## 题解

