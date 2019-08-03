# CS-170

These programs tend to be based on recursion and all of them have some code that was used for testing purposed here at Haverford College. For that reason, they will not run on machines other than the ones that they were coded on. 

palindrome.py is a simple program that takes a string and returns whether or not it is a palindrome(it is spelled the same way forwards and baskwards).

isLegal.py and graphColoring.py are based on coloring a map, such that two adjacent land masses are never the same color. For example, if NJ and PA were next to each other and NJ was colored blue, then PA could not be colored blue. The maps are formatted in the following format: ("Ab Br Cg","AB BC"). Ab shows that the land mass A is the color blue, B is the color red and C is the color green. The second part of the statement shows that A is adjacent to B and B is adjacent to C(AB and BC respectively). isLegal.py takes an input in this format and checks whether or not that input is a valid coloring of a map. In other words it returns whether or not there are adjacent pieces of land of the same color. graphColoring.py, on the other hand, does this process in reverse and returns all legal colorings after being given an input in the format ("ABC","rgb","AB BC") where A, B and C are all of the pieces of land; r, g, and b are all of the colors on the map; AB and BC are the adjacencies of the pieces of land.

BinaryTree.py, Dictionary.py, and Dictionary_Faster.py are implementations of binary trees and dictionaries. All of these data types are made from scratch in this code.

TwentyQuestions.py takes the BinaryTree.py program previously mentioned to create a abbreviated game of 20 Questions.

checkers.py was my final project for this course, and it is an ASCII art version of checkers that can be played with another human player or a computer AI. During each turn, the player is presented with a list of possible pieces to move, and then the moves that chosen piece can make. The player chooses their piece and move by typing the number associated with that piece or move, and then pressing enter. This program relies very heavily on recursion to calculate all possible moves for each piece, especially when the move involves jumping another piece. 
