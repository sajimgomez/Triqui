import random #Space complexity O(1), time complexity O(1)

triquitable = [

    [None, None, None],
    [None, None, None],
    [None, None, None]

] #Space complexity O(1), time complexity O(1)



def ValidRowCol(i) :  #Space complexity O(1), time complexity O(1)

    if 0 <= i <= 2 :  #Space complexity O(1), time complexity O(1)

        return True   #Space complexity O(1), time complexity O(1)

    return False       #Space complexity O(1), time complexity O(1)



def EmptyPosition(row, col) : #Space complexity O(1), time complexity O(1)

    if triquitable[row][col] == None : #Space complexity O(1), time complexity O(1)

        return True  #Space complexity O(1), time complexity O(1)

    return False            #Space complexity O(1), time complexity O(1)



def ChoiceOfUser() : #Space complexity O(1), time complexity O(1)

    row = int(input(print('Digite numero de fila (0 - 2): '))) #Space complexity O(1), time complexity O(1)

    col = int(input(print('Digite numero de columna (0 - 2): '))) #Space complexity O(1), time complexity O(1)

    while not ValidRowCol(row) and not ValidRowCol(col) : #Space complexity O(1), time complexity O(1) if condition becomes true

        print('Digite rango adecuado para fila y columna') #Space complexity O(1), time complexity O(1)

        row = int(input(print('Digite numero de fila (0 - 2): '))) #Space complexity O(1), time complexity O(1)

        col = int(input(print('Digite numero de columna (0 - 2): '))) #Space complexity O(1), time complexity O(1)


    while not EmptyPosition(row, col) : #Space complexity O(1), time complexity O(1) if condition becomes true

        print('La casilla seleccionada está ocupada') #Space complexity O(1), time complexity O(1)

        row = int(input(print('Digite numero de fila (0 - 2): '))) #Space complexity O(1), time complexity O(1)

        col = int(input(print('Digite numero de columna (0 - 2): '))) #Space complexity O(1), time complexity O(1)


    triquitable[row][col] = 'X' #Space complexity O(1), time complexity O(1)




def ChoiceOfComputer() : #Space complexity O(1), time complexity O(1)

    row = random.randint(0, 2) #Space complexity O(1), time complexity O(1)

    col = random.randint(0, 2) #Space complexity O(1), time complexity O(1)

    while not EmptyPosition(row, col) : #Space complexity O(1), time complexity O(1) if condition becomes true

        row = random.randint(0, 2) #Space complexity O(1), time complexity O(1)

        col = random.randint(0, 2) #Space complexity O(1), time complexity O(1)


    triquitable[row][col] = 'O' #Space complexity O(1), time complexity O(1)


def WhoPlayFirst() : #Space complexity O(1), time complexity O(1)

    IsS = input(print('''Si desea comenzar presione "s" luego enter de lo 
 contrario presione otra tecla y luego enter: '''))  #Space complexity O(1), time complexity O(1)

    if IsS == 's' : #Space complexity O(1), time complexity O(1)

        Turn = 'User' #Space complexity O(1), time complexity O(1)

    else : #Space complexity O(1), time complexity O(1)

        Turn = 'Computer' #Space complexity O(1), time complexity O(1)

    
    return Turn #Space complexity O(1), time complexity O(1)

    

def ChangePlayTurn(Turn) : #Space complexity O(1), time complexity O(1)

    if Turn == 'User' : #Space complexity O(1), time complexity O(1)

        Turn = 'Computer' #Space complexity O(1), time complexity O(1)

    else : #Space complexity O(1), time complexity O(1) 

        Turn = 'User' #Space complexity O(1), time complexity O(1)


    return Turn #Space complexity O(1), time complexity O(1)


def IsAllFull() : #Space complexity O(1), time complexity O(1)

    if None in triquitable[0] or None in triquitable[1] or None in triquitable[2] : #Space complexity O(1), time complexity O(1)

        return False #Space complexity O(1), time complexity O(1)

    return True #Space complexity O(1), time complexity O(1)


