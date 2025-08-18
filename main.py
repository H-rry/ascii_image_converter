import PIL.Image

# ASCII_CHARS = ["@", "#", "S", "%", "?", "*","+",";",":",",","."]
ASCII_CHARS = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'.  ") # gradient
new_width = 60 # edit to change txt width

# resize image according to new width
def resize_image(image):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# converts each pixel to greyscale
def greyify(image):
    greyscale_image = image.convert("L")
    return(greyscale_image)
    
# convert pixels to a string of ASCII characters
def pizels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel * (len(ASCII_CHARS) -1) // 255] for pixel in pixels])
    return(characters)


def main():
    #attempt to open image from user-imput
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not a valid pathname to an image")
    
    #convert image to ascii
    new_image_data = pizels_to_ascii(greyify(resize_image(image)))

    #format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0,pixel_count, new_width))

    #print result
    print(ascii_image)
    with open(f"ascii_{path[:-4]}.txt", "w") as f:
        f.write(ascii_image)



main()