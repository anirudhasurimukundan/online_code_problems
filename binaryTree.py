import numpy as np

class BinaryTree:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

    def contains(self, target):
        if self.label == target:
            return True

        containedInLeft = False if self.left == None else self.left.contains(target)
        containedInRight = False if self.right == None else self.right.contains(target)
        return (containedInLeft or containedInRight)
    
    def insert(self, label, location="left"):
    #def insert(self, label):
        left = np.random.rand() < 0.5
        print(label)
        #if location == "left":
        if left:
            if self.left is None:
                self.left = BinaryTree(label)
            else:
                #self.left = self.left.insert(location, label)
                self.left = self.left.insert(label)
        else:
            if self.right is None:
                self.right = BinaryTree(label)
            else:
                #self.right = self.right.insert(location, label)
                self.right = self.right.insert(label)


if __name__ == "__main__":
    tree = BinaryTree("Asuri")
    tree.left = BinaryTree("Appa")
    tree.right = BinaryTree("Amma")
    tree.left.left = BinaryTree("Anirudh")
    tree.left.right = BinaryTree("Bharath")
    #tree.insert("Appa")
    #tree.insert("Amma")
    #tree.insert("Anirudh")
    #tree.insert("Aishwarya")
    #tree.insert("Kutti Pattoos")
    #tree.insert("Bharath")
    
    lookup = "Anirudh"
    print(tree.contains(lookup))
    #print(tree.left, tree.right)
