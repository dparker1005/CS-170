"""
>>> p = Piece(1, 2, True)
>>> print p
r(1,2)
>>> p.setCoords(5,6)
>>> print p
r(5,6)

>>> m = Move(p, 6, 7, [])
>>> print m
r(5,6)-->r(6,7)

>>> b = Board()
>>> print b
   1  2  3  4  5  6  7  8
1    [r]   [r]   [r]   [r]
2 [r]   [r]   [r]   [r]   
3    [r]   [r]   [r]   [r]
4 [ ]   [ ]   [ ]   [ ]   
5    [ ]   [ ]   [ ]   [ ]
6 [b]   [b]   [b]   [b]   
7    [b]   [b]   [b]   [b]
8 [b]   [b]   [b]   [b]   
<BLANKLINE>

>>> UserInteraction().stringIsInteger("3")
True
>>> UserInteraction().stringIsInteger("Apple")
False
>>> UserInteraction().stringIsInteger("123Apple456")
False

"""

from operator import __eq__
from copy import deepcopy
import random
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print "Can't find logic.py; if this happens in the CS teaching lab, tell your instructor"
    print "   If you are using a different computer, add logic.py to your project"
    print "   (You can download logic.py from http://www.cs.haverford.edu/resources/software/logic.py)"
    sys.exit(1)
 
 
