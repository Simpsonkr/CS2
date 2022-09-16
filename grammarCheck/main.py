def getUserInput():
    return input('Please enter your text. ')

def printMenu():
    print('MENU')
    print('c-Number of non-whitespace characters')
    print('w-Number of Words')
    print('f-Fix Capitalization')
    print('r-Replace Punctuation')
    print('s-Shorten Spaces')
    print('q-Quit')
    menuChoice=input('\nChoose an Option ')
    return menuChoice

def executeMenu(userInput, menuChoice):
    if menuChoice=='c':
        print(f'Number of non-whitespace characters: {optionC(userInput)}')
    elif menuChoice=='w':
        print(f'Number of words: {optionW(userInput)}')
    elif menuChoice=='f':
        newString, changeCount=optionF(userInput)
        print(f'The text with edits is: {newString}')
        print(f'Number of edits: {changeCount}')

    elif menuChoice=='r':
        print()
    elif menuChoice=='s':
        print()
    return

def optionC(input):
    count=0
    for characters in input:
        if ' '!= characters:
            count=count+1
    return count

def optionW(input):
    count=1
    for characters in input:
        if ' '==characters:
            count=count+1
    return count

def optionF(userInput):
    lastCharacter = ' '
    tempString = ''
    count = 0
    if userInput[0].islower():
        tempString = tempString + userInput[0].upper()
        count += 1
    else:
        tempString = tempString + userInput[0]

    for i in range(1, len(userInput)):
        if (lastCharacter == '.' or lastCharacter == '!' or lastCharacter == '?') and userInput[i].islower():
            tempString = tempString + userInput[i].upper()
            count += 1
        else:
            tempString = tempString + userInput[i]
        if not userInput[i].isspace():
            lastCharacter = userInput[i]

    return tempString, count

def optionR(userInput):
    
    return

if __name__ == '__main__':
    userInput=getUserInput()
    print(f'You Entered: {userInput}')
    menuChoice=''
    while menuChoice != 'q':
        menuChoice=printMenu()
        if menuChoice in['c','w','f','r','s']:
            break
        elif menuChoice=='q':
            print('End')
        else:
            print('That is not an option.\n')
    executeMenu(userInput, menuChoice)
