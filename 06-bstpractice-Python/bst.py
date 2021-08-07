class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        num = new_val
        newnode = Node(num)
        if self.root == None:
            self.root = newnode
        else:
            current = self.root
            parent = self.root
            while(current != None):
                parent = current
                if num < current.value:
                    current = current.left
                else:
                    current = current.right
                    
            if num < parent.value:
                parent.left = newnode
            else:
                parent.right = newnode
        pass

    def printSelf(self):
        # Your code goes here
        print(self.root)
        pass
        
    def search(self, find_val):
        # Your code goes here
        num = find_val
        while(self.root != None):
            
            if self.root.value == num:
                return True
            if self.root.value < num:
                self.root = self.root.right
                
            elif self.root.value > num:
                self.root = self.root.right
                
            return False
        pass

