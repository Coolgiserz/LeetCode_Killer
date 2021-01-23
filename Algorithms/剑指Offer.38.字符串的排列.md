# 剑指Offer.38.字符串的排列

##### 难度：中等

##### 关键词：回溯算法

##### 链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/

## 题目描述

输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

**示例:**

```
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
```

 

## 题目解析

### 测试用例:

每个字符都不同的字符串："abc"

存在重复字符的字符串："aab"

### 思路：回溯

每次选择一个字符，然后将该字符与后面的字符进行交换，递归进行排列

## 代码实现

### 实现1

```c++
class Solution {
public:
    vector<string> permutation(string s) {
        set<string> _result;
        
        permutation(s, 0, s.length(), _result);
        vector<string> result;
        for(set<string>::iterator it=_result.begin();it!=_result.end();++it){
            result.emplace_back(*it);
        }
        return result;

    }

    void permutation(string s, int index, int length, set<string>& result){
        if(index == length-1){
            result.insert(s);
        }
        for(int i=index;i<length;++i){
            swap(s[i], s[index]);
            permutation(s, index+1, length, result);
            swap(s[i], s[index]);
        }
    }
    
};
```

执行用时：140 ms, 在所有 C++ 提交中击败了45.47%的用户

内存消耗：25.1 MB, 在所有 C++ 提交中击败了45.49%的用户

### 实现2

```c++
class Solution {
public:
    vector<string> permutation(string s) {
         vector<string> result;

        permutation(s, 0, s.length(), result);

        return result;

    }

    void permutation(string s, int index, int length, vector<string>& result){

        if(index == length-1){
            result.push_back(s);
        }
        set<char> _set;
        for(int i=index;i<length;++i){
            if(_set.find(s[i])!=_set.end()){//同一层循环中遇到重复字符就跳过，保证result中不会有重复的字符串排列
                continue;
            }else{
                _set.insert(s[i]);
            }
            swap(s[i], s[index]);
            permutation(s, index+1, length, result);
            swap(s[i], s[index]);
        }
    }
    
};
```

执行用时：96 ms, 在所有 C++ 提交中击败了62.83%的用户

内存消耗：32.8 MB, 在所有 C++ 提交中击败了26.96%的用户

## 题解

