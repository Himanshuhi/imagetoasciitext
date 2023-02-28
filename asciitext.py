from PIL import Image

#In this you to give your photo name
image = Image.open('himanshu.jpg')

new_size = (80, 80)
image = image.resize(new_size)

image = image.convert('L')

chars = [' ', '.', ':', '*', 'o', '&', '8', '#', '@']

dot_text = ''
for y in range(new_size[1]):
    for x in range(new_size[0]):
        pixel = image.getpixel((x, y))

        char_index = int((pixel/255) * (len(chars)-1))

        dot_text += chars[char_index]

    dot_text += '\n'

print(dot_text)

with open('output.txt', 'w') as f:
    f.write(dot_text)