class Board:
#pieces is the list of all pieces on the board
    #init makes the array of pieces and puts them where they should be
    #to start game
    def __init__(self):
        self.pieces = []
        for i in range(1, 5):
            self.pieces = self.pieces + [Piece((i*2), 1, True)]
            self.pieces = self.pieces + [Piece((i*2)-1, 2, True)]
            self.pieces = self.pieces + [Piece((i*2), 3, True)]
            self.pieces = self.pieces + [Piece((i*2)-1, 6, False)]
            self.pieces = self.pieces + [Piece((i*2), 7, False)]
            self.pieces = self.pieces + [Piece((i*2)-1, 8, False)]
    #returns a copy of Board after a Move m has been made
    def boardWithMove(self, m):
        newPieces = []
        #removes dead pieces and the piece that was moved
        for p in self.pieces:
            add = not p==m.piece
            for dead in m.dead:
                if p==dead:
                    add = False
            if add:
                newPieces = newPieces+[p]
        #add in the piece that was moved
        pieceToAdd = deepcopy(m.newPiece)
        pieceToAdd.setCoords(m.newX, m.newY)
        newPieces = newPieces+[pieceToAdd]
        toReturn = Board()
        toReturn.pieces = newPieces
        return toReturn
    #A recursive function that gets all possible jumping moves for
    #a Piece pCopy on a Board boardCopy. Needs to know if the piece
    #is originally a king before starting to jump
    def getRecursiveJumps(self, pCopy, boardCopy, isOriginallyKing):
        moves = []
        if pCopy.y <7 and pCopy.isRed and not isOriginallyKing:
            #tests if red can jump left
            if pCopy.x>2:
                #piece that will be jumped
                toJump = boardCopy.getPiece(pCopy.x-1, pCopy.y+1)
                #location that will be jumped to
                toLand = boardCopy.getPiece(pCopy.x-2, pCopy.y+2)
                #if toJump is a piece and toLand is empty
                if isinstance(toJump, Piece) and not isinstance(toLand, Piece):
                    #if toJump is not the same color
                    if not toJump.isRed:
                        #make and add the new move
                        newMove = Move(pCopy, pCopy.x-2, pCopy.y+2, [toJump])
                        moves = [newMove]+moves
                        #make a new board and piece based on move
                        newBoard = boardCopy.boardWithMove(newMove)
                        newP = deepcopy(pCopy)
                        newP.setCoords(newMove.newX, newMove.newY)
                        #get jumps from new location recursively
                        moreJumps = self.getRecursiveJumps(newP, newBoard, False)
                        #add recursive options to current list of possible moves
                        for m in moreJumps:
                            #update moves
                            m.piece = pCopy
                            m.dead = [toJump]+m.dead
                            moves = [m]+moves
            #tests if red can jump right
            if pCopy.x<7:
                toJump = boardCopy.getPiece(pCopy.x+1, pCopy.y+1)
                toLand = boardCopy.getPiece(pCopy.x+2, pCopy.y+2)
                if isinstance(toJump, Piece) and not isinstance(toLand, Piece):
                    if not toJump.isRed:
                        newMove = Move(pCopy, pCopy.x+2, pCopy.y+2, [toJump])
                        moves = [newMove]+moves
                        newBoard = boardCopy.boardWithMove(newMove)
                        newP = deepcopy(pCopy)
                        newP.setCoords(newMove.newX, newMove.newY)
                        moreJumps = self.getRecursiveJumps(newP, newBoard, False)
                        for m in moreJumps:
                            m.piece = pCopy
                            m.dead = [toJump]+m.dead
                            moves = [m]+moves
        elif pCopy.y>2 and not pCopy.isRed and not isOriginallyKing:
            if pCopy.x>2:
                #tests if black can jump left
                toJump = boardCopy.getPiece(pCopy.x-1, pCopy.y-1)
                toLand = boardCopy.getPiece(pCopy.x-2, pCopy.y-2)
                if isinstance(toJump, Piece) and not isinstance(toLand, Piece):
                    if toJump.isRed:
                        newMove = Move(pCopy, pCopy.x-2, pCopy.y-2, [toJump])
                        moves = [newMove]+moves
                        newBoard = boardCopy.boardWithMove(newMove)
                        newP = deepcopy(pCopy)
                        newP.setCoords(newMove.newX, newMove.newY)
                        moreJumps = self.getRecursiveJumps(newP, newBoard, False)
                        for m in moreJumps:
                            m.piece = pCopy
                            m.dead = [toJump]+m.dead
                            moves = [m]+moves
            if pCopy.x<7:
                #tests if black can jump right
                toJump = boardCopy.getPiece(pCopy.x+1, pCopy.y-1)
                toLand = boardCopy.getPiece(pCopy.x+2, pCopy.y-2)
                if isinstance(toJump, Piece) and not isinstance(toLand, Piece):
                    if toJump.isRed:
                        newMove = Move(pCopy, pCopy.x+2, pCopy.y-2, [toJump])
                        moves = [newMove]+moves
                        newBoard = boardCopy.boardWithMove(newMove)
                        newP = deepcopy(pCopy)
                        newP.setCoords(newMove.newX, newMove.newY)
                        moreJumps = self.getRecursiveJumps(newP, newBoard, False)
                        for m in moreJumps:
                            m.piece = pCopy
                            m.dead = [toJump]+m.dead
                            moves = [m]+moves
        elif isOriginallyKing:
            #same as above, but in all 4 directions. works for both
            #red and black kings
            if pCopy.x>2:
                if pCopy.y<7:
                    toJump = boardCopy.getPiece(pCopy.x-1, pCopy.y+1)
                    toLand = boardCopy.getPiece(pCopy.x-2, pCopy.y+2)
                    if isinstance(toJump, Piece) and not isinstance(toLand, Piece):
                        if toJump.isRed!=pCopy.isRed:
                            newMove = Move(pCopy, pCopy.x-2, pCopy.y+2, [toJump])
                            moves = [newMove]+moves
                            newBoard = boardCopy.boardWithMove(newMove)
                            newP = deepcopy(pCopy)
                            newP.setCoords(newMove.newX, newMove.newY)
                            moreJumps = self.getRecursiveJumps(newP, newBoard, True)
                            for m in moreJumps:
                                m.piece = pCopy
                                m.dead = [toJump]+m.dead
                                moves = [m]+moves
                if pCopy.y>2:
                    toJump = boardCopy.getPiece(pCopy.x-1, pCopy.y-1)
                    toLand = boardCopy.getPiece(pCopy.x-2, pCopy.y-2)
                    if isinstance(toJump, Piece) and not isinstance(toLand, Piece):
                        if toJump.isRed!=pCopy.isRed:
                            newMove = Move(pCopy, pCopy.x-2, pCopy.y-2, [toJump])
                            moves = [newMove]+moves
                            newBoard = boardCopy.boardWithMove(newMove)
                            newP = deepcopy(pCopy)
                            newP.setCoords(newMove.newX, newMove.newY)
                            moreJumps = self.getRecursiveJumps(newP, newBoard, True)
                            for m in moreJumps:
                                m.piece = pCopy
                                m.dead = [toJump]+m.dead
                                moves = [m]+moves
            if pCopy.x<7:
                if pCopy.y<7:
                    toJump = boardCopy.getPiece(pCopy.x+1, pCopy.y+1)
                    toLand = boardCopy.getPiece(pCopy.x+2, pCopy.y+2)
                    if isinstance(toJump, Piece) and not isinstance(toLand, Piece):
                        if toJump.isRed!=pCopy.isRed:
                            newMove = Move(pCopy, pCopy.x+2, pCopy.y+2, [toJump])
                            moves = [newMove]+moves
                            newBoard = boardCopy.boardWithMove(newMove)
                            newP = deepcopy(pCopy)
                            newP.setCoords(newMove.newX, newMove.newY)
                            moreJumps = self.getRecursiveJumps(newP, newBoard, True)
                            for m in moreJumps:
                                m.piece = pCopy
                                m.dead = [toJump]+m.dead
                                moves = [m]+moves
                if pCopy.y>2:
                    toJump = boardCopy.getPiece(pCopy.x+1, pCopy.y-1)
                    toLand = boardCopy.getPiece(pCopy.x+2, pCopy.y-2)
                    if isinstance(toJump, Piece) and not isinstance(toLand, Piece):
                        if toJump.isRed!=pCopy.isRed:
                            newMove = Move(pCopy, pCopy.x+2, pCopy.y-2, [toJump])
                            moves = [newMove]+moves
                            newBoard = boardCopy.boardWithMove(newMove)
                            newP = deepcopy(pCopy)
                            newP.setCoords(newMove.newX, newMove.newY)
                            moreJumps = self.getRecursiveJumps(newP, newBoard, True)
                            for m in moreJumps:
                                m.piece = pCopy
                                m.dead = [toJump]+m.dead
                                moves = [m]+moves
        return moves
    #gets all moves for a given Piece p. first checks for all movement and then calls
    #other function to check recursively for jumps
    def getMoves(self, p):
        moves = []
        if p.y<8 and p.isRed and not p.isKing:
            #check red movement
            if(p.x!=1):
                #check movement left
                pieceCheck = self.getPiece(p.x-1, p.y+1)
                if not isinstance(pieceCheck, Piece):
                    moves = moves+[Move(p, p.x-1, p.y+1, [])]
            if(p.x!=8):
                #check movement right
                pieceCheck = self.getPiece(p.x+1, p.y+1)
                if not isinstance(pieceCheck, Piece):
                    moves = moves+[Move(p, p.x+1, p.y+1, [])]       
        elif p.y>1 and not p.isRed and not p.isKing:
            #check black movement
            if(p.x!=1):
                pieceCheck = self.getPiece(p.x-1, p.y-1)
                if not isinstance(pieceCheck, Piece):
                    moves = moves+[Move(p, p.x-1, p.y-1, [])]
            if(p.x!=8):
                pieceCheck = self.getPiece(p.x+1, p.y-1)
                if not isinstance(pieceCheck, Piece):
                    moves = moves+[Move(p, p.x+1, p.y-1, [])]
        elif p.isKing:
            #check movement for all kings, color doesn't matter
            #works same way as above
            if(p.x!=1):
                if(p.y!=8):
                    pieceCheck = self.getPiece(p.x-1, p.y+1)
                    if not isinstance(pieceCheck, Piece):
                        moves = moves+[Move(p, p.x-1, p.y+1, [])]
                    if(p.y!=1):
                        pieceCheck = self.getPiece(p.x-1, p.y-1)
                        if not isinstance(pieceCheck, Piece):
                            moves = moves+[Move(p, p.x-1, p.y-1, [])]
            if(p.x!=8):
                if(p.y!=8):
                    pieceCheck = self.getPiece(p.x+1, p.y+1)
                    if not isinstance(pieceCheck, Piece):
                        moves = moves+[Move(p, p.x+1, p.y+1, [])] 
                if(p.y!=1):
                    pieceCheck = self.getPiece(p.x+1, p.y-1)
                    if not isinstance(pieceCheck, Piece):
                        moves = moves+[Move(p, p.x+1, p.y-1, [])]
        #gets all the recursive jump possibilities        
        jumps = self.getRecursiveJumps(deepcopy(p), deepcopy(self), p.isKing)
        return jumps+moves
    #returns the piece at a given x,y coordinate
    #if piece doesn't exist, returns -1
    def getPiece(self, x, y):
        for p in self.pieces:
            if p.x==x and p.y==y:
                return p
        return -1
    #makes Move m on this board
    #works same way as boardWithMove()
    def makeMove(self, m):
        newPieces = []
        for p in self.pieces:
            add = not p==m.piece
            for dead in m.dead:
                if p==dead:
                    add = False
            if add:
                newPieces = newPieces+[p]
        pieceToAdd = deepcopy(m.newPiece)
        pieceToAdd.setCoords(m.newX, m.newY)
        newPieces = newPieces+[pieceToAdd]
        self.pieces = newPieces
    #returns a user-friendly representation of the board
    def __str__(self):
        toReturn = "   1  2  3  4  5  6  7  8\n"
        for n in range(1, 9):
            #n is y coordinate
            toReturn = toReturn+str(n)+' '
            for m in range(1, 9):
                #m is x coordinate
                if (n+m)%2 == 0:
                #calculate the blank spaces
                    toReturn = toReturn+"   "
                else:
                #fill in the spaces
                    p = self.getPiece(m, n)
                    if isinstance(p, Piece):
                        letterToAdd = ""
                        if p.isRed==True:
                            if p.isKing:
                                letterToAdd = 'R'
                            else:
                                letterToAdd = 'r'
                        else:
                            if p.isKing:
                                letterToAdd = 'B'
                            else:
                                letterToAdd = 'b'
                        toReturn = toReturn+"["+letterToAdd+"]"
                    else:
                        toReturn = toReturn+"[ ]"
            toReturn = toReturn+"\n"
        return toReturn         

