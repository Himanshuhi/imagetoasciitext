from PIL import Image

# Open the image file
image = Image.open('maruthi.jpg')

# Resize the image to a smaller size for faster processing
new_size = (80, 80)
image = image.resize(new_size)

# Convert the image to grayscale
image = image.convert('L')

# Define the list of characters to use for the dot text
chars = [' ', '.', ':', '*', 'o', '&', '8', '#', '@']

# Loop through each pixel in the image and replace it with a corresponding character
dot_text = ''
for y in range(new_size[1]):
    for x in range(new_size[0]):
        # Get the pixel value at the current position
        pixel = image.getpixel((x, y))

        # Determine the index of the corresponding character based on the pixel value
        char_index = int((pixel/255) * (len(chars)-1))

        # Add the corresponding character to the dot text string
        dot_text += chars[char_index]

    # Add a line break after each row of characters
    dot_text += '\n'

# Print the dot text to the console
print(dot_text)

# Save the dot text to a text file
with open('output.txt', 'w') as f:
    f.write(dot_text)

