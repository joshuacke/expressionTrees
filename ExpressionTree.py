import operator
currentTree = object

class Stack():

  def __init__(self):
    self.items = []
  def isEmpty(self):
    return self.items == []
  def push(self, item):
    self.items.append(item)
  def pop(self):
    return self.items.pop()
  def peek(self):
    return self.items[-1]
  def size(self):
    return len(self.items)

def main():

  file = open("treedata.txt", "r")
  for line in file:
    line = line.strip()
    print("Infix expression:  " + line + "\n")
    print("   Value:   " + str(BinaryTree("").createTree(line).evaluate()))
    print("   Prefix expression:   ", end = "")
    BinaryTree("").createTree(line).preOrder(BinaryTree("").createTree(line))
    print("")
    print("   Postfix expression:   ", end = "")
    BinaryTree("").createTree(line).postOrder(BinaryTree("").createTree(line))
    print("\n")

class BinaryTree:

  def __init__(self, rootObj):
    self.key = rootObj
    self.leftChild = None
    self.rightChild = None
  def createTree(self, expression):
    list_expressions = expression.split(" ")
    s = Stack()
    tree = BinaryTree("")
    s.push(tree)
    current = tree
    for i in list_expressions:
      if (i == "("):
        current.insertLeft("")
        s.push(current)
        current = current.getLeftChild()
      elif (i not in ["*", ")", "+", "-", "/"]):
        if (i.find(".") == -1):
          current.setRootVal(int(i))
        else:
          current.setRootVal(float(i))
        current = s.pop()
      elif (i in ["+", "-", "*", "/"]):
        current.setRootVal(i)
        current.insertRight("")
        s.push(current)
        current = current.getRightChild()
      elif (i == ")"):
        current = s.pop()
      else:
        raise ValueError
    return tree
  def evaluate(self):
    if (self.getLeftChild() and self.getRightChild()):
      return eval(str(self.getLeftChild().evaluate()) + self.getRootVal() + str(self.getRightChild().evaluate()))
    else:
      return self.getRootVal()
  def preOrder(self, tree):
    if (tree == None):
      return
    print(tree.getRootVal(), end = " ")
    self.preOrder(tree.getLeftChild())
    self.preOrder(tree.getRightChild())
  def postOrder(self, tree):
    if (tree == None):
      return
    self.postOrder(tree.getLeftChild())
    self.postOrder(tree.getRightChild())
    print(tree.getRootVal(), end = " ")
  def insertLeft(self, t):
    if (self.leftChild == None):
      self.leftChild = BinaryTree(t)
    else:
      BinaryTree(t).leftChild = self.leftChild
      self.leftChild = BinaryTree(t)
  def insertRight(self, t):
    if (self.rightChild == None):
      self.rightChild = BinaryTree(t)
    else:
      BinaryTree(t).rightChild = self.rightChild
      self.rightChild = BinaryTree(t)
  def getRightChild(self):
    return self.rightChild
  def getLeftChild(self):
    return self.leftChild
  def setRootVal(self, obj):
    self.key = obj
  def getRootVal(self):
    return self.key
    
main()
