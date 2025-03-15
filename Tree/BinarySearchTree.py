class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.value = val

class BST:
    def __init__(self):
        self.root = None

    def insert(self,val):
        if self.root == None:
            self.root = Node(val)
        else:
            currentNode = self.root
            while True:
                if val < currentNode.value:
                    if currentNode.left == None:
                        currentNode.left = Node(val)
                        return
                    else:
                        currentNode = currentNode.left
                elif val > currentNode.value:
                    if currentNode.right == None:
                        currentNode.right = Node(val)
                        return
                    else:
                        currentNode = currentNode.right
    def delete(self, val):
        parent, node = None, self.root
        
        # **Step 1: 查找要删除的节点**
        while node and node.value != val:
            parent = node
            if val < node.value:
                node = node.left
            else:
                node = node.right

        if not node:  # 没找到节点
            return

        # **Step 2: 处理不同的删除情况**
        
        # **情况 1: 叶子节点（无子节点）**
        if not node.left and not node.right:
            if not parent:  # 删除根节点
                self.root = None
            elif parent.left == node:
                parent.left = None
            else:
                parent.right = None

        # **情况 2: 只有一个子节点**
        elif node.left and not node.right:  # 只有左子树
            if not parent:
                self.root = node.left
            elif parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left

        elif node.right and not node.left:  # 只有右子树
            if not parent:
                self.root = node.right
            elif parent.left == node:
                parent.left = node.right
            else:
                parent.right = node.right

        # **情况 3: 有两个子节点**
        else:
            successor_parent = node
            successor = node.right  # 找中序后继（右子树中的最小节点）

            while successor.left:
                successor_parent = successor
                successor = successor.left

            node.value = successor.value  # 用后继节点的值覆盖当前节点

            # 删除后继节点
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
            
B = BST()
B.insert(30)
B.insert(21)
B.insert(23)
B.insert(20)
B.insert(33)
B.insert(32)

B.delete(21)
print(B.root.left.value)