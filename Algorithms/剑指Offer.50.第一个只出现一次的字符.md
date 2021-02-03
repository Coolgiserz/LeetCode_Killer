# 剑指Offer.50.第一个只出现一次的字符

##### 难度：简单

##### 关键词：哈希表

##### 链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/

## 题目描述

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

```
s = "abaccdeff"
返回 "b"

s = "" 
返回 " "
```


限制：

```
0 <= s 的长度 <= 50000
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

引入一个哈希表记录字符出现的次数。

## 代码实现

```c++
class Solution {
public:
    char firstUniqChar(string s) {
        //哈希表记录次数
        int hashtable[256] = {0};
        for(char& ch: s){
            ++hashtable[ch-' '];
        }

        for(char& ch: s){
            if(hashtable[ch-' ']==1){
                return ch; 
            }
        }
        return ' ';
    }
};
```

执行用时：16 ms, 在所有 C++ 提交中击败了98.88%的用户

内存消耗：10.3 MB, 在所有 C++ 提交中击败了97.32%的用户

## 题解

