"""
  Dictionary class, and two implementations

>>> testing = Dictionary()
>>> testing.put(1, 'x')

>>> d = Dictionary()
>>> d.put('Dave', 4973)
>>> d.put('J.D.', 4993)
>>> d.put('CS lab', 1202)
>>> d.lookup('Dave')
4973

>>> d.put('Dave', 1202)  # when Dave is working in the lab
>>> d.lookup('Dave')
1202
>>> d.lookup('CS lab')
1202

>>> d.lookup('Steven')
'No entry'

>>> d2 = d.withEntry('Steven', 1203)
>>> d.lookup('Steven')
'No entry'

>>> d2.lookup('Steven')
1203

>>> d2==d2
True

>>> d3 = d2.withEntry('Steven', 0)
>>> d2==d3
False
>>> d3
d = Dictionary1()
d.put("CS lab", 1202)
d.put("Dave", 1202)
d.put("J.D.", 4993)
d.put("Steven", 0)

>>> d4 = d3.withEntry('Steven', 1203)
>>> d2==d4
True
>>> d4
d = Dictionary1()
d.put("CS lab", 1202)
d.put("Dave", 1202)
d.put("J.D.", 4993)
d.put("Steven", 1203)

>>> d4 = Dictionary().withEntry("key1", 1).withEntry("key666", 666).withEntry("key2", 2)
>>> d5 = Dictionary().withEntry("key3", 3).withEntry("key666", 42).withEntry("key4", 4)
>>> d5b= Dictionary().withEntry("key666", 42).withEntry("key3", 3).withEntry("key4", 4)
>>> d5 == d5b
True
>>> d5 == d4
False
>>> d6 = d4.withDictionary(d5)
>>> d6.lookup("key1")
1
>>> d6.lookup("key2")
2
>>> d6.lookup("key3")
3
>>> d6.lookup("key4")
4
>>> d6.lookup("key666")
42
>>> d6
d = Dictionary1()
d.put("key1", 1)
d.put("key2", 2)
d.put("key3", 3)
d.put("key4", 4)
d.put("key666", 42)


"""
# make Python look in the right place for logic.py, or complain if it doesn't
from copy import deepcopy
from operator import itemgetter
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
    from BinaryTree import *
except:
    print "Can't find logic.py; if this happens in the CS teaching lab, tell your instructor"
    print "   If you are using a different computer, add logic.py to your project"
    print "   (You can download logic.py from http://www.cs.haverford.edu/resources/software/logic.py)"
    sys.exit(1)