def WaysToWin(String) : #Space complexity O(1), time complexity O(1)

    #By Rows

    for row in range(3) : #Space complexity O(1), time complexity O(1) because end of for is constant

        if triquitable[row].count(String) == 3 : #Space complexity O(1), time complexity O(1)

            return True #Space complexity O(1), time complexity O(1)


    #By Columns

    for col in range(3) : #Space complexity O(1), time complexity O(1)

        for row in range(3) : #Space complexity O(1), time complexity O(1)

            if triquitable[row][col] != String : #Space complexity O(1), time complexity O(1)

                break #Space complexity O(1), time complexity O(1)

            elif row == 2 : #Space complexity O(1), time complexity O(1)

                return True #Space complexity O(1), time complexity O(1)


    #By diagonals

    ByFirstDiagonal = True #Space complexity O(1), time complexity O(1)

    for RC in range(3) : #Space complexity O(1), time complexity O(1)

        if triquitable[RC][RC] != String : #Space complexity O(1), time complexity O(1)


            ByFirstDiagonal = False #Space complexity O(1), time complexity O(1)


            break #Space complexity O(1), time complexity O(1)


    if ByFirstDiagonal : #Space complexity O(1), time complexity O(1)

        return True #Space complexity O(1), time complexity O(1)
    

    BySecondDiagonal = True #Space complexity O(1), time complexity O(1)


    for RC in range(3) : #Space complexity O(1), time complexity O(1)

        if triquitable[2 - RC][RC] != String : #Space complexity O(1), time complexity O(1)

            BySecondDiagonal = False #Space complexity O(1), time complexity O(1)

            break #Space complexity O(1), time complexity O(1)


    if BySecondDiagonal : #Space complexity O(1), time complexity O(1)

        return True #Space complexity O(1), time complexity O(1)


    return False #Space complexity O(1), time complexity O(1)


def TriquiGame() : #Space complexity O(1), time complexity O(1)

    print() #Space complexity O(1), time complexity O(1)
    print(triquitable[0]) #Space complexity O(1), time complexity O(1)
    print(triquitable[1]) #Space complexity O(1), time complexity O(1)
    print(triquitable[2]) #Space complexity O(1), time complexity O(1)
    print() #Space complexity O(1), time complexity O(1)

    Turn = WhoPlayFirst() #Space complexity O(1), time complexity O(1) 


    while not IsAllFull() : #Space complexity O(1), time complexity O(1)


        if Turn == 'User' : #Space complexity O(1), time complexity O(1)

            ChoiceOfUser() #Space complexity O(1), time complexity O(1)

            print() #Space complexity O(1), time complexity O(1)
            print(triquitable[0]) #Space complexity O(1), time complexity O(1)
            print(triquitable[1]) #Space complexity O(1), time complexity O(1)
            print(triquitable[2]) #Space complexity O(1), time complexity O(1)
            print() #Space complexity O(1), time complexity O(1)

            if WaysToWin('X') : #Space complexity O(1), time complexity O(1)
                
                print('Ganaste') #Space complexity O(1), time complexity O(1)

                return #Space complexity O(1), time complexity O(1)

            Turn = ChangePlayTurn(Turn) #Space complexity O(1), time complexity O(1)


        else : #Space complexity O(1), time complexity O(1)

            ChoiceOfComputer() #Space complexity O(1), time complexity O(1)

            print() #Space complexity O(1), time complexity O(1)
            print(triquitable[0]) #Space complexity O(1), time complexity O(1)
            print(triquitable[1]) #Space complexity O(1), time complexity O(1)
            print(triquitable[2]) #Space complexity O(1), time complexity O(1)
            print() #Space complexity O(1), time complexity O(1)

            if WaysToWin('O') : #Space complexity O(1), time complexity O(1)

                print('Perdiste') #Space complexity O(1), time complexity O(1)

                return #Space complexity O(1), time complexity O(1)

            Turn = ChangePlayTurn(Turn) #Space complexity O(1), time complexity O(1)

    
    if not WaysToWin('X') and not WaysToWin('O') : #Space complexity O(1), time complexity O(1)

        print('Empate') #Space complexity O(1), time complexity O(1)

        return #Space complexity O(1), time complexity O(1)



TriquiGame() #Space complexity O(1), time complexity O(1)





        



    
    
