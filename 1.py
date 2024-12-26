from typing import List, Any

def push(item: Any, stack: List[Any], top: int, maxSize: int) -> int:
    """
    將元素推入堆疊
    :param item: 新增的元素
    :param stack: 堆疊列表
    :param top: 堆疊頂部的索引
    :param maxSize: 堆疊的最大容量
    :return: 更新後的堆疊頂部索引
    """
    # 檢查堆疊是否已滿
    if top == maxSize - 1:
        print("Stack is full")  # 如果滿了，顯示訊息
    else:
        top += 1               # 指標位置加 1
        stack[top] = item      # 將資料加入堆疊
    return top                 # 返回更新後的 top 值

def isEmpty(top: int) -> bool:
    """
    判斷堆疊是否為空
    :param top: 堆疊頂部的索引
    :return: True 表示堆疊為空，False 表示堆疊非空
    """
    return top == -1

def isFull(top: int, maxSize: int) -> bool:
    """
    判斷堆疊是否為滿
    :param top: 堆疊頂部的索引
    :param maxSize: 堆疊的最大容量
    :return: True 表示堆疊已滿，False 表示堆疊未滿
    """
    return top == maxSize - 1

def topItem(stack: List[Any], top: int) -> Any:
    """
    查看堆疊頂端的項目內容
    :param stack: 堆疊列表
    :param top: 堆疊頂部的索引
    :return: 堆疊頂部的值
    """
    if not isEmpty(top):
        return stack[top]
    else:
        return "Stack is empty"

# 初始化堆疊
maxSize = 5
stack = [None] * maxSize  # 使用列表模擬堆疊
top = -1                  # 堆疊初始為空

# 測試操作
top = push(10, stack, top, maxSize)  # 推入 10
top = push(20, stack, top, maxSize)  # 推入 20
top = push(30, stack, top, maxSize)  # 推入 30

print("IsFull:", isFull(top, maxSize))  # False
print("TopItem:", topItem(stack, top))  # 30

top = push(40, stack, top, maxSize)  # 推入 40
top = push(50, stack, top, maxSize)  # 推入 50
top = push(60, stack, top, maxSize)  # 堆疊已滿，無法推入

print("IsFull:", isFull(top, maxSize))  # True
print("IsEmpty:", isEmpty(top))        # False
print("TopItem:", topItem(stack, top))  # 50