class Dictionary1:
    """
        A dictionary represented with a Python list.
        Each list element is a tuple of two parts, the key and the value
    """
    def __init__(self):
        precondition(True)
        self.__listOfPairs = []
        self.__rep_inv__()

    def withEntry(self, key, value):
        precondition(True)
        result = Dictionary1()
        listCopy = deepcopy(self.__listOfPairs)
        lowerBound = 0
        upperBound = len(listCopy)
        while(upperBound-lowerBound>0):
            #uppserBound is larger than lowerBound, listCopy[lowerBound]<key, 
            #listCopy[upperBound]>key, upperBound-lowerBound is about half of previous iteration
            if key == listCopy[(upperBound-lowerBound-1)/2+lowerBound][0]:
                listCopy[(upperBound-lowerBound-1)/2+lowerBound][1] = value
                result.__listOfPairs=listCopy
                return result
            elif key > listCopy[(upperBound-lowerBound-1)/2][0]:
                lowerBound = (upperBound-lowerBound+1)/2+lowerBound
            else:
                upperBound = (upperBound-lowerBound-1)/2
        listCopy.insert(lowerBound, [key, value])
        result.__listOfPairs=listCopy
        #result.__rep_inv__()
        return result

    # axioms:
    #  Dictionary().lookup(x) === "No entry"
    #  d.withEntry(k, v).lookup(x) === v, if k==x
    #                          or d.lookup(x), otherwise
    def lookup(self, key):
        precondition(True)
        listCopy = self.__listOfPairs
        lowerBound = 0
        upperBound = len(listCopy)
        while(upperBound-lowerBound>0):
            #uppserBound is larger than lowerBound, listCopy[lowerBound]<key, 
            #listCopy[upperBound]>key, upperBound-lowerBound is about half of previous iteration
            if key == listCopy[(upperBound-lowerBound-1)/2+lowerBound][0]:
                return listCopy[(upperBound-lowerBound-1)/2+lowerBound][1]
            elif key > listCopy[(upperBound-lowerBound-1)/2][0]:
                lowerBound = (upperBound-lowerBound+1)/2+lowerBound
            else:
                upperBound = (upperBound-lowerBound-1)/2
        return "No entry"


    # axioms:
    #  d.put(k, v) --> new d is d.withEntry(k, v)
    #  d.put(k, v) returns the updated d, so d.put(k1, v1),put(k2, v2) is legal
    def put(self, key, value):
        precondition(True)
        listCopy = self.__listOfPairs
        lowerBound = 0
        upperBound = len(listCopy)
        while(upperBound-lowerBound>0):
            #uppserBound is larger than lowerBound, listCopy[lowerBound]<key, 
            #listCopy[upperBound]>key, upperBound-lowerBound is about half of previous iteration
            if key == listCopy[(upperBound-lowerBound-1)/2+lowerBound][0]:
                listCopy[(upperBound-lowerBound-1)/2+lowerBound][1] = value
                return 
            elif key > listCopy[(upperBound-lowerBound-1)/2][0]:
                lowerBound = (upperBound-lowerBound+1)/2+lowerBound
            else:
                upperBound = (upperBound-lowerBound-1)/2
        listCopy.insert(lowerBound, [key, value])
        #result.__rep_inv__()

    def __eq__(self,otherDictionary):
        precondition( isinstance(otherDictionary,Dictionary1) )
        list1 = deepcopy(self.__listOfPairs)
        list2 = deepcopy(otherDictionary.__listOfPairs)
        
        list1copy = deepcopy(list1)
        list2copy = deepcopy(list2)
        
        for i in list1:
            for n in list2:
                if(i[0]==n[0] and i[1]==n[1]):
                    list1copy.remove(i)
                    list2copy.remove(n)
                    
        if(len(list1copy)==0 and len(list2copy)==0):
            return True
        return False
    
    # axioms:
    #  Dictionary().withEntry("key1", 1).withDictionary(Dictionary().withEntry("key2", 2)) == Dictionary().withEntry("key1", 1).withEntry("key2", 2)
    #  Dictionary().withEntry("key2", 2).withDictionary(Dictionary().withEntry("key1", 1)) == Dictionary().withEntry("key1", 1).withEntry("key2", 2)
    #  Dictionary().withEntry("key1", 1).withDictionary(Dictionary().withEntry("key1", 2)) == Dictionary().withEntry("key1", 2)
   
    def withDictionary(self, otherDictionary):
        precondition( isinstance(otherDictionary,Dictionary1) )
        d = Dictionary1()
        d.__listOfPairs = self.__listOfPairs
        for x in otherDictionary.__listOfPairs:
            d.put(x[0], x[1])
        d.__rep_inv__()
        return d
    
    def merge(self, otherDictionary):
        precondition( isinstance(otherDictionary,Dictionary1) )
        precondition( isinstance(otherDictionary,Dictionary1) )
        d = self
        d.__listOfPairs = self.__listOfPairs
        for x in otherDictionary.__listOfPairs:
            d.put(x[0], x[1])
        self.__rep_inv__()
  
    def __repr__(self):
        precondition(True)
        toReturn = 'd = Dictionary1()'
        for i in self.__listOfPairs:
            toReturn=toReturn+'\nd.put("'+str(i[0])+'", '+str(i[1])+')'
        return toReturn
    
    def __rep_inv__(self):
        precondition(True)
        for x in range(0, len(self.__listOfPairs)-1):
            if(self.__listOfPairs[x][0]>self.__listOfPairs[x+1][0]):
                print "__rep_inv__ IS BROKEN!!!"
                return False
        return True
            
        

