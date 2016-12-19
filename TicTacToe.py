#Name: Ovidiu Mitroi
#Student ID: 6832432
#Blog: https://cumahara.coventry.ac.uk/view/view.php?id=117323
import time
import pickle
import random
import turtle
def midGrids():
    """Returns a list of the coordinates of the midpoints in the 9 squares of the board."""
    #######################################################################################
    #-This function is only used by the turtle aspect of the game.
    #-The coordinates of the squares are already known, I used this function to quickly calculate
    #the midpoint coordinates of my squares
    #######################################################################################
    x=-120
    y=40
    aList=[]
    for i in range(3):
        x=-120
        if i!=0:
            y-=80
        
        
        for j in range(3):
            x2=x+80
            y2=y+80
            aList.append((round((x+x2)/2,2),round((y+y2)/2,2)))
            x=x2
    return aList
midp=midGrids()                                                     #constant list of coordinates
sq=[((-120,-40),(40,120)),((-40,40),(40,120)),((40,120),(40,120)),
         ((-120,-40),(-40,40)),((-40,40),(-40,40)),((40,120),(-40,40)),
         ((-120,-40),(-120,-40)),((-40,40),(-120,-40)),((40,120),(-120,-40))]        #constant list -coordinates of squares
def turtleBoard():
    "Draws the turtle board."""
    #############################################
    #-left top corner is at -120,120
    #-right bottom corner is at 120,-120
    # 1 side length is 80
    #############################################
    scr=turtle.Screen()
    scr.title("Tic-Tac-Toe")
    scr.setup(0.4,0.6,800,0)
    t=turtle.Turtle()
    t.pensize(8)
    t.speed(0)
    y=120
    for i in range(4):
        t.pu()
        t.goto(-120,y)
        t.pd()
        t.fd(240)
        y-=80
    x=-120
    t.right(90)
    for i in range(4):
        t.pu()
        t.goto(x,120)
        t.pd()
        t.forward(240)
        x+=80
    return scr
def updateTurtleBoard(game=[" "," "," "," "," "," "," "," "," "],sign="",pos=0,first=False):
    """Function to update the turtleBoard appropriately."""
    ########################################################
    # - Role of boolean first is to properly update the board if the game has been loaded.
    # - The function checks the entire board list if first==True, else it just updates the last move made
    ########################################################
    if first:
        for i in range(len(game)):
            if game[i]=="X":
                drawX(i)
            elif game[i]=="O":
                drawACircle(i)
    else:
        if sign=="X":
            drawX(pos)
        elif sign=="O":
            drawACircle(pos)
    return None


def drawACircle(i):
    """Draw a circle on the turtleBoard."""
    mimi=turtle.Turtle()
    mimi.ht()
    mimi.shape("circle")
    mimi.shapesize(3)
    mimi.pu()
    mimi.goto(midp[i][0],midp[i][1])
    mimi.st()
    return None
def drawX(i):
    """Draws an X on the turtleBoard."""
    mimi=turtle.Turtle()
    mimi.ht()
    mimi.pu()
    x1=sq[i][0][0]
    x2=sq[i][0][1]
    y1=sq[i][1][0]
    y2=sq[i][1][1]
    mimi.goto(x1,y1)
    mimi.pensize(4)
    mimi.speed(0)
    mimi.left(45)
    mimi.fd(25)
    mimi.pd()
    mimi.fd(60)
    mimi.pu()
    mimi.goto(x1,y1+80)
    mimi.right(90)
    mimi.fd(25)
    mimi.pd()
    mimi.fd(60)
    return None
         
def updateBoard(g,sign,pos):
    '''Checks if the player input is valid, if it is this function updates the game List appropriately.'''
    if pos in range(1,10) and g[pos-1]==" ":
        g[pos-1]=sign
        return None
    elif pos in range(1,10):
        raise ValueError ("That position is taken. Try Again!\n")
    else:
        raise ValueError ("Your input must be between 1 and 9. Try Again!\n")
def printBoard(aList):
    '''Function to print the board.'''
    tab=" "*25
    print(tab+" ______________ ")
    print(tab+"|1   |2   |3   |")
    print(tab+"| "+aList[0]+"  | "+aList[1]+"  | "+aList[2]+"  |")
    print(tab+"|____|____|____|")
    print(tab+"|4   |5   |6   |")
    print(tab+"| "+aList[3]+"  | "+aList[4]+"  | "+aList[5]+"  |")
    print(tab+"|____|____|____|")
    print(tab+"|7   |8   |9   |")
    print(tab+"| "+aList[6]+"  | "+aList[7]+"  | "+aList[8]+"  |")
    print(tab+"|____|____|____|")
    print("\n"*10)
