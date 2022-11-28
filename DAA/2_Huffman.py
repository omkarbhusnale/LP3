# PR -2 Huffman

from collections import Counter
# BCAADDDCCACACAC
# string = ""
string = input("Enter String: ")


freq=Counter(string)
nodes=sorted(freq.items(),key=lambda x:x[1],reverse=True)
class NodeTree:
    def __init__(self,left=None,right=None):
        self.left=left
        self.right=right
while len(nodes)>1:
    (key1,c1)=nodes[-1]
    (key2,c2)=nodes[-2]
    nodes=nodes[:-2]
    node=NodeTree(key1,key2)
    nodes.append((node,c1+c2))
    nodes=sorted(nodes,key=lambda x:x[1],reverse=True)

def haftree(nodes,left=True,binstring=''):
    if type(nodes) is str:
        return {nodes:binstring}
    l,r=nodes.left,nodes.right
    b=dict()
    b.update(haftree(l,True,binstring+"0"))
    b.update(haftree(r,False,binstring+"1"))
    return b

p=haftree(nodes[0][0])
print(p)
