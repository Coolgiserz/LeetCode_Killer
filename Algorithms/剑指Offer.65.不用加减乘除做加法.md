# 剑指Offer.65.不用加减乘除做加法

##### 难度：简单

##### 关键词：位运算

##### 链接：https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/

## 题目描述

写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

**示例:**

```
输入: a = 1, b = 1
输出: 2
```

 **提示：**

- `a`, `b` 均可能是负数或 0
- 结果不会溢出 32 位整数

## 题目解析

利用位运算.

## 代码实现

### 实现1

```c++
class Solution {
public:

    int add(int a, int b) {
        int sum = 0, carry = 0;
        do{
           sum = a^b;
            carry = (a & b & 0xffffffff) << 1;
            a = sum;
            b = carry;
        }while(b!=0);
        return a;
    }
};
```

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户

内存消耗：5.9 MB, 在所有 C++ 提交中击败了74.85%的用户

```c++
class Solution {
public:

    int add(int a, int b) {
        int sum = 0, carry = 0;
        do{
           sum = a^b;
            carry = (unsigned int)(a & b) << 1;
            a = sum;
            b = carry;
        }while(b!=0);
        return a;
    }
};
```

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户

内存消耗：5.9 MB, 在所有 C++ 提交中击败了70.12%的用户

#### 实现1-origin

```c++
class Solution {
public:

    int add(int a, int b) {
        int sum = 0, carry = 0;
        do{
           sum = a^b;
            carry = (a & b) << 1;
            a = sum;
            b = carry;
        }while(b!=0);
        return a;
    }
};
```



## 题解

