# Kruskal
edges = [("A", "B", 4), ("A", "C", 6),
         ("A", "D", 16), ("B", "E", 24),
         ("C", "E", 23), ("C", "F", 5),
         ("C", "D", 8), ("D", "F", 10),
         ("D", "H", 21),("E", "F", 18),
         ("E","G",9),("F","G",11),
         ("G","H",7)]
vertices=list('ABCDEFGH')
# 升序排列
edges.sort(key=lambda x:x[2])
print(edges)
# 字典
trees=dict()
for i in vertices:
    trees[i]=i
#寻找根节点
def find_node(x):
    if trees[x]!=x:
        trees[x]=find_node(trees[x])
    return trees[x]
#定义最小生成树
mst=[]
#定义循环次数，n为需要添加的边数=顶点数-1
n=len(vertices)-1
#循环
for edge in edges:
    v1,v2,_=edge
    if find_node(v1)!=find_node(v2):
        trees[find_node(v2)]=find_node(v1)
        print(edge,trees)
        mst.append(edge)
        n-=1
        if n==0:
            break
print(mst)
