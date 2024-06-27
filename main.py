from PIL import Image, ImagePalette

size = 128

o = open('output.txt', 'w')
o.write('testing/texting')
o.write('\n')
o.close()

# open image
i = Image.open("/home/m/cs/python/img2ascii/input.jpg")
# resize image
width, height = i.size
if int(width) > int(height):
    height = int(size / (width / height))
    width = size
else:
    width = int(size / (height / width))
    height = size
i = i.resize((width,height))
# convert rgb to grayscale
i = i.convert("L")

# i.show()

p = list(i.getdata())

# for each in p :

print(len('$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`.')+1)