def tutorial():
    """Function to display how the game works"""
    #This function is called once at the beginning of the game, its purpose is
    #to teach the user how to play the game
    tut=[" "," "," "," "," "," "," "," "," "]
    print("\nFirst, let's teach you the basics of the game.")
    time.sleep(2)
    print("This is what the board looks like:\n")
    printBoard(tut)
    time.sleep(2)
    print("Notice that each part of the grid is numbered, from 1 to 9. In order to place an X or O on the board, you must enter the respective number when prompted.")
    print("\nFor Example:")
    time.sleep(6)
    print("\nLet's say I want to play my next move on square 4. I wait for my move and I type 4 and press ENTER\n\n")
    printBoard(tut)
    scr=turtleBoard()
    print("Player 1 turn: ",end='')
    time.sleep(5)
    print("4")
    time.sleep(2)
    tut[3]='X'
    printBoard(tut)
    updateTurtleBoard(tut,"X",3)
    print("\n There it is. Now you try it.")
    time.sleep(2)
    while True:
        print("Choose a square and press ENTER.")
        try:
            nr=int(input("Your turn: "))
            if nr in range(1,10) and tut[nr-1]==" ":
                tut[nr-1]="O"
                printBoard(tut)
                updateTurtleBoard(tut,"O",nr-1)
                break
            else:
                print("Your input is not valid or the square is already taken. Try Again!\n")
                continue
        except ValueError:
            print("Your input must be a number between 1 and 9. Try Again!\n")
            continue
    print("Well Done. Now you know the commands")
    time.sleep(3)
    print("The game is won when a player succeeds in filling a row,column or diagonal with the same element")
    time.sleep(2)
    print("If the board is full and nobody won, the game finishes in a tie.")
    time.sleep(4)
    print("That' all, You are now ready to play! GO HAVE FUN!! ")
    input("Press ENTER to exit the tutorial")
    scr.bye()
def checkWin(g):
    '''Check all winning scenarios.'''
    ##################################
    #-Returns True  if a winning scenario is fulfilled
    #-Returns False otherwise
    ##################################
    if g[0]!=" ":
        if g[0]==g[1] and g[0]==g[2]:
            return True,g[2]
        elif g[0]==g[3] and g[0]==g[6]:
            return True,g[0]
        elif g[0]==g[4] and g[0]==g[8]:
            return True,g[0]
    if g[1]!=" ":
        if g[1]==g[4] and g[1]==g[7]:
            return True,g[1]
    if g[3]!=" ":
        if g[3]==g[4] and g[3]==g[5]:
            return True,g[3]
    if g[6]!=" ":
        if g[6]==g[7] and g[6]==g[8]:
            return True,g[6]
        elif g[6]==g[4] and g[6]==g[2]:
            return True,g[6]
    if g[2]!=" ":
        if g[2]==g[5] and g[2]==g[8]:
            return True,g[2]
    return False,''
def multiPlayer(game=[" "," "," "," "," "," "," "," "," "],turn=0,mode="m"): 
    '''Simulates Player vs Player version of the game'''

    scr=turtleBoard()              #create TurtleBoard
    updateTurtleBoard(game,first=True)  #update it (specifically useful if the game was loaded
    gameOn=True
    print("Player 1 goes first and his symbol is X.")
    print("Player 2 goes second and his symbol is O.")
    time.sleep(3)
    stop,winner=checkWin(game)      #fnction call checkWin
    
    print("\n"*30)
    print("At any point in the game you can write 'save' or 's' to save the game.\n")
    print("At any point in the game you can write 'exit' or 'x' to quit the game without saving it.\n")
    printBoard(game)                #function call printBoard
    
    while not stop:
        turn+=1
        if turn % 2 == 1:
            sign="X"
            player="Player 1"
        else:
            sign="O"
            player="Player 2"
        gameOn=playerMove(player,sign,game,mode) #function call playerMove
        if gameOn==False:
                print("\n"*15+"You have chosen to exit the game. Thank you for playing.")
                return None
            
        print("\n"*30)
        print("MULTI-PLAYER"+"\n"*5)
        print("At any point in the game you can write 'save' or 's' to save the game.\n")
        print("At any point in the game you can write 'exit' or 'x' to quit the game without saving it.\n")
        printBoard(game)             #function call printBoard
        stop,winner=checkWin(game)   #function call checkWin
        if " " not in game and winner=="":
            print("It's a tie! No winner this time!")
            return None
    if winner=="X":
        print("Player 1 wins! Congratulations!")
        return None
    else:
        print("Player 2 wins! Congratulations!")
        return None
