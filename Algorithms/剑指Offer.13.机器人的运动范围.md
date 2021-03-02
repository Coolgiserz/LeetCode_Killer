# 剑指Offer.13.机器人的运动范围

##### 难度：中等

##### 关键词：回溯

##### 链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/

## 题目描述

地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：

```
输入：m = 2, n = 3, k = 1
输出：3
```

示例 2：

```
输入：m = 3, n = 1, k = 0
输出：1
```

提示：

- 1 <= n,m <= 100
- 0 <= k <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

### 思路：回溯算法

需要注意，一次只能移动一步

### 测试用例

```
1
2
1
3
1
0
4
6
6
12
31
42
12
8
4
10
8
4
11
8
4
20
10
4
40
20
4
40
45
6
```



## 代码实现

```c++
class Solution {
public:
    int movingCount(int m, int n, int k) {
        vector<bool> visited(m*n, false);
        int count = movingCountCore(m, n, 0, 0, k, visited);
        return count;
    }

    //检查(i,j)是否访问过，如果没访问过，检查是否满足条件，并标记其为访问过，检查其周围元素是否满足条件。
    int movingCountCore(int m, int n, int i, int j, int k,  vector<bool>& visited){
        int result = 0;
        if(check(m,n,i,j, k, visited)){
            visited[i*n+j]=true;
            result = 1+movingCountCore(m,n,i-1,j, k,visited)
            +movingCountCore(m,n,i+1,j,k,visited)
            +movingCountCore(m,n,i,j-1,k,visited)
            +movingCountCore(m,n,i,j+1,k,visited);
        }
        return result;
    }
    //判断是否属于运动范围
    bool check(int m, int n, int i, int j, int k, vector<bool>& visited){
         if( i>=0 && j>=0 && i<m && j<n && getNum(i)+getNum(j)<=k && !visited[i*n+j]){
            return true;
        }
        return false; 
    }

    int getNum(int n){
        int res = 0;
        while(n>0){
            res += n % 10;
            n = n /10;
        }
        return res;
    }
    
};
```

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户

内存消耗：6.3 MB, 在所有 C++ 提交中击败了89.28%的用户



```c++
class Solution {
public:

    //寻找(m,n)中满足m、n数位之和小于等于k的个数,m、n是正整数

    //暴力解法：二重循环遍历m、n,
    int movingCount(int m, int n, int k) {
        // int result = 0;
        vector<bool> visited(m*n, false);
        int count = movingCountCore(m, n, 0, 0, k, visited);
        return count;
    }

    //检查(i,j)是否访问过，如果没访问过，检查是否满足条件，并标记其为访问过，检查其周围元素是否满足条件。
    int movingCountCore(int m, int n, int i, int j, int k,  vector<bool>& visited){
        int result = 0;
        if(check(m,n,i,j, k, visited)){
            visited[i*n+j]=true;
            result = 1+movingCountCore(m,n,i-1,j, k,visited)
            +movingCountCore(m,n,i+1,j,k,visited)
            +movingCountCore(m,n,i,j-1,k,visited)
            +movingCountCore(m,n,i,j+1,k,visited);
        }
        return result;
    }
    //判断是否属于运动范围
    bool check(int m, int n, int i, int j, int k, vector<bool>& visited){
        if( i<0 || j<0 || i>=m || j>=n || getNum(i)+getNum(j)>k || visited[i*n+j]){
            return false;
        }
        return true; 
    }

    int getNum(int n){
        int res = 0;
        while(n>0){
            res += n % 10;
            n = n /10;
        }
        return res;
    }
    
};
```

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户

内存消耗：6.4 MB, 在所有 C++ 提交中击败了81.52%的用户

## 题解

