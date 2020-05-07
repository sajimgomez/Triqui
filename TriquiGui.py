from tkinter import *

from random import randint

TriquiPositions = [

    [None, None, None],

    [None, None, None],

    [None, None, None]

]


def EmptyPosition(Row, Col) :


    if TriquiPositions[Row][Col] == None :

        return True

    
    return False


def WaysToWin(String) : #Space complexity O(1), time complexity O(1)

    #By Rows

    for row in range(3) : #Space complexity O(1), time complexity O(1) because end of for is constant

        if TriquiPositions[row].count(String) == 3 : #Space complexity O(1), time complexity O(1)

            return True #Space complexity O(1), time complexity O(1)


    #By Columns

    for col in range(3) : #Space complexity O(1), time complexity O(1)

        for row in range(3) : #Space complexity O(1), time complexity O(1)

            if TriquiPositions[row][col] != String : #Space complexity O(1), time complexity O(1)

                break #Space complexity O(1), time complexity O(1)

            elif row == 2 : #Space complexity O(1), time complexity O(1)

                return True #Space complexity O(1), time complexity O(1)


    #By diagonals

    ByFirstDiagonal = True #Space complexity O(1), time complexity O(1)

    for RC in range(3) : #Space complexity O(1), time complexity O(1)

        if TriquiPositions[RC][RC] != String : #Space complexity O(1), time complexity O(1)


            ByFirstDiagonal = False #Space complexity O(1), time complexity O(1)


            break #Space complexity O(1), time complexity O(1)


    if ByFirstDiagonal : #Space complexity O(1), time complexity O(1)

        return True #Space complexity O(1), time complexity O(1)
    

    BySecondDiagonal = True #Space complexity O(1), time complexity O(1)


    for RC in range(3) : #Space complexity O(1), time complexity O(1)

        if TriquiPositions[2 - RC][RC] != String : #Space complexity O(1), time complexity O(1)

            BySecondDiagonal = False #Space complexity O(1), time complexity O(1)

            break #Space complexity O(1), time complexity O(1)


    if BySecondDiagonal : #Space complexity O(1), time complexity O(1)

        return True #Space complexity O(1), time complexity O(1)


    return False #Space complexity O(1), time complexity O(1)


def IsAllFull() : #Space complexity O(1), time complexity O(1)

    if None in TriquiPositions[0] or None in TriquiPositions[1] or None in TriquiPositions[2] : #Space complexity O(1), time complexity O(1)

        return False #Space complexity O(1), time complexity O(1)

    return True #Space complexity O(1), time complexity O(1)


Root = Tk()

Root.title('Triqui')

TriquiImage = PhotoImage(file = 'tic_tac_toe-512.png')

Root.iconphoto(False, TriquiImage)

XImage = PhotoImage(file = 'X.png')

OImage = PhotoImage(file = 'O.png')


def Choice(Row, Col) :


    if EmptyPosition(Row, Col) :

        Button(Root, image = XImage, state = DISABLED).grid(row = Row, column = Col)

        TriquiPositions[Row][Col] = 'X'

        
    if WaysToWin('X') :

        Label(Root, text = 'Ganaste!').grid(row = 3, column = 0, columnspan = 3)

        for i in range(3) :

            for j in range(3) :

                if EmptyPosition(i, j) :

                    Button(Root, state = DISABLED).grid(row = i, column = j)

        return


    PcRow = randint(0, 2)

    PcCol = randint(0, 2)


    while not EmptyPosition(PcRow, PcCol) :

        PcRow = randint(0, 2)

        PcCol = randint(0, 2)


    TriquiPositions[PcRow][PcCol] = 'O'

    Button(Root, image = OImage, state = DISABLED).grid(row = PcRow, column = PcCol)

    if WaysToWin('O') :

        Label(Root, text = 'Perdiste').grid(row = 3, column = 0, columnspan = 3)

        for i in range(3) :

            for j in range(3) :

                if EmptyPosition(i, j) :

                    Button(Root, state = DISABLED).grid(row = i, column = j)

        return

    
    if not WaysToWin('X') and not WaysToWin('O') and IsAllFull() :

        Label(Root, text = 'Empate').grid(row = 3, column = 0, columnspan = 3)

        return
    

B00 = Button(Root, command = lambda : Choice(0, 0), height = 5, width = 10).grid(row = 0, column = 0)

B01 = Button(Root, command = lambda : Choice(0, 1), height = 5, width = 10).grid(row = 0, column = 1)

B02 = Button(Root, command = lambda : Choice(0, 2), height = 5, width = 10).grid(row = 0, column = 2)

B10 = Button(Root, command = lambda : Choice(1, 0), height = 5, width = 10).grid(row = 1, column = 0)

B11 = Button(Root, command = lambda : Choice(1, 1), height = 5, width = 10).grid(row = 1, column = 1)

B12 = Button(Root, command = lambda : Choice(1, 2), height = 5, width = 10).grid(row = 1, column = 2)

B20 = Button(Root, command = lambda : Choice(2, 0), height = 5, width = 10).grid(row = 2, column = 0)

B21 = Button(Root, command = lambda : Choice(2, 1), height = 5, width = 10).grid(row = 2, column = 1)

B22 = Button(Root, command = lambda : Choice(2, 2), height = 5, width = 10).grid(row = 2, column = 2)

Result = Label(Root, text = '').grid(row = 3, column = 0, columnspan = 3)

Root.mainloop()