class Dictionary2:
    """
        A dictionary represented with a binary tree
    """
    def __init__(self):
        precondition(True)
        self.tree = BinaryTree("")
    # "extending" constructor method: 'withEntry'
    #  d.withEntry(k, v) has all the key/value pairs of d, together with a new entry
    def withEntry(self, key, value):
        precondition(True)
        t = deepcopy(self)
        if(t.tree.getValueWithPath("") == ""):
            t.tree = BinaryTree([key, value])
            return t
        else:
            path = ""
            while(True):
                #check for duplicates
                if(key==t.tree.getValueWithPath(path)[0]):
                    t.tree = t.tree.replaceValueWith(path, [key, value])
                    t.__rep_inv__()
                    return t
                
                #create the path for where value should go
                newPath = path
                if(key>t.tree.getValueWithPath(path)[0]):
                    newPath=newPath+"r"
                elif(key<t.tree.getValueWithPath(path)[0]):
                    newPath=newPath+"l"
                
                #Check if a value already exists there
                if(t.tree.nodeExists(newPath)):
                    if(t.tree.getValueWithPath(newPath)==""):
                        t.tree = t.tree.replaceValueWith(newPath, [key, value])
                        t.__rep_inv__()
                        return t
                    else:
                        path = newPath
                else:
                    if(key>t.tree.getValueWithPath(path)):
                        t.tree = t.tree.withNewBranches(path, "", [key, value]) 
                        t.__rep_inv__()
                        return t
                    elif(key<t.tree.getValueWithPath(path)):
                        t.tree = t.tree.withNewBranches(path, [key, value], "") 
                        t.__rep_inv__()
                        return t
    # axioms:
    #  Dictionary().lookup(x) === "No entry"
    #  d.withEntry(k, v).lookup(x) === v, if k==x
    #                          or d.lookup(x), otherwise
    def lookup(self, key):
        precondition(True)
        t = self.tree
        path = ""
        while(True):
            if(not t.nodeExists(path)):
                break
            if(t.getValueWithPath(path) == ""):
                break
            if(t.getValueWithPath(path)[0]==key):
                return t.getValueWithPath(path)[1]
            elif(t.getValueWithPath(path)[0]>key):
                path = path+"l"
            else:
                path = path+"r"
        return 'No entry'


    # axioms:
    #  d.put(k, v) --> new d is d.withEntry(k, v)
    #  d.put(k, v) returns the updated d, so d.put(k1, v1),put(k2, v2) is legal
    def put(self, key, value):
        precondition(True)
        t = self
        if(t.tree.getValueWithPath("") == ""):
            t.tree = BinaryTree([key, value])
            self.__rep_inv__()
            return
        else:
            path = ""
            while(True):
                #check for duplicates
                if(key==t.tree.getValueWithPath(path)[0]):
                    t.tree = t.tree.replaceValueWith(path, [key, value])
                    self.__rep_inv__()
                    return
                
                #create the path for where value should go
                newPath = path
                if(key>t.tree.getValueWithPath(path)[0]):
                    newPath=newPath+"r"
                elif(key<t.tree.getValueWithPath(path)[0]):
                    newPath=newPath+"l"
                
                #Check if a value already exists there
                if(t.tree.nodeExists(newPath)):
                    if(t.tree.getValueWithPath(newPath)==""):
                        t.tree = t.tree.replaceValueWith(newPath, [key, value])
                        self.__rep_inv__()
                        return
                    else:
                        path = newPath
                else:
                    if(key>t.tree.getValueWithPath(path)):
                        t.tree = t.tree.withNewBranches(path, "", [key, value]) 
                        self.__rep_inv__()
                        return
                    elif(key<t.tree.getValueWithPath(path)):
                        t.tree = t.tree.withNewBranches(path, [key, value], "") 
                        self.__rep_inv__()
                        return
 


    def __eq__(self,otherDictionary):
        precondition( isinstance(otherDictionary,Dictionary2) )
        return self.tree.nodes==otherDictionary.tree.nodes
    
    # axioms:
     #  Dictionary().withEntry("key1", 1).withDictionary(Dictionary()) == Dictionary().withEntry("key1", 1)
    #  Dictionary().withEntry("key1", 1).withDictionary(Dictionary().withEntry("key2", 2)) == Dictionary().withEntry("key1", 1).withEntry("key2", 2)
    #  Dictionary().withEntry("key1", 1).withDictionary(Dictionary().withEntry("key1", 2)) == Dictionary().withEntry("key1", 2)
    def withDictionary(self, otherDictionary):
        precondition( isinstance(otherDictionary,Dictionary2) )
        d = deepcopy(self)
        toAdd = deepcopy(otherDictionary.tree.nodes)
        for x in toAdd:
            if(not x.value==""):
                d = d.withEntry(x.value[0], x.value[1])
        d.__rep_inv__()
        return d
    
    def merge(self, otherDictionary):
        precondition( isinstance(otherDictionary,Dictionary2) )
        d = self
        toAdd = deepcopy(otherDictionary.tree.nodes)
        for x in toAdd:
            if(not x.value==""):
                d.put(x.value[0], x.value[1])
        self.__rep_inv__()
        
    def __repr__(self):
        precondition(True)
        toReturn = 'd = Dictionary2()'
        list = self.tree.nodes
        for i in list:
            if(i.value!=""):
                toReturn=toReturn+'\nd.put("'+str(i.value[0])+'", '+str(i.value[1])+')'
        return toReturn
    
    def __rep_inv__(self):
        precondition(True)
        t = self.tree
        for x in t.nodes:
            if(x.value == ""):
                continue
            if(t.nodeExists(x.path+"l")):
                if(t.getValueWithPath(x.path+"l")!=""):
                    if(x.value[0] <= t.getLeftValue(x.path)[0]):
                        print "__rep_inv__ IS BROKEN!!!"
                        return False
            if(t.nodeExists(x.path+"r")):
                if(t.getValueWithPath(x.path+"r")!=""):
                    if(x.value[0] >= t.getRightValue(x.path)[0]):
                        print "__rep_inv__ IS BROKEN!!!"
                        return False
        return True






# by default, use the first representation, but this is changed in DocTest below
Dictionary = Dictionary1

# mostly copied from  http://docs.python.org/lib/module-doctest.html
def _test():
    import doctest
    global Dictionary
    whatever_dictionary_was = Dictionary

    print "=========================== Running doctest tests for Dictionary1 ===========================\n"
    Dictionary = Dictionary1
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1],  "tests!"
    else:
        print "Rats!"

    print "\n\n\n\n"
    print "=========================== Running doctest tests for Dictionary2 ===========================\n"
    Dictionary = Dictionary2
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1],  "tests!"
    else:
        print "Rats!"
    Dictionary = whatever_dictionary_was

if __name__ == "__main__":
    _test()
