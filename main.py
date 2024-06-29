from PIL import Image, ImagePalette, ImageOps

ascii_chars = list("$B%&W#*oakbdpqmZOQLCUXcvnxjf/|)1}[]-_~<>!lI;:,^`'. ")
index = 0

print('If you get an error in image location use absolute path. Otherwise use ./[...] path')

# open image
# i = Image.open("/home/m/cs/python/img2ascii/3.png") #fixed path
i = Image.open(input("Image location: "))
# ask for image size
size = input("ASCII art max width/height size (in characters): ")
size = int(size)
size_tuple = (size, size)
# resize image
width, height = i.size
width = width*2
if int(width) > int(height):
    height = int(size / (width / height))
    width = size
else:
    width = int(size / (height / width))
    height = size
i = i.resize((width,height))

# convert rgb to grayscale
i = i.convert("L")

# getting all the pixels
tuple_list = list(i.getdata())

# write to the output file
o = open('output.txt', 'w')

while index < len(tuple_list): 
    if index % width == 0 and index != 0:
        o.write('\n')          
    o.write(ascii_chars[int((tuple_list[index])/5)-1])
    index += 1

# close output file
o.write('\n')
o.close()

# print file output
o = open('output.txt', 'r')
print(o.read())
o.close()