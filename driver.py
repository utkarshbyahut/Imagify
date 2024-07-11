from PIL import Image
import functions

while True:
    print("\n", "| 1- Compress Image | 2- Quit | 3- Get Colours | ", "\n")
    userChoice = int(input("What action would you like to perform? : "))
    
    if (userChoice ==   1):     
        functions.compress_image()

    elif (userChoice == 2):
        functions.exitFunction()
        break

#    elif (userChoice == 3):
#        functions.getpalette()

    else:
        print("Oh no! Invalid Input! Try Again :) \n")