def winNow(g,sign):
    """
    This functions checks if its possible to end the game with the next move.
        Returns 0 if False
        Return a number between 1 and 9 representing where the next move should be played to finish the game.
    """
    gamecopy=g.copy()
    for i in range(len(g)):
        if g[i]==" ":
            gamecopy[i]=sign
            won,xsign=checkWin(gamecopy)
            if won:
                return i+1
            else:
                gamecopy[i]=" "
    return 0
def saveg(game,mode):
    "Function to save the game."""
    ##############################################################
    # - Player chooses his file name
    # - Game is stored in <filename>.txt
    # - <filename>.txt is added to savenames.txt which holds all the files containing saved games
    ##############################################################
    try:
        g=open("savenames.txt","ab")
        name=input("\nChoose a name for your save file: ") + ".txt"
        f=open(name,"wb")
        pickle.dump((game,mode),f)
        pickle.dump(name,g)
        print("Your file has been saved in the filename: %s" %(name))
    finally:
        f.close()
        g.close()
def loadg():
    """Function to load a game. Returns the gameList, game Mode("m","s1" or "s0") and turn"""
    #########################################################################################
    #-Function first lists all the current file names in savenames.txt
    #-Player chooses an option
    #-Function opens the file with that name and then counts how many elements are different than " "
    #-Returns the game list, game mode, and count+1 which represents the next turn
    #########################################################################################
    try:
        f=open("savenames.txt","rb")
        aList=[]
        while True:
            try:
                file=pickle.load(f)
                aList.append(file)
            except EOFError:
                break
        print("Which game would you like to load?\n")
        for i in range(len(aList)):
            print("%s.  %s"%(i+1,aList[i]))
        while True:
            xStr=input("Choice: ")
            try:
                x=int(xStr)

                if x in range(1,len(aList)+1):
                    gname=aList[x-1]
                    g=open(gname,"rb")
                    (game,mode)=pickle.load(g)
                    g.close()
                    count=0
                    for i in game:
                        if i!=" ":
                            count+=1
                    return (game,count,mode)
                
                else:
                    print("That is not a valid choice. Try again! ")
                    continue
            except ValueError:
                print("You must choose a number in the specified range.")
                continue
            finally:
                f.close()
    except FileNotFoundError:
        print("There are no saved games currently")
        return None,None,None
    

def singlePlayer(mode,game=[" "," "," "," "," "," "," "," "," "],turn=0):
    """Simulates a single-player game between user and computer."""

    ######################################################
    #In this block:
    #-Turtle Board is created and then updated in case the game was loaded
    scr=turtleBoard()
    updateTurtleBoard(game,first=True)
    #######################################################
    gameOn=True                       
    stop,winner=checkWin(game)
    print("\n"*30)
    print("At any point in the game you can write 'save' or 's' to save the game.\n")
    print("At any point in the game you can write 'exit' or 'x' to quit the game without saving it.\n")
    printBoard(game)
    if mode=="s1":
        psign="X"
        csign="O"
        player=1
    else:
        psign="O"
        csign="X"
        player=0
    while not stop:
        turn+=1
        if turn % 2 == player:
            gameOn=playerMove("Player",psign,game,mode)
            if gameOn==False:
                print("\n"*15+"You have chosen to exit the game. Thank you for playing.")
                break
            
        else:
            #Computer will first check if its possible to win this turn
            print("Computer is thinking...")
            time.sleep(2)
            fin=winNow(game,csign)
            if fin>0:
                updateBoard(game,csign,fin)
                updateTurtleBoard(game,csign,fin-1)
            #-----------------------------------------------
            else:
                #Computer will now check if player is about the win and will try to block
                fin=winNow(game,psign)
                if fin>0:
                    updateBoard(game,csign,fin)
                    updateTurtleBoard(game,csign,fin-1)
                #-----------------------------------------------------
                else:
                #As a final tactic, computer will choose a random square for its input
                    while True:
                        try:
                            cmove=random.randrange(1,10)
                            updateBoard(game,csign,cmove)
                            updateTurtleBoard(game,csign,cmove-1)
                            break
                        except ValueError as e:
                            continue
                #--------------------------------------------------------

        
        print("\n"*30)
        print("SINGLE PLAYER "+"\n"*5)
        print("At any point in the game you can write 'save' or 's' to save the game.\n")
        print("At any point in the game you can write 'exit' or 'x' to quit the game without saving it.\n")
        
        printBoard(game)
        stop,winner=checkWin(game)
        if " " not in game and winner=="":
            print("It is a tie. Nobody won!")
            return None
        elif winner==psign:
            print("You win! Congrats! ")
            return None
        elif winner==csign:
            print("Computer wins! Try again later!")
            return None