class computerPlayer:
    #gets all possible moves that the computer can make
    def getAllRedMoves(self, board):
        allMoves = []
        for p in board.pieces:
            if p.isRed:
                for m in board.getMoves(p):
                    allMoves = allMoves+[m]
        return allMoves
    #chooses a move and makes the move for red
    def playTurnForRed(self, board):
        allRedMoves = self.getAllRedMoves(deepcopy(board))
        if not isinstance(allRedMoves, list):
            print "There are no moves to be made. Stalemate."
            return 0
        if len(allRedMoves)==0:
            print "There are no moves to be made. Stalemate."
            return 0
        bestMoves = []
        moveToBeMade = 0
        
        #checks if a piece can become king
        for m in allRedMoves:
            if m.newPiece.isKing and not m.piece.isKing:
                bestMoves = bestMoves+[m]
        if len(bestMoves)!=0:
            #looks for the way to become a king with the most jumps
            mostJumps = [bestMoves[0]]
            for n in bestMoves:
                if len(n.dead)>len(mostJumps[0].dead):
                    mostJumps = [n]
                elif len(n.dead)==len(mostJumps[0].dead):
                    mostJumps = mostJumps+[n]
            moveToBeMade = mostJumps[0]
         
        #check for jumps   
        if not isinstance(moveToBeMade, Move):
            bestMoves = [allRedMoves[0]]    
            for m in allRedMoves:
                #looks for the highest amount of jumps
                #that can be made
                if len(m.dead)>len(bestMoves[0].dead):
                    bestMoves = [m]
                elif len(m.dead)==len(bestMoves[0].dead):
                    bestMoves = bestMoves+[m]
            if len(bestMoves[0].dead)>0:
                #if the highest number of jumps are the same,
                #moves the piece that is farthest forward
                farthestForward = [bestMoves[0]]
                for n in bestMoves:
                    if n.newY>farthestForward[0].newY:
                        farthestForward = [n]
                    elif n.newY==farthestForward[0].newY:
                        farthestForward = farthestForward+[n]
                moveToBeMade = farthestForward[0]
                        
        if not isinstance(moveToBeMade, Move):
            bestMoves = []    
            for m in allRedMoves:
                if (m.piece.x!=1 and m.piece.x!=8 and m.piece.y!=1) or m.piece.isKing:
                    #tries to move pieces that are kings OR aren't in back or on sides first
                    bestMoves = bestMoves+[m]
                    if (m.newX==1 or m.newX==8) and not m.piece.isKing:
                    #prioritizes moving pieces that aren't kings onto sides
                        bestMoves = [m]+bestMoves
            if len(bestMoves)!=0:
                moveToBeMade = bestMoves[0]
                
        if not isinstance(moveToBeMade, Move):
            bestMoves = []    
            for m in allRedMoves:
                #tries to move anything that isn't on back line
                if m.piece.y!=1:
                    bestMoves = bestMoves+[m]
            if len(bestMoves)!=0:
                #chooses a random possible move
                moveToBeMade = bestMoves[randrange(0, len(bestmoves))] 
        
        if not isinstance(moveToBeMade, Move):
            #chooses a random possible move
            moveToBeMade = allRedMoves[randrange(0, len(allRedMoves))]  
        
        board.makeMove(moveToBeMade)    
        
        #checks if red has won
        for p in board.pieces:
            if p.isRed!=False:
                return 1
        return 2

