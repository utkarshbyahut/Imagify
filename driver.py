from PIL import Image
import functions

while True:
    print("\n", "| 1- Compress Image | 2- Quit | ", "\n")
    userChoice = int(input("What action would you like to perform? : "))
    
    if (userChoice ==   1):     
        inputPath      =    input("Enter Local Path to the Input Image        : ")
        outputPath     =    input("Enter Output Path for the Image            : ")
        outputQuality  =    input("Enter Desired Quality of the Image (0-100) : ")

        functions.compress_image(inputPath, outputPath, outputQuality)

    elif (userChoice == 2):
        print("\n", "See you soon! Bye Bye!", "\n")
        break

    else:
        print("Oh no! Invalid Input! Try Again :) \n")


