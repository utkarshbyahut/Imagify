from PIL import Image

def compress_image(input_path, output_path, output_quality):
    
    '''
   
    Goal : Compresses an image and saves it to the output path.

    Args :
        input_path: The path to the input image.
        output_path: The path to save the compressed image.
        quality: The compression quality (0-100).
   
    '''
    
    print("\n", "IP:", input_path, "OP:", output_path, "OQ:", output_quality, "\n")
    
    img = Image.open(input_path)
    img.save(output_path, optimize = True, quality = int(output_quality))