class Game:
    #creates the board, asks if user wants to play vs computer and calls startGame()
    def __init__(self):
        self.board = Board()
        self.computerOpponent = UserInteraction().askYN("Would you like to play against\na computer opponent? (y/n)")
        self.startGame()
    #allows a human to play a turn. if isRed=True, it is red's turn. else it's black's
    def playTurn(self, isRed):
        #becomes true once a move has been chosen
        turnOver = False
        move = None
        piecesWithMoves = []
        #finds pieces with moves
        for p in self.board.pieces:
            if p.isRed==isRed and len(self.board.getMoves(p))>0:
                piecesWithMoves = piecesWithMoves+[p]
        #checks for stalemate
        if len(piecesWithMoves)==0:
            print "There are no moves to be made. Stalemate."
            return 0
        while not turnOver:
            #asks user which piece to move
            toMove = UserInteraction().askPiece(piecesWithMoves)
            if(not isinstance(toMove, Piece)):
                return 0
            #asks user which move to make for chosen piece
            moveToMake = UserInteraction().askMove(self.board.getMoves(toMove))
            if(isinstance(moveToMake, Move)):
                move = moveToMake
                turnOver = True
        self.board.makeMove(move)
        #check for win
        for p in self.board.pieces:
            if p.isRed!=isRed:
                return 1
        return 2
    def startGame(self):
        #game loop to run game until someone wins or quits
        #b=0: User decided to quit or there is a stalemate
        #b=1: Turn went normally
        #b=2: Player has won
        while True:
            print "\n----------------------------\nBlack's Turn!"
            print self.board
            b = self.playTurn(False)
            if b==0:
                print "The game has been ended."
                return
            if b==2:
                print "\Black has won!!!"
                return
            print "\n----------------------------\nRed's Turn!"
            r = 0
            if self.computerOpponent:
                r = computerPlayer().playTurnForRed(self.board)
            else:
                print self.board
                r = self.playTurn(True)
            if r==0:
                print "The game has been ended."
                return
            if r==2:
                print "\nRed has won!!!"
                return

