class Node:
    def __init__(self,val,left=None,right=None):
        self.data = val
        self.left = None
        self.right = None

def recHeight(root,h=0):
    
    # if root.left is None and root.right is None:
    #     return 1
    # if root.left is not None and root.right is not None:
    #     return 1 + max(recHeight(root.right),recHeight(root.left))
    # if root.left is None:
    #     return 1 + recHeight(root.right)
    # elif root.right is None:
    #     return 1 + recHeight(root.left)
    
    return h if root is None else max(recHeight(root.left,h+1),recHeight(root.right,h+1)) 

p=Node(5)
p.left=Node(3)
p.left.left=Node(2)
p.left.right=Node(4)
p.right=Node(20)
p.right.left=Node(13)
p.right.right=Node(27)
p.right.right.right=Node(30)
p.right.right.right.right=Node(33)

print(recHeight(p))
    

