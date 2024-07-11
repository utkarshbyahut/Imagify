from PIL import Image

def compress_image():
    
    '''
   
    Goal : Compresses an image and saves it to the output path.

    Args :
        input_path: The path to the input image.
        output_path: The path to save the compressed image.
        quality: The compression quality (0-100).
   
    '''
    inputPath      =    input("Enter Local Path to the Input Image        : ")
    outputPath     =    input("Enter Output Path for the Image            : ")
    outputQuality  =    input("Enter Desired Quality of the Image (0-100) : ")

    print("\n", "IP:", inputPath, "OP:", outputPath, "OQ:", outputQuality, "\n")
        
    img = Image.open(inputPath)
    img.save(outputPath, optimize = True, quality = int(outputQuality))

def exitFunction():
    print("\n", "See you soon! Bye Bye!", "\n")

