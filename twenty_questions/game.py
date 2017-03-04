"""
Welcome to 20 Questions: Drink Edition!!!
To play, just type 'yes' or 'no'.

Is it hot?no
Is it a type of juice?yes
Is it orange juice?no
Darn, I didn't get it.
What drink were you thinking of? (Is it ...?)Is it grape juice?
What's a question to distinguish that from my answer?Does the fruit grow on a tree?
What is the answer to your question for your answer?no

Is it hot?no
Is it a type of juice?yes
Does the fruit grow on a tree?no
Is it grape juice?yes
Yay!!! I got it :D

Is it hot?no
Is it a type of juice?yes
Does the fruit grow on a tree?yes
Is it orange juice?yes
Yay!!! I got it :D
"""

from BinaryTree import *

#left is yes, right is no
tree = BinaryTree("Is it hot?")
tree = tree.withNewBranches("", "Is it sweet?", "Is it a type of juice?")
tree = tree.withNewBranches("r", "Does the fruit grow on a tree?", "Is it carbonated?")
tree = tree.withNewBranches("l", "Is it Hot Chocolate?", "Is it Coffee?")
tree = tree.withNewBranches("rl", "Is it orange juice?", "Is it grape juice?")
tree = tree.withNewBranches("rr", "Is it clear?", "Is it clear?")
tree = tree.withNewBranches("rrr", "Is it water?", "Is it milk?")
tree = tree.withNewBranches("rrl", "Is it Sprite?", "Is it Coke?")

print("Welcome to 20 Questions: Drink Edition!!!")
print("To play, just type 'yes' or 'no'.\n")

while(True):
    path = ""
    gameOver = 0 #changes to 1 after a round finishes
    printTree = True #Toggles whether or not the tree is printed after rounds
    while(gameOver==0):
        response = raw_input(tree.getValueWithPath(path))
        if(response=="yes"):
            if(tree.nodeIsLeaf(path)):
                print"Yay!!! I got it :D\n"
                gameOver=1
            path=path+"l"
        elif(response=="no"):
            if(tree.nodeIsLeaf(path)):
                print"Darn, I didn't get it."
                newValue = raw_input("What drink were you thinking of? (Is it ...?)")
                newQuestion = raw_input("What's a question to distinguish that from my answer?")
                sideForNewValue = raw_input("What is the answer to your question for your answer?\n")
                
                oldValue = tree.getValueWithPath(path)
                tree = tree.replaceValueWith(path, newQuestion)
                if(sideForNewValue=="yes"):
                    tree = tree.withNewBranches(path, newValue, oldValue)
                elif(sideForNewValue=="no"):
                    tree = tree.withNewBranches(path, oldValue, newValue)
                gameOver=1
            path=path+"r"
    if printTree:
        print(tree)
        print("\n")
            
        
        

