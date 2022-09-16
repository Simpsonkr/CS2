def getUserInput():
    userInput=input('Please enter a string.')
    return userInput

def get_num_of_characters(userInput):
    numberOfCharacters=0
    for characters in userInput:
        numberOfCharacters+=1
    return numberOfCharacters

def removeWhitespace(userInput):
    tempString=''
    for characters in userInput:
        if ' ' !=characters:
            tempString=tempString+characters
    return tempString

if __name__ == '__main__':
    # Type your code here
    userInput=getUserInput()
    print(f'You entered: {userInput}')
    numberOfCharacters=get_num_of_characters(userInput)
    print(f'There are {numberOfCharacters} characters in the string')
    noWhitespace=removeWhitespace(userInput)
    print(f'The entered sting with no whitespace is: {noWhitespace}')
