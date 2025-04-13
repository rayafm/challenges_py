# Debug Hex to RGB
# Doc2Doc should seamlessly convert hex triplet color codes to RGB values. 
# Hex colors are an efficient means of representing color with only 6 characters. 
# RGB values combine red, green and blue light to electronically display the entire color spectrum.

# Assignment
# Debug the hex_to_rgb function. 
# hex_to_rgb should take a hex triplet color code 
# and return three integers for the RGB values using int(). 
# One of the arguments used in int() is incorrect, 
# examine the documentation to see how to convert hexadecimal values.

# Use the provided is_hexadecimal function inside of hex_to_rgb to check if its input is valid. 
# If the input is not a six character long hexadecimal string, raise an exception "not a hex color string".

def hex_to_rgb(hex_color):
    # ?
    if is_hexadecimal(hex_color) and (len(hex_color) == 6):
        r = int(hex_color[:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:], 16)
        return r, g, b 
    else:
        raise Exception("not a hex color string")


# Don't edit below this line

def is_hexadecimal(hex_string):
    try:
        int(hex_string, 16)
        return True
    except:
        return False
