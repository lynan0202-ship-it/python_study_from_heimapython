# 迭代版阶乘
def factorial_iter(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial_iter(5))  # 输出：120
'''
 **递归**：代码简洁，适合“问题能拆分成更小同类问题”的场景（如阶乘、斐波那契、二叉树遍历），但调用次数多了会慢甚至报错。  
- **迭代（循环）**：效率高，适合解决递归能做的问题，比如用循环算阶乘：  
  ```python
'''