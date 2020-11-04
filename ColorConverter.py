# -*- coding: utf-8 -*-
"""
colorConverter.py
Author: SMFSW
Copyright (c) 2016-2018 SMFSW

The MIT License (MIT)
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

from Tkinter import *
from tkColorChooser import askcolor


winColorConv = Tk()
winColorConv.title("Color Converter (by SMFSW)")

converterWin = Canvas(winColorConv, width=320, height=400, background="black")
converterWin.grid(row=0, column=1)

r_slide_val = IntVar()  # variables used by slider controls
g_slide_val = IntVar()
b_slide_val = IntVar()

fnt = 'SansSerif 12 bold'

combined_hex = '000000'
red_hex = '00'
green_hex = '00'
blue_hex = '00'

red_int = 0
green_int = 0
blue_int = 0

red_text = 0
green_text = 0
blue_text = 0

# red display
converterWin.create_rectangle(20, 30, 80, 110)
converterWin.create_text(20, 10, text="Red", width=60, font=fnt, anchor=NW, fill='red')

# green display
converterWin.create_rectangle(100, 30, 160, 110)
converterWin.create_text(100, 10, text="Green", width=60, font=fnt, anchor=NW, fill='green')

# blue display
converterWin.create_rectangle(180, 30, 240, 110)
converterWin.create_text(180, 10, text="Blue", width=60, font=fnt, anchor=NW, fill='blue')

# Labels
converterWin.create_text(250, 30, text="integer 256", width=60, anchor=NW)
converterWin.create_text(250, 60, text="% of 256", width=60, anchor=NW)
converterWin.create_text(250, 86, text="hex", width=60, anchor=NW)

# combined display
fnt = 'SansSerif 10 bold'
converterWin.create_rectangle(20, 170, 220, 220)
converterWin.create_text(20, 130, text="Combined colors", width=200, font=fnt, anchor=NW, fill='white')
converterWin.create_text(20, 150, text="Hexadecimal red-green-blue", width=300, font=fnt, anchor=NW, fill='white')


# callback functions to service slider changes
def code_shrtn(slide_value, x0, y0, width, height, col):
    """ This allows the callback functions to be reduced in length. """
    global combined_hex, red_int, green_int, blue_int, fnt

    fnt = 'SansSerif 10 bold'
    slide_txt = str(slide_value)
    slide_int = int(slide_value)
    slide_hex = hex(slide_int)

    slide_percent = slide_int * 100 / 256

    converterWin.create_rectangle(x0, y0, x0 + width, y0 + height, fill='black')

    converterWin.create_text(x0 + 6, y0 + 6, text=slide_txt, width=width, font=fnt, anchor=NW, fill=col)
    converterWin.create_text(x0 + 6, y0 + 28, text=slide_percent, width=width, font=fnt, anchor=NW, fill=col)
    converterWin.create_text(x0 + 6, y0 + 50, text=slide_hex, width=width, font=fnt, anchor=NW, fill=col)

    return slide_int


def callback_red(*args):
    """ red slider event handler """
    global red_int
    col = "red"
    str_val = str(r_slide_val.get())
    red_int = code_shrtn(str_val, 20, 30, 60, 80, col)
    update_display(red_int, green_int, blue_int)


def callback_green(*args):
    """ green slider event handler """
    global green_int
    col = "darkgreen"
    str_val = str(g_slide_val.get())
    green_int = code_shrtn(str_val, 100, 30, 60, 80, col)
    update_display(red_int, green_int, blue_int)


def callback_blue(*args):
    """ blue slider event handler """
    global blue_int
    col = "blue"
    str_val = str(b_slide_val.get())
    blue_int = code_shrtn(str_val, 180, 30, 60, 80, col)
    update_display(red_int, green_int, blue_int)


def update_display(red_int, green_int, blue_int):
    """ Refresh the swatch and numerical display. """
    combined_int = (red_int, green_int, blue_int)
    combined_hx = '#%02x%02x%02x' % combined_int

    converterWin.create_rectangle(20, 170, 220, 220, fill='black')
    converterWin.create_text(26, 170, text=combined_hx, width=200, anchor=NW,
                             fill='white', font='SansSerif 14 bold')
    converterWin.create_rectangle(1, 400, 320, 230, fill=combined_hx)


r_slide_val.trace_variable("w", callback_red)
g_slide_val.trace_variable("w", callback_green)
b_slide_val.trace_variable("w", callback_blue)

# red slider specification parameters.
r_slider = Scale(winColorConv, length=400, fg='red', activebackground="tomato",
                 background="gray", troughcolor="red", label="RED", from_=255, to=0,
                 resolution=1, variable=r_slide_val, orient='vertical')

r_slider.grid(row=0, column=2)

# green slider specification
g_slider = Scale(winColorConv, length=400, fg='dark green', activebackground="green yellow",
                 background="gray", troughcolor="green", label="GREEN", from_=255, to=0,
                 resolution=1, variable=g_slide_val, orient='vertical')

g_slider.grid(row=0, column=3)

# blue slider specification
b_slider = Scale(winColorConv, length=400, fg='blue', activebackground="turquoise",
                 background="gray", troughcolor="blue", label="BLUE", from_=255, to=0,
                 resolution=1, variable=b_slide_val, orient='vertical')

b_slider.grid(row=0, column=4)


color = askcolor()
print("askcolor ret: {}".format(color))

if isinstance(color[1], str):
    r_slide_val.set(color[0][0])
    g_slide_val.set(color[0][1])
    b_slide_val.set(color[0][2])
else:
    r_slide_val.set(0)
    g_slide_val.set(0)
    b_slide_val.set(0)

winColorConv.mainloop()
