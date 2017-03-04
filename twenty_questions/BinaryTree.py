"""
    >>> n = Node("I am a node", "lr")
    >>> n1 = Node("I am a node", "lr")
    >>> n2 = Node("I am a different node", "lr")
    >>> n.getPath()
    'lr'
    >>> n.getValue()
    'I am a node'
    >>> n==n1
    True
    >>> n==n2
    False
    
   
    >>> tree1 = BinaryTree("I am the root")
    >>> tree1.getValueWithPath("")
    'I am the root'
    
    >>> tree1 = tree1.withNewBranches("", "I am the top left node", "I am the top right node")
    >>> tree1.getLeftValue("")
    'I am the top left node'
    >>> tree1.getRightValue("")
    'I am the top right node'
    >>> tree1.getValueWithPath("l")
    'I am the top left node'
    >>> tree1.getValueWithPath("r")
    'I am the top right node'
    
    >>> tree1.nodeExists("r")
    True
    >>> tree1.nodeExists("rl")
    False
    >>> tree1 = tree1.withNewBranches("r", "I am the bottom left leaf on right", "I am the bottom right leaf on right")
    >>> tree1.nodeExists("rl")
    True
    
    >>> tree1.nodeIsLeaf("r")
    False
    >>> tree1.nodeIsLeaf("rl")
    True
    >>> tree1.nodeIsLeaf("l")
    True
    
    >>> tree2 = BinaryTree("I am the root") 
    >>> tree2 = tree2.withNewBranches("", "I am the top left node", "I am the top right node")
    >>> tree1==tree2
    False
    
    >>> tree2 = tree2.withNewBranches("r", "I am the bottom left leaf on right", "I am the bottom right leaf on right")
    >>> tree1==tree2
    True
    
    >>> print tree1
    tree = BinaryTree("I am the root")
    tree = tree.withNewBranches("", "I am the top left node", "I am the top right node")
    tree = tree.withNewBranches("r", "I am the bottom left leaf on right", "I am the bottom right leaf on right")
    
    >>> tree1 = tree1.replaceValueWith("r", "I am the new value!")
    >>> tree1.getValueWithPath("r")
    'I am the new value!'
       
"""
# make Python look in the right place for logic.py, or complain if it doesn't
from operator import __eq__
from copy import deepcopy
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print "Can't find logic.py; if this happens in the CS teaching lab, tell your instructor"
    print "   If you are using a different computer, add logic.py to your project"
    print "   (You can download logic.py from http://www.cs.haverford.edu/resources/software/logic.py)"
    sys.exit(1)

