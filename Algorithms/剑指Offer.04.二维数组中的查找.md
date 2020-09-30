

# 剑指Offer.04.二维数组中的查找

##### 难度：简单

##### 关键词：数组、双指针

##### 链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/

## 题目描述

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：

```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```

给定 target = `5`，返回 `true`。

给定 target = `20`，返回 `false`。

**限制：**

```
0 <= n <= 1000
0 <= m <= 1000
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

利用二维数组已经排好序的特性，从右上角（或左下角）开始查找，如果找到了则返回true，没找到则往左或者往下找。由于此时target要么大于右上角元素要么小于，每一种情况都能保证后面可能的方向只有一个：向左或向下之中的一个。

所以这种思路最坏的情形时间复杂度为O(m+n)，往左遍历到尽头后往下到尽头。

【注：如果从左上角或者右下角开始则没有这种好处，因为不能保证后面可能的方向唯一】

## 代码实现

```c++
class Solution {
public:
    //测试用例
    // 1）空矩阵 2）非空矩阵，能找到的target 3）非空矩阵，不能找到的target
    bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
        int n = matrix.size();
        if(n == 0){
            return false;
        }
        int m = matrix[0].size();
        if(m == 0){
            return false;
        }
        //确保m和n都大于或等于1了
        int i = 0;
        while(m >= 1 && i < n && matrix[i][m-1]!=target){
            //还没有找到target时
            if(matrix[i][m-1]>target){//排除第m列
                m--;
            }else{
                i++;
            }
        }
        if(m<=0 || i>=n){
            return false;
        }
        if(matrix[i][m-1]==target){
                return true;
        }
        return false;  
    }
};
```

执行用时：52 ms, 在所有 C++ 提交中击败了93.78%的用户

内存消耗：12.7 MB, 在所有 C++ 提交中击败了90.14%的用户

## 题解

