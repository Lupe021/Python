# Guadalupe Rodriguez
# USB Calculator


# program greeting
print(' Welcome to the USB storage Calculator')
print()
print()
#init
stop = False
while stop == False:
    
    # Assign vales to User Input
    Size= int(input('Enter USB size in Gigabyes: '))
    print()
    mp= int(input('Enter either an 8,10,or 12 for your resolution: '))
    print()
    if mp== 8:
        res= 2840 * 2160
    elif mp== 10:
        res=3872 * 2592
    elif mp== 12:
        res= 4000 * 3000
        
    # Calculations
    SizeByes= Size*1000000000
    
    GIF= SizeByes//(res/5)

    JPEG= SizeByes//((res * 3)/8)
    PNG= SizeByes//((res * 3)/10)
    TIFF= SizeByes//(res * 6)

    # Results display
    print('Your Flash Drive can store: ')
    # Image in GIF format
    print(format(GIF), 'Images in GIF format can be stored. ')
    # Image in JPEG format
    print(format(JPEG), 'Images in JPEG format can be stored. ')
    # Image in PNG format
    print(format(PNG), 'Images in PNG format can be stored. ')
    # Image in TIFF format
    print(format(TIFF), 'Images in TIFF format can be stored. ')
    print()
    
    # continue?
    response= input('Would you like to enter another USB size? (y/n): ')
    responce = responce.lower();
    print()
    
    while response !='y' and response !='n':
        response= input("Please enter 'y' or 'n': ")
        response = response.lower();
    print()
    
    if response == 'n':
        stop= True