class Move:
# piece is the piece that would be moved with this Move
# newX and newY are integers where 1,1 is the upper right corner of the board
# dead is a list of Piece objects that would die with this Move
    def __init__(self, piece, newX, newY, dead):
        self.piece = piece
        self.newX = newX
        self.newY = newY
        self.dead = dead
        
        self.newPiece = deepcopy(piece)
        if newY==1 or newY==8:
            self.newPiece.isKing = True
    def __str__(self):
        
        if len(self.dead)==0:
            #if there are no jumps
            newPiece = deepcopy(self.newPiece)
            newPiece.setCoords(self.newX, self.newY)
            return self.piece.__str__()+"-->"+newPiece.__str__()
        toReturn = self.piece.__str__()
        currentX = self.piece.x
        currentY = self.piece.y
        #loops to show how the piece gets to where it ends up and 
        #what it kills
        for d in self.dead:
            if currentX>d.x:
                currentX = currentX-2
            else:
                currentX = currentX+2
            if currentY>d.y:
                currentY = currentY-2
            else:
                currentY = currentY+2
            pCopy = deepcopy(self.piece)
            pCopy.setCoords(currentX, currentY)
            if currentY==1 or currentY==8:
                pCopy.isKing = True
            toReturn = toReturn+"-->"+pCopy.__str__()
        return toReturn
        
