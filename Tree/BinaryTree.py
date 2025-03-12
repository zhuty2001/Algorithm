class TreeNode:
    def __init__(self,val = 0):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        """插入节点（按二叉搜索树BST的规则）"""
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        """递归插入"""
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)

    def preorder_traversal(self,node):
        if node:
            print(node.val, " ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def inorder_traversal(self,node):
        if node:
            self.inorder_traversal(node.left)
            print(node.val, " ")
            self.inorder_traversal(node.right)

    def postorder_traversal(self,node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.val, " ")

if __name__ == "__main__":
    tree = BinaryTree()
    values = [10, 5, 15, 3, 7, 13, 18]  # 插入节点的值
    for v in values:
        tree.insert(v)

    print("前序遍历:")
    tree.preorder_traversal(tree.root)  # 10 5 3 7 15 13 18
    print("\n中序遍历:")
    tree.inorder_traversal(tree.root)   # 3 5 7 10 13 15 18
    print("\n后序遍历:")
    tree.postorder_traversal(tree.root) # 3 7 5 13 18 15 10
