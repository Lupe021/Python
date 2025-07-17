# Guadalupe Rodriguez
# Shipping Program

def displayWelcome():
    #program Greaating
    print('Welcome this program will calulate your subtotal, shipping, handling, and tax.')
    print(' )
    print()

def getInfo():
    shippingInfo = []
    moreInfo = True
    
    # quanity, item, and weight enter by user
    while moreInfo == True:
        quantity = int(input('Enter the quantity amount of a single item (enter 0 if done): '))

        if quantity == 0:
            moreInfo = False
        else:
            itemPrice = float(input('\nEnter Item price: '))
            itemWeight = float(input('\nEnter Item weight: '))
            print()
            shippingInfo.append([quantity, itemPrice, itemWeight])
    
    return shippingInfo

def calculation(shippingInfoList):
    #calculation
    totalWeight =  0
    subTotal = 0

    for indexValue in range(len(shippingInfoList)):
        quantity, itemPrice, itemWeight = shippingInfoList[indexValue]

        subTotal = subTotal + (quantity * itemPrice)
        
        totalWeight = totalWeight + (quantity * itemWeight)

    #Shipping & Handling
    shipping = totalWeight * 0.25

    if totalWeight < 10:
        handling = 1
    elif totalWeight > 100:
        handling = 5
    else:
        handling = 3
        
    shipAndHandling = shipping + handling

    return(subTotal, shipAndHandling)

def Continue():
    #continue
    response = input('\nWould you like to enter another (y/n): ')
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

#--------------------Main------------------------
# initialization
stop = False

# display program welcome
displayWelcome()

while stop == False:
    
    # shipping state
    state = input('Please enter the abbreviation of the state the product is being shipped to: ')
    state = state.upper();
    print()
    
    #user input
    shippingInfoList = getInfo()
    subTotal, shipAndHandling = calculation(shippingInfoList)
    
    #sales Tax
    if state == 'CA':
        salesTax= subTotal * 0.08
    else:
        salesTax = 0.00
    print()
    total = subTotal + shipAndHandling + salesTax
    
    #Result Display
    print(format('SubTotal: ', '<25'), format(subTotal, '>10,.2f'))
    print(format('SalesTax: ', '<25'), format(salesTax, '>10,.2f'))
    print(format('Shipping & Handling: ', '<25'), format(shipAndHandling, '>10,.2f'))
    print(format('Total: ', '<25'), format(total, '>10,.2f'))
    print()
    #continue
    stop = Continue()
