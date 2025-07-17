#Guadalupe Rodriguez
#number of breaths in years

#program greeting
print('welcome this program will calculate how many breaths and Heart Beats you have base on your age \nFor months please enter as a decemial point')
print()
print()

#intit.
responce = 'y'
while responce == 'y':

    #user input
    age = float(input('Enter an age: '))
    print()

    #Calculations for breaths per min.
    if age >= 15:
        solution = (525600 * 45) + (525600 * 5 * 25) + (525600 * 10 * 20) + (525600 * (age - 15) * 16)
    elif age >= 5:
        solution = (525600 * 45) + (525600 * 5 * 25) + (525600 * (age - 5) * 20)
    elif age >= 1:
        solution = (525600 * 45) + (525600 * (age - 1) * 25)
    else:
        solution = 45 * 525600 * age
    
    #Calculations for heart beats per min
    HeartBeat = 525600 * age * 67.5

    #Display
    print()
    print('On average you have breathed' ,format(solution , ',.0f'), 'per min throughout your life spand.')
    print()
    print('Your heart beats per min. is',format(HeartBeat ,',.0f'))
    print()

    #Continue?
    responce = input('Would you like to enter another (y/n): ')
    responce = responce. lower();
    print()
    while responce !='y' and responce !='n':
        responce = input("please enter 'y' or 'n': ")
        responce = responce. lower();
    print()
print('Thank you, have a nice day.')
    
