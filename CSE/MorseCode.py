# Guadalupe Rodriguez
# Morse Code Translator


# intializtion
stop = False
while stop == False:
    transOut = ''
    # English To Morse
    MorseKey = (('a', '.-'), ('b', '-...'), ('c', '-.-.'), ('d', '-..'), ('e', '.'),
                    ('f', '..-.'), ('g', '--.'), ('h', '....'), ('i', '..'), ('j', '.---'), ('k', '-.-'), ('l', '.-..'),
                    ('m', '--'), ('n', '-.'), ('o', '---'), ('p', '.--.'), ('q', '--.-'), ('r', '.-.'), ('s', '...'),
                    ('t', '-'), ('u', '..-'), ('v', '...-'), ('w', '.--'), ('x', '-..-'), ('y', '-.--'), ('z', '--..'))

    # program Greating
    print("Welcome to the Morse code Translator.")
    print()
    print()
    print('When entering morse code please enter spaces between letters.')
    print()
    # pick to translate
    which = input('Enter(m) to translate to morse code or (e) to translate to english: ')

    while which != 'm' and which != 'e':
            which = input("Enter 'm' or 'e': ")
            which = which.lower();
    print() 
    # see if condition is true or false
    toMorse = (which == 'm')

    # get sentence
    transInput = input('Enter sentence/word you would like translated: ')
    print()
    
    #perform morse code/ english translation
    if toMorse == True:
        transInput = transInput.lower();
        fromIndex = 0
        toIndex = 1
    else:
        transInput = transInput.split()
        fromIndex = 1
        toIndex = 0


    for character in transInput: #iterates over input
        letterFound = False # set to False
        if which == 'm':
            for mainIndex in MorseKey:
                if character == mainIndex[fromIndex]:
                    transOut = transOut + " " + mainIndex[toIndex]
                    letterFound = True
        else:
            for mainIndex in MorseKey: #iterates over
                if character == mainIndex[fromIndex]:
                    transOut = transOut + mainIndex[toIndex]
                    letterFound = True

    #output
    if transInput == True:
        print('your english translation is: ',transOut)
    else:
        print('your morse translation is: ',transOut)
    print()
    
    #reset
    transOut = ''
    
    #continue?
    response = input('Would you like to enter other translation? (y/n) : ')
    response = response.lower();
    print()
    
    while response != 'y' and response != 'n':
        response = input("please enter a 'y' or 'n': ")
        response = response.lower();
        print()
        
    if response == 'n':
        stop = True
        


