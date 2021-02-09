# 剑指Offer.59-2.队列的最大值

##### 难度：中等

##### 关键词：栈、滑动窗口

##### 链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/

## 题目描述

请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

```
输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
```

**示例 2：**

```
输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
```

 **限制：**

- `1 <= push_back,pop_front,max_value的总操作数 <= 10000`
- `1 <= value <= 10^5`

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

### 思路1: 使用辅助队列

要点：

1. 保证辅助队列的头元素为队列最大值，这样当需要访问最大值时可以O(1)时间复杂度获得
2. 弹出队列元素时检查该元素是否为队列最大值
3. 插入新元素时判断新元素与辅助队列末端元素大小

### 测试用例

```
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
["MaxQueue","push_back","push_back","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[10],[2],[],[],[]]
["MaxQueue","push_back","push_back","push_back","push_back","max_value","pop_front","pop_front","max_value","pop_front","max_value"]
[[],[1],[2],[10],[2],[],[],[],[],[],[]]
["MaxQueue","pop_front","pop_front","pop_front","pop_front","pop_front","push_back","max_value","push_back","max_value"]
[[],[],[],[],[],[],[15],[],[9],[]]
["MaxQueue","max_value","pop_front","max_value","push_back","max_value","pop_front","max_value","pop_front","push_back","pop_front","pop_front","pop_front","push_back","pop_front","max_value","pop_front","max_value","push_back","push_back","max_value","push_back","max_value","max_value","max_value","push_back","pop_front","max_value","push_back","max_value","max_value","max_value","pop_front","push_back","push_back","push_back","push_back","pop_front","pop_front","max_value","pop_front","pop_front","max_value","push_back","push_back","pop_front","push_back","push_back","push_back","push_back","pop_front","max_value","push_back","max_value","max_value","pop_front","max_value","max_value","max_value","push_back","pop_front","push_back","pop_front","max_value","max_value","max_value","push_back","pop_front","push_back","push_back","push_back","pop_front","max_value","pop_front","max_value","max_value","max_value","pop_front","push_back","pop_front","push_back","push_back","pop_front","push_back","pop_front","push_back","pop_front","pop_front","push_back","pop_front","pop_front","pop_front","push_back","push_back","max_value","push_back","pop_front","push_back","push_back","pop_front"]
[[],[],[],[],[46],[],[],[],[],[868],[],[],[],[525],[],[],[],[],[123],[646],[],[229],[],[],[],[871],[],[],[285],[],[],[],[],[45],[140],[837],[545],[],[],[],[],[],[],[561],[237],[],[633],[98],[806],[717],[],[],[186],[],[],[],[],[],[],[268],[],[29],[],[],[],[],[866],[],[239],[3],[850],[],[],[],[],[],[],[],[310],[],[674],[770],[],[525],[],[425],[],[],[720],[],[],[],[373],[411],[],[831],[],[765],[701],[]]
```

## 代码实现

### 实现1

```c++
class MaxQueue {
public:
    deque<int> _index; //用一个栈保存最大值
    deque<int> _data; //保存队列里的数据
    MaxQueue() {

    }
    
    int max_value() {
        if(_data.empty()){
            return -1;
        }
        return _index.front();
    }
    //保证_index的front元素一定是队列的最大值
    void push_back(int value) {
        _data.push_back(value);
        //后进元素value若大于当前队列最大值，则_index清空
        while(!_index.empty() && _index.back()<=value){
            _index.pop_back();
        }
        _index.push_back(value);
    }
    
    int pop_front() {
        if(_data.empty()){
            return -1;
        }
        int front = _data.front();
        _data.pop_front();
        //判断是否要更改index
        if(front == _index.front()){
            _index.pop_front();
        }
        return front;
    }
};

/**
 * Your MaxQueue object will be instantiated and called as such:
 * MaxQueue* obj = new MaxQueue();
 * int param_1 = obj->max_value();
 * obj->push_back(value);
 * int param_3 = obj->pop_front();
 */
```

执行用时：132 ms, 在所有 C++ 提交中击败了94.34%的用户

内存消耗：47.5 MB, 在所有 C++ 提交中击败了95.07%的用户

## 题解