# Put BinaryTree class here
class BinaryTree:
    #constructor
    def __init__(self, rootValue):
        self.nodes = [Node(rootValue, "")]
    #returns the value of the left child from the given path
    #BinaryTree("root").withNewBranches("","left", "right").getLeftValue("")=="left"
    def getLeftValue(self, path):
        precondition(type(path)==type("") and self.nodeExists(path+"l"))
        return self.getValueWithPath(path+"l")
    #returns the value of the right child from the given path
    #BinaryTree("root").withNewBranches("","left", "right").getRightValue("")=="right"
    def getRightValue(self, path):
        precondition(type(path)==type("") and self.nodeExists(path+"r"))
        return self.getValueWithPath(path+"r")
    #returns the value of the node at the given path
    #BinaryTree("root").getValueWithPath("")=="root"
    #B.withNewBranches("","left", "right").getValueWithPath("r") =="right"
    #B.withNewBranches(P,"left", "right").getValueWithPath(P+"r") =="right"
    #B.withNewBranches(P,"left", "right").getValueWithPath(P)    =="right"
    def getValueWithPath(self, path):
        precondition(type(path)==type("") and self.nodeExists(path))
        for n in self.nodes:
            if n.getPath() == path:
                return n.getValue()            
    #returns whether or not a node exists at the given path
    #BinaryTree("root").nodeExists("")==True
    #BinaryTree("root").nodeExists("r")==False
    #BinaryTree("root").withNewBranches("","left", "right").nodeExists("r")==True
    def nodeExists(self, path):
        precondition(type(path)==type(""))
        for n in self.nodes:
            if n.getPath() == path:
                return True
        return False
    
    #returns whether or not a node is a leaf(aka has no children)
    #BinaryTree("root").nodeIsLeaf("")==True
    #BinaryTree("root").withNewBranches("","left", "right").nodeIsLeaf("r")==True
    #BinaryTree("root").withNewBranches("","left", "right").nodeIsLeaf("")==False
    def nodeIsLeaf(self, path):
        precondition(type(path)==type("") and self.nodeExists(path))
        for n in self.nodes:
            if n.getPath() == path:
                if(self.nodeExists(path+"l") or self.nodeExists(path+"r")):
                    return False
                return True
        return False
    
    #returns a new BianaryTree with the node at the given path replaced
    #with a new Node with same path and a the given value
    #BinaryTree("root").replaceValueWith("", "newRoot").getValueWithPath("")=="newRoot"
    #B.replaceValueWith("", "newRoot") changes B into ******* B.withNewBranches("", "newRoot")
    def replaceValueWith(self, path, value):
        precondition(type(path)==type("") and self.nodeExists(path))
        newList = []
        newBinaryTree = BinaryTree("")       
        for n in self.nodes:
            if n.path!=path:
                newList=newList+[n]
        newList=newList+[Node(value, path)]
        newBinaryTree.nodes = newList
        return newBinaryTree
    #returns a new BianaryTree with two new nodes branching off of the node
    #at the given pathOfStart that contain the values given
    def withNewBranches(self, pathOfStart, leftValue, rightValue):
        precondition(type(pathOfStart)==type("") and self.nodeExists(pathOfStart) and not (self.nodeExists(pathOfStart+"l") or self.nodeExists(pathOfStart+"r")))
        newBinaryTree = BinaryTree("")
        newBinaryTree.nodes = self.nodes+[Node(leftValue, pathOfStart+"l")]+[Node(rightValue, pathOfStart+"r")]
        return newBinaryTree
    def __eq__(self, other):
        precondition(type(self)==type(other))
        return listsHaveSameContents(self.nodes, other.nodes)
    def __repr__(self):
        
        toReturn = 'tree = BinaryTree("'+self.getValueWithPath("")+'")'
        nodesCopy = deepcopy(self.nodes)
        nodesCopy = sorted(nodesCopy, key=lambda nodes:len(nodes.getPath()), reverse=True)
        nodesCopy.pop()
        
        while(len(nodesCopy)>0):
            node1=nodesCopy.pop()
            node2=None
            for n in nodesCopy:
                if n.getPath()[0:-1]==node1.getPath()[0:-1]:
                    node2=nodesCopy.pop(nodesCopy.index(n))
                    
            if(node1.getPath()[-1]=='l'):
                toReturn=toReturn+'\ntree = tree.withNewBranches("'
                toReturn=toReturn+node1.getPath()[0:-1]
                toReturn=toReturn+'", "'
                toReturn=toReturn+node1.getValue()
                toReturn=toReturn+'", "'
                toReturn=toReturn+node2.getValue()
                toReturn=toReturn+'")'
            else:
                toReturn=toReturn+'\ntree = tree.withNewBranches("'
                toReturn=toReturn+node2.getPath()[0:-1]
                toReturn=toReturn+'", "'
                toReturn=toReturn+node2.getValue()
                toReturn=toReturn+'", "'
                toReturn=toReturn+node1.getValue()
                toReturn=toReturn+'")'
        
        return toReturn
         
class Node:
    def __init__(self, value, path):
        precondition(type(path)==type(""))
        self.value = value
        self.path = path
    def getPath(self):
        return self.path
    def getValue(self):
        return self.value
    def __eq__(self, other):
        return(self.path==other.path and self.value == other.value)
    
    
def listsHaveSameContents(list1, list2):
    precondition(type(list1)==type(list2)==type([]))
    list1 = sorted(list1, key=lambda nodes:nodes.path)
    list2 = sorted(list2, key=lambda nodes:nodes.path)
    return list1==list2
    
# mostly copied from  http://docs.python.org/lib/module-doctest.html
def _test():
    import doctest
    result = doctest.testmod()
    print "Result of doctest is:",
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1],  "tests!"
    else:
        print "Rats!"


if __name__ == "__main__":
    _test()