class Piece:
# x and y are integers where 1,1 is the upper right corner of the board
# isRed and isKing are boolean
    def __init__(self, x, y, isRed): 
        self.x = x
        self.y = y 
        self.isRed = isRed
        self.isKing = False
    def setCoords(self, x, y):
        self.x = x
        self.y = y 
    def __eq__(self, other):
        return (self.x==other.x and self.y==other.y and self.isRed==other.isRed and self.isKing==other.isKing)
    def __str__(self):
        toReturn = ""
        if self.isRed==True:
            if self.isKing:
                toReturn = toReturn + 'R'
            else:
                toReturn = toReturn + 'r'
        else:
            if self.isKing:
                toReturn = toReturn + 'B'
            else:
                toReturn = toReturn + 'b'
        return toReturn + "("+str(self.x)+","+str(self.y)+")"

class UserInteraction:
    #asks a yes or no question
    def askYN(self, question):
        response = raw_input(question)
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print "That is not a valid answer.\nPlease only respond with y or n.\n"
            return self.askYN(question)
    #asks which piece a player wants to move, given a list of pieces with moves
    def askPiece(self, pieces):
        index = 0
        for p in pieces:
            print str(index+1)+". "+p.__str__()
            index=index+1
        print "0. Exit Game"
        response = raw_input("Which piece would you like to move?") 
        if self.stringIsInteger(response):
            if int(response)<=len(pieces):
                if int(response)==0:
                    if self.askYN("Are you sure you want to exit? (y/n)"):
                        return 0
                    else:
                        return self.askPiece(pieces)
                return pieces[int(response)-1]
        print "Please enter a valid integer.\n"
        #recursive call if answer is not valid
        return self.askPiece(pieces)
    #asks which move a player wants to make, given a list of moves
    def askMove(self, moves):
        index = 0
        print "\n--------------\n"
        for m in moves:
            print str(index+1)+". "+m.__str__()
            index=index+1
        print "0. Choose Piece"
        response = raw_input("Which move would you like to make?") 
        if self.stringIsInteger(response):
            if int(response)<=len(moves):
                if int(response)==0:
                    return 0
                return moves[int(response)-1]
        print "Please enter a valid integer.\n"
        #recursive call if answer is not valid
        return self.askMove(moves)
    #returns whether or not a string an integer
    #Ex: "123"=True   "12ABC34"=False
    def stringIsInteger(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False

Game()

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