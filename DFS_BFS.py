# DFS
def DFS(graph, node):    
    # DFS使用栈实现先进后出
    # 需要注意DFS在系统上是有限制的，不是无限制的，比如win只支持3000左右（实验测试知道的）
    stack = []
    stack.append(node)
    Find_Path = set()
    Find_Path.add(node)
    while(len(stack) > 0):
        vertex = stack.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in Find_Path:
                stack.append(node)
                Find_Path.add(node)
        print(vertex,end=" ")
DFS(graph,'A')
# BFS
def BFS(graph, node):
    queue = []#BFS使用栈实现先进先出
    queue.append(node)
    Find_Path = set()
    Find_Path.add(node)
    while(len(queue) > 0):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in Find_Path:
                queue.append(node)
                Find_Path.add(node)
        print(vertex,end=" ")
BFS(graph,'A')
