#Guadalupe Rodriguez
#Exponent program

#PROGRAM GREETING
print('Welcome this program will help you solve exponential expressions.')
print()
print()

#intit.
responce = 'y'
while responce == 'y':

    #user input
    base= input('What base? ')
    power= int(input('What power of ' + base +' ? '))
    base = int(base)

    #calculations
    solution = base ** power
    print(base,'to the power of', power,'is', solution)
    print()

    #continue?
    responce = input('would you like to enter another (y/n): ')
print('Have a nice day.')
