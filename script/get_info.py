from PIL import Image
#filename = 'test.png'
print("Please enter the file path")
filename = input()
im = Image.open(filename)
#im.load()
print(im.info)
