# 剑指Offer.64.求1+2+…+n

##### 难度：中等

##### 关键词：发散思维

##### 链接：https://leetcode-cn.com/problems/qiu-12n-lcof/

## 题目描述

求 `1+2+...+n` ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

**示例 1：**

```
输入: n = 3
输出: 6
```

**示例 2：**

```
输入: n = 9
输出: 45
```

 **限制：**

- `1 <= n <= 10000`

## 题目解析

### 思路1: 利用构造函数和类静态成员

循环的本质是重复执行一段代码多次，可以通过多次调用构造函数实现这种特性。

### 思路2: 虚函数

### 思路3: 函数指针

## 代码实现

### 实现1

```c++
class Temp{
public:
     
    Temp(){
        ++cur;
        sum += cur;
        
    }
    static void reset(){
        sum = 0;
        cur = 0;
    }

    static int getsum(){
        return sum;
    }
private:
    static  int  sum ;
    static int  cur ;
};
int Temp::sum ;
int Temp::cur ;
class Solution {
public:

    int sumNums(int n) {
        Temp::reset();
        Temp *s = new Temp[n];
        return Temp::getsum();
    }


};
```

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户

内存消耗：5.9 MB, 在所有 C++ 提交中击败了90.45%的用户

```c++
class Temp{
public:
     
    Temp(){
        ++cur;
        sum += cur;
        
    }
    static void reset(){
        sum = 0;
        cur = 0;
    }

    static int getsum(){
        return sum;
    }
private:
    static  int  sum ;
    static int  cur ;
};
   int Temp::sum ;
   int Temp::cur ;
class Solution {
public:

    int sumNums(int n) {
        Temp::reset();
        Temp *s = new Temp[n];
        delete[] s;
        s = nullptr;
        return Temp::getsum();
    }


};
```

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户

内存消耗：6.2 MB, 在所有 C++ 提交中击败了60.27%的用户

## 题解

## 小结

#### 构造函数

- 类的构造函数有什么作用？

#### 虚函数

- 虚函数的定义？
- 虚函数的作用？
- 虚函数的特点是？
- 为什么要设计「虚函数」？

#### 函数指针

- 函数指针是什么时候出现的？解决了什么痛点？

#### 模版类型

