"""
Turtle graphics based code-39 barcode generator.
The code-39 supports upto 39 ASCII charatcers
and is the de facto barcode standard used
by the United Stated Department of Defense.
"""

import argparse
import turtle
try:
    from encoding_table import encoding_table
except ImportError:
    print("'encoding_table.py' file missing")

def init_screen(bg_color="white", title_="Barcode Generator"):
    """
    initialise the screen
    """
    screen = turtle.Screen()
    screen.bgcolor(bg_color)
    screen.title(title_)

def line(thickness, tcolor, length=20, factor=0.9, renderer=None):
    """
    Draw a line onto the screen.
    thickness is controlled by the factor.
    """
    renderer.pencolor(tcolor)
    for _ in range(int(thickness/factor)):
        renderer.pensize(1)
        renderer.pendown()
        renderer.forward(length)
        renderer.penup()
        renderer.setx(renderer.xcor()+1)
        renderer.right(180)

def encoder39(datastring, length, factor):
    """
    Encode the given data string into a barcode.
    """
    renderer = turtle.Turtle()
    renderer.penup()
    renderer.hideturtle()
    renderer.speed(0)
    renderer.left(90)
    data = '*'+datastring.upper()+'*'
    encoded_data = []
    for character in data:
        for encoding in encoding_table[character]:
            if encoding == 'W':
                encoded_data.append(2)
            elif encoding == 'N':
                encoded_data.append(1)
        encoded_data.append(1)
    colors = ["white" if i % 2 != 0 else "black" for i in range(len(encoded_data))]
    renderer.setx(renderer.xcor()-len(encoded_data))
    for bit in zip(encoded_data, colors):
        line(bit[0], bit[1], renderer=renderer, length=length, factor=factor)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data",   type=str,   dest="dstring", required=True)
    parser.add_argument("-l", "--length", type=int,   dest="bar_length", default=50)
    parser.add_argument("-f", "--factor", type=float, dest="t_factor",   default=0.9)
    args = parser.parse_args()
    assert args.t_factor > 0 and args.t_factor < 1
    init_screen()
    encoder39(args.dstring, args.bar_length, args.t_factor)
    input("Done! Hit RETURN to exit")
