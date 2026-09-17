import random

#aBI stands for arbitrary Binary Integer
def aBI():
    return random.randint(0,1)

#mSR stands for make Symetrical Row, returns row
def mSR(x):
    #napravi row listu
    row = []

    #provjeri jeli parni broj
    parni = False
    if x % 2 == 0:
        parni = True
    
    if parni:
        for i in range(x//2):
            row.append(aBI())
        for i in range(x//2-1, -1, -1):
            row.append(row[i])
    else:
        for i in range(x//2+1):
            row.append(aBI())
        for i in range(x//2-1, -1, -1):
            row.append(row[i])
    return row
    #boze pomozi

def makeMatrix(x, y):
    matrix = []
    for i in range(y):
        matrix.append(mSR(x))
    return matrix

def printMatrix(matrix):
    #loops through the rows of the matrix
    for row in matrix:
        print(row)

x, y = int(input("x value?: ")), int(input("y value?: "))
wheight = y * 50
wwidth = x * 50



from PIL import Image, ImageDraw
image = Image.new("RGB", (wwidth, wheight), "white")
draw = ImageDraw.Draw(image)

def drawBox(x, y):
    x2 = x + 50
    y2 = y + 50
    draw.rectangle((x, y, x2, y2), fill="black")

def drawPic(matrix):
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value == 1:
                drawBox(x*50, y*50)

drawPic(makeMatrix(x, y))
image.save("my_pfp.png")

print("Success! Check your folder!")