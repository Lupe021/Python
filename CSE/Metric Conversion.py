# Guadalupe Rodriguez
# Project 5: metric conversion

    
def displayWelcome():
    #Program Greeting
    print('Welcome this program will convert Inches/Centimeters, Ounce/Grams, & Kilometers/Miles.')
    print()
    print()

    
def getConvertTo():
    print('Enter I to convert from inches to centimeters & C for vice versa.')
    print('Enter O to convert from ounces or Grams & G for vice versa.')
    print('Enter M to convert from Miles or Kilometers & K for vice versa..')
    print()

    
    # wanted conversion enter by user
    variable = input('Enter a selection: ')
    variable = variable.upper();
    print()
    
    while variable !='I' and variable !='C' and variable !='O' and variable !='G' and variable !='M' and variable !='K':
        variable = input("Please enter an 'I', 'C', 'O', 'G', 'M', or 'K': ")
        variable = variable.upper();
        print()

    
    # weight/measurement entered
    weight = (float(input('Enter measurement/weight to convert: ')))
    print()
    return (variable, weight)

def doConversion(variable, weight):
    if variable == 'O':
        anwser = weight * 28.3495231
        number = 'onces equals'
        newNumber = 'grams'
    elif variable == 'G':
        anwser = weight / 28.3495231
        number = 'grams equals'
        newNumber = 'onces'
    elif variable == 'I':
        anwser = weight * 2.54
        number = 'Inches equals'
        newNumber = 'centimeters'
    elif variable == 'C':
        anwser = weight / 2.54
        number = 'Centimeters equals'
        newNumber = 'inches'
    elif variable == 'M':
        anwser = weight * 1.609344
        number = 'Miles equals'
        newNumber = 'kilometers'
    elif variable == 'K':
        anwser = weight / 1.609344
        number = 'Kilometers equals'
        newNumber = 'miles'

    #output
    print(weight, number, format(anwser, '.2f'), newNumber)
    print()


def Continue():
    #continue
    response = input('Would you like to enter another conversion (y/n): ')
    response = response. lower();
    print()
    while response !='y' and response !='n':
        response = input("Please enter 'y' or 'n': ")
        response = response. lower();

    if response == 'n':
        stop = True
    else:
        stop = False
    
    return stop

#---------------Main--------------

# initialization
stop = False

# display program welcome
displayWelcome()

while stop == False:
    
    # get user input
    variable, weight = getConvertTo()
    
    # do the conversion

    doConversion(variable, weight)
    #continue
    stop = Continue()

print('Have a nice day!')
    
