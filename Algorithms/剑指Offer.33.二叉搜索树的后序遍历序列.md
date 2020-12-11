# 剑指Offer.33.二叉搜索树的后序遍历序列

##### 难度：中等

##### 关键词：树

##### 链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/

## 题目描述

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

         5
        / \
       2   6
      / \
     1   3

示例 1：

```
输入: [1,6,3,2,5]
输出: false
```

示例 2：

```
输入: [1,3,2,6,5]
输出: true
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

确定根节点

确定序列中左子树的节点及右子树的节点

分而治之

## 代码实现

```c++
class Solution {
public:
    bool verifyPostorder(vector<int>& postorder) {
        if(postorder.size()==0){//特殊输入
            return true;
        }
        return helpVerify(postorder, 0, postorder.size()-1);
    }

    bool helpVerify(vector<int>& postorder, int si, int sj){
        if(si >= sj){
            return true;
        }
        int root = postorder[sj]; //根节点

        //找到左子树; [0, i-1]
        int i = si;
        for(;i<sj;++i){
            if(postorder[i]>root){
                break;
            }
        }
        int j=i;
        for(;j<sj;++j){
            if(postorder[j]<root){
                return false;
            }
        } 
        if(i>0 && !helpVerify(postorder, si, i-1)){
             return false;
        }
        if(i<sj &&!helpVerify(postorder, i, sj-1)){
            return false;

        }
        return true;
    }
};
```

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户

内存消耗：7.3 MB, 在所有 C++ 提交中击败了31.29%的用户

## 小结

处理二叉树的遍历序列时，考虑先找到根节点，再确定遍历序列的哪部分属于左子树，哪部分属于右子树，然后就可以进行递归操作了。

