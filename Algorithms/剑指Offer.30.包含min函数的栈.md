# 剑指Offer.30.包含min函数的栈

##### 难度：简单

##### 关键词：栈、设计

##### 链接：https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/

## 题目描述

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

示例:

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
```

**提示：**

1. 各函数的调用总次数不超过 20000 次

注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

要实现的是栈结构，所以要求后进先出，关键问题在于如何实现O(1)时间复杂度的min函数。

自然而然会想到空间换时间，但用什么样的“空间”换取快速的min函数操作呢？

用一个变量存储最小值如何？第一次调用的时候是O(1)复杂度，但弹出了最小值之后再调用就不是O(1)了（需要重新遍历一遍以获取次最小值），所以还是考虑用一个辅助容器保存最小值，保证每次对数据栈进行push、pop操作之后辅助容器也能够以O(1)时间复杂度返回栈的最小值。

具体的设计思路可以是:

添加一个辅助栈，使其栈顶元素始终为最小值，同时辅助栈的大小与数据栈大小相等。

进行push操作时，除了将元素推入数据栈中，还将最小值推入辅助栈中（如果新推入的值是最小值自然没问题，如果新推入的值不是最小值，则将数据栈中现有的最小值重新推入辅助栈中）

进行pop操作时，同时弹出数据栈和辅助栈的栈顶元素

进行min操作时，返回辅助栈的栈顶元素（最小值）。

## 代码实现

### 实现1

```c++
class MinStack {
public:
    /** initialize your data structure here. */
    vector<int> _container; //保存元素
    vector<int> _index; //用于保存最小值的索引
    int size_of_con = 0;
    int min_ind = 0;
    MinStack() {
        
    }
    /*
        推入元素时，检查该元素是否比最小值小，若小则将索引推入索引栈，
    */
    void push(int x) {
        if(_index.size()>0){
            min_ind = _index.back();
        }else{
            min_ind = 0;
        }
        _container.push_back(x);
        ++size_of_con;
        if(x <= _container[min_ind]) {//找到更小的
             min_ind = size_of_con-1;
            _index.emplace_back(min_ind);
            
        }else{
            _index.emplace_back(min_ind);
        }
    }
    
    void pop() {
        if(_container.size()>0){
            _container.pop_back();
            _index.pop_back();
            --size_of_con;
        }
        
    }
    
    int top() {
        return _container.back();
    }
    
    int min() {

        int tmp = _index.back();
        return _container[tmp];
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->min();
 */
```

执行用时：40 ms, 在所有 C++ 提交中击败了73.90%的用户

内存消耗：15.2 MB, 在所有 C++ 提交中击败了26.06%的用户

### 实现2

```c++
class MinStack {
public:
    /** initialize your data structure here. */
    stack<int> _container; //保存元素
    stack<int> _min; //用于保存最小值的索引

    MinStack() {
        
    }
    /*
        推入元素时，检查该元素是否比最小值小，若小则将索引推入索引栈，
    */
    void push(int x) {
        int min_v;
        if(_min.size()>0){
            min_v = _min.top();
        }else{
            min_v = x;
        }
        _container.push(x);
        if(x <= min_v) {//找到更小的
            _min.push(x);
            
        }else{
            _min.push(min_v);
        }
    }
    
    void pop() {
        if(_container.size()>0){
            _container.pop();
            _min.pop();
        }   
    }
    
    int top() {
        return _container.top();
    }
    
    int min() {
        return _min.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->min();
 */
```

执行用时：44 ms, 在所有 C++ 提交中击败了58.38%的用户

内存消耗：15.3 MB, 在所有 C++ 提交中击败了11.50%的用户

## 题解

