# 剑指Offer.12.矩阵中的路径

##### 难度：中等

##### 关键词：深度优先搜索

##### 链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/

## 题目描述

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

```
[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]
```

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

## 代码实现

```c++
class Solution {
public:
    //思路：回溯法，选定一个起点，判断是否match，不match则直接返回false，match则递归检查起点周围的格子是否等于word的第二个字符，依次类推。
    bool exist(vector<vector<char>>& board, string word) {
        vector<vector<int>> visited(board.size(), vector<int>(board[0].size()));
        for(int i=0;i<board.size();i++){
            for(int j=0;j<board[0].size();j++){
                if(word[0] == board[i][j]){
                    if(dfs(board, visited, i, j, word, 0)){
                        return true;
                    }
                }
                
            }
        }
        return false;
    }

    bool dfs(vector<vector<char>>& board, vector<vector<int>>& visited, int i, int j, string& word, int length){
        if(length == word.length()){//递归终止条件
            return true;
        }
        if(i<0 || j<0 || i>=board.size() || j>=board[0].size() ){
            return false;
        }
        if(visited[i][j]==0 && board[i][j] == word[length]){
            visited[i][j] = 1;
            if(dfs(board, visited, i+1, j, word, length+1)){
                return true;
            }
            if(dfs(board, visited, i, j+1, word, length+1)){
                return true;
            }
            if(dfs(board, visited, i, j-1, word, length+1)){
                return true;
            }
            if(dfs(board, visited, i-1, j, word, length+1)){
                return true;
            }
            visited[i][j] = 0;
        }
        
        return false;

    }
};
```

执行用时：20 ms, 在所有 C++ 提交中击败了99.24%的用户

内存消耗：8.6 MB, 在所有 C++ 提交中击败了54.14%的用户

## 小结

### 嵌套vector的初始化

```c++
vector<vector<int>> visited(board.size(), vector<int>(board[0].size()));
```



