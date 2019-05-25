"""code from Pearson Education, Inc p104 """

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree
    def search(self, e):
        current = self.root # Start from the root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current.element
                return True # Element is found

        return False

    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully
    def insert(self, e):
        if self.root == None:
          self.root = self.createNewNode(e) # Create a new root
        else:
          # Locate the parent node
          parent = None
          current = self.root
          while current != None:
            if e < current.element:
              parent = current
              current = current.left
            elif e > current.element:
              parent = current
              current = current.right
            else:
              return False # Duplicate node not inserted

          # Create the new node and attach it to the parent node
          if e < parent.element:
            parent.left = self.createNewNode(e)
          else:
            parent.right = self.createNewNode(e)

        self.size += 1 # Increase tree size
        return True # Element inserted

    # Create a new TreeNode for element e
    def createNewNode(self, e):
      return TreeNode(e)
    """
    # Return the size of the tree
    def getSize(self):
      return self.size"""

    # Inorder traversal from the root
    def inorder(self):
      self.inorderHelper(self.root)

    # Inorder traversal from a subtree
    def inorderHelper(self, r):
      if r != None:
        self.inorderHelper(r.left)
        print(r.element, end = " ")
        self.inorderHelper(r.right)

    # Postorder traversal from the root
    def postorder(self):
      self.postorderHelper(self.root)

    # Postorder traversal from a subtree
    def postorderHelper(self, root):
      if root != None:
        self.postorderHelper(root.left)
        self.postorderHelper(root.right)
        print(root.element, end = " ")

    # Preorder traversal from the root
    def preorder(self):
      self.preorderHelper(self.root)

    # Preorder traversal from a subtree
    def preorderHelper(self, root):
      if root != None:
        print(root.element, end = " ")
        self.preorderHelper(root.left)
        self.preorderHelper(root.right)


    # Return true if the tree is empty
    def isEmpty(self):
      return self.size == 0

    # Remove all elements from the tree
    def clear(self):
      self.root == None
      self.size == 0

    # Return the root of the tree
    def getRoot(self):
      return self.root


    def PrintLeafLeftToRight(self):
        root = BinaryTree.getRoot(self)
        s1 = []
        # Stack to store all the
        # leaf nodes
        s2 = []

    # Push the root node
        s1.append(root)

        while len(s1) != 0:
            curr = s1.pop()

        # If current node has a left child
        # push it onto the first stack
            if curr.left:
                s1.append(curr.left)

        # If current node has a right child
        # push it onto the first stack
            if curr.right:
                s1.append(curr.right)

        # If current node is a leaf node
        # push it onto the second stack
            elif not curr.left and not curr.right:
                s2.append(curr)

    # Print all the leaf nodes

        while len(s2) != 0:
            print(s2.pop().element, end = " ")












class TreeNode:
    def __init__(self, e):
      self.element = e
      self.left = None # Point to the left node, default None
      self.right = None # Point to the right node, default None


# Python code t get difference of two lists
# Not using set()
def Diff(li1, li2):
    return (list(set(li1) - set(li2)))

# Driver Code
    ####################### Main test binary tree

def main(size = 7):
    tree = BinaryTree()
    tree.insert("George")
    tree.insert("Michael")
    tree.insert("Tom")
    tree.insert("Adam")
    tree.insert("Jones")
    tree.insert("Peter")
    tree.insert("Daniel")

    # Traverse tree
    print("Inorder (sorted): ", end = "")
    tree.inorder()
    print("\nPostorder: ", end = "")
    tree.postorder()
    print("\nPreorder: ", end = "")
    tree.preorder()

    numbers = input("Enter family members separated by comma ")
    li1  = numbers.split(",")

    print ("\n\nInserting the following values:")
    for i in numbers:
        print(i, end=" ")
    print()
    intTree = BinaryTree()

    for e in numbers:
      intTree.insert(e)
    print("\nPreorder traversal:")
    intTree.preorder()
    print("\n\nInorder traversal:")
    intTree.inorder()
    print("\n\nPostorder traversal:")
    intTree.postorder()
    print("\n\nLeaf Nodes Only:")
    intTree.PrintLeafLeftToRight()
    print("\n\nNonLeafNodes:")




    #print("\n\nNon-Leaf Nodes:")
    #intTree.findFullNode()

if __name__ == "__main__":
    main()
