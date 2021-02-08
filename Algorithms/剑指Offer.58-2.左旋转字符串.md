# 剑指Offer.58-2.左旋转字符串

##### 难度：简单

##### 关键词：字符串

##### 链接：https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/

## 题目描述

字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

**示例 1：**

```
输入: s = "abcdefg", k = 2
输出: "cdefgab"
```

**示例 2：**

```
输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
```

**限制：**

- `1 <= k < s.length <= 10000`

## 题目解析

本题可以利用[翻转单词顺序](剑指Offer.58-1.翻转单词顺序.md)的经验，只不过这里的“单词”只有两个，且不是用空格隔开的：1～k处的字符组成的单词，k+1到结尾组成的单词。

## 代码实现

```c++
class Solution {
public:
    string reverseLeftWords(string s, int n) {
        if(n<1 || s.length()<2 || s.length()<n){
            return s;
        }
        reverseString(s, 0, n-1);
        reverseString(s, n, s.length()-1);
        reverseString(s,0,s.length()-1);
        return s;
    }
    void reverseString(string& s, int start, int end){
        while(start<end){
            char tmp = s[start];
            s[start] = s[end];
            s[end] = tmp;
            ++start;
            --end;
        }
        return;
    }
};
```

执行用时：4 ms, 在所有 C++ 提交中击败了83.70%的用户

内存消耗：7.1 MB, 在所有 C++ 提交中击败了93.75%的用户

## 题解