def playerMove(player,sign,game,mode):
    """Asks the player to make his next move."""
    ############################################
    #- If input is "exit" or "x", player chooses to exit the game without saving
    #- If input is "save" or "s", player saves the game
    #- If input is a number between 1 and 9, player chooses to make his next move
    ############################################
    while True:    
        print(" YOU ARE %s." %sign)
        nrStr=input(player+ " turn.\n\tEnter your next move: ").lower()
        if nrStr=='exit' or nrStr[0]=='x':
            return False
        if nrStr=='save' or nrStr[0]=='s':
            saveg(game,mode)
            continue
            
        else:
        
            try:
                nr=int(nrStr)
            except ValueError:
                print("Your input must be a number. Try Again!\n\n")
                continue
            try:
                updateBoard(game,sign,nr)
                updateTurtleBoard(game,sign,nr-1)
                break
            except ValueError as e:
                print(e)
                continue
    return True
def playGame():
    """Main function of the game. Controls the flow of the game"""
    
    #---------------------------------------------------------------
    #In this block, ask the user if he wants to see the tutorial and do error checks
    #for input
    print("\n"*20)
    print("\t\t\tHello and welcome to Tic-Tac-Toe\n\n\t\t\t\tby Ovidiu Mitroi\n\n\n\n\n\n\n")
    while True:
        s=input("\n\nWould you like to play the tutorial? (Write Yes or No)\n")
        s=s.lower()
        if s=="yes":
            tutorial()
            break
        elif s=="no":
            break
        else:
            print("Wrong input!")
            continue
    #----------------------------------------------------------------
    ################################################################
    #          IN THIS BLOCK
    #- Menu options are presented to the player
    #- Firstly, player can choose New Game or Load Game
    #- In case of New Game:
    #       -Player chooses Multiplayer or Single-Player
    #       -In case of Single-Player:
    #               -Player chooses to go First or Second
    #- This function redirects the flow of the game depending on Player choices
    #- Game modes are : "m" - Multiplayer
    #                   "s1" - Single-Player, Player goes first
    #                   "s0" - Single-Player, Player goes second
    print("\n1.New Game\n2.Load Game")
    while True:
        xStr=input("Choice: ")
        try:
            x=int(xStr)
            if x==1:
                print("Choose a game mode: \n\t1. Multiplayer\n\t2. Single Player")
                while True:
                    s=input("\nChoice: ").lower()
                    if s=="1":
                        multiPlayer()
                    elif s=="2":
                        while True:
                            print("Would you like to play: \n1.First.\n2.Second")
                            x=input("Enter your choice here: ").lower()
                            if x=='1':
                                singlePlayer("s1")
                                break
                            elif x=='2':
                                singlePlayer("s0")
                                break
                            else:
                                print("Your input is not valid. Try again! \n")
                                continue
            
                            break
                   
                    else:
                        print("Your input is not valid. Try again! \n")
                        continue
                    return None
        
            elif x==2:
                game,turn,mode=loadg()
                #######################
                #if no saved games, return to selecting choice
                if game==None:
                    continue
                #########################
                if mode=="m":
                    whoWon=multiPlayer(game,turn)
                    break
                else:
                    singlePlayer(mode,game,turn)
                    break
            else:
                print("Your input is invalid. Try again!")
                continue
        
        except ValueError:
            print("Your input must be a 1 or 2.")
            continue
        break
    #######################################################################################

    
        
        
playGame()

