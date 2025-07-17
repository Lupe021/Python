#Guadalupe Rodriguez
#State name and Abbreviation

#Program Greeting
print('Welcome this program is designed to help you find the state name or abbreviation')
print()
print()

#init.
stop = False
while stop == False:


    # State List:
    stateName = ('alabama', 'alaska', 'american samoa', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut',
                 'delaware', 'district of columbia', 'florida', 'georgia', 'guam', 'hawaii', 'idaho','illinois', 'indiana',
                 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts','michigan', 'minnesota',
                 'minor outlying islands', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire',
                 'new jersey', 'new mexico', 'new york', 'north carolina', 'north dakota', 'northern mariana islands',
                 'ohio','oklahoma', 'oregon', 'pennsylvania', 'puerto rico', 'rhode island', 'south carolina', 'south dakota',
                 'tennessee', 'texas', 'u.s. virgin islands', 'utah', 'vermont', 'virginia', 'washington', 'west virginia',
                 'wisconsin', 'wyoming')
    stateAbbrev = ('al', 'ak', 'as', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'dc', 'fl', 'ga', 'gu', 'hi', 'id', 'il','in',
                    'ia','ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn','um', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh','nj',
                    'nm', 'ny', 'nc', 'nd','cm', 'oh', 'ok', 'or', 'pa', 'pr', 'ri', 'sc', 'sd', 'tn', 'tx', 'vi','ut',
                    'vt', 'va', 'wa', 'wv', 'wi', 'wy')
    
    #User Input:
    which = input('Enter (n) to find the state name from abbreviation \nor (a) to find the abbreviation: ')
    which = which. lower();
    
    while which != 'n' and which != 'a':
        which = input("Error. Please enter 'n'or'a': ")
        which = which.lower();
    print()
    
    state = input('Please enter the state name or abbreviation: ')
    state = state. lower();
    print()

    
   #check List:
    for mainIndex in range(len(stateName)):
            if state == stateName[mainIndex]:
                output = 'The abbreviatoin is ' +stateAbbrev[mainIndex].upper()

    for mainIndex in range(len(stateAbbrev)):
            if state == stateAbbrev[mainIndex]:
                output = 'The state name is ' +stateName[mainIndex].upper()


    # output
    print(output)
    print()

    
    #continue
    response = input('Would you like to enter another? (y/n) : ')
    response = response.lower();
    print()
    
    while response != 'y' and response != 'n':
        response = input("please enter a 'y' or 'n': ")
        response = response.lower();
        print()
        
    if response == 'n':
        stop = True
