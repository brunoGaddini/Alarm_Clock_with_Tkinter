# Import Libraries
import tkinter
import PIL

from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk

# Color Pallete

cr0 = "#f0f3f5"  # Black
cr1 = "#feffff"  # White
cr2 = "#d6872d"  # Gold
cr3 = "#fc766d"  # Red
cr4 = "#403d3d"  # Letter Color
cr5 = "#4a88e8"  # Blue

# Creating the Window

window = Tk()
window.title("")
window.geometry('350x150')
window.configure(background=cr1)
window.resizable(width=False, height=False)

# window.mainloop()

# Splitting the window into two frames

frame_logo = Frame(window, width=400, height=10, background=cr2)
frame_logo.grid(row=0, column=0, pady=1, padx=0)

frame_body = Frame(window, width=400, height=290, background=cr1)
frame_body.grid(row=1, column=0, pady=1, padx=0)

# Configuring the logo frame

l_line = Label(frame_logo, height=1, background=cr2, anchor=NW, font=('Ivy 1'))
l_line.place(x=0, y=0)

# Configuring the body frame

l_line = Label(frame_logo, height=1, background=cr2, anchor=NW, font=('Ivy 1'))
l_line.place(x=0, y=0)

# Configuring the image frame

imagem = Image.open(r'C:\Users\Bruno\Desktop\Python\Depertador\icon1.png')
imagem = imagem.resize((100, 100))
imagem = ImageTk.PhotoImage(imagem)

l_imagem = Label(frame_body, height=100, image=imagem, compound=LEFT, padx=10, anchor=NW, font=('Ivy 16 bold'), background=cr1, fg=cr3)  # fg = letter color
l_imagem.place(x=10, y=10)

# Configuring the name frame

l_imagem = Label(frame_body, height=100, image=imagem, compound=LEFT, padx=10, anchor=NW, font=('Ivy 16 bold'), background=cr1, fg=cr3)
l_imagem.place(x=10, y=10)

# Configuring the text frame

l_text = Label(frame_body, text='Alarme', height=1, anchor=NE, font=('Ivy 10 bold'), background=cr1, fg=cr4)  # fg = text color
l_text.place(x=127, y=10)

# Creating the combobox

# Hours
l_hours = Label(frame_body, text='Hours', height=1, anchor=NW, font=('arial 7'), background=cr1, fg=cr4)  # fg = text color
l_hours.place(x=127, y=40)
c_hour = Combobox(frame_body, width=2, font=('Ivy 15'))
c_hour['value'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_hour.current(0) # setting index order
c_hour.place(x=130, y=58)

# Minutes
l_minutes = Label(frame_body, text='Minutes', height=1, anchor=NW, font=('arial 7'), background=cr1, fg=cr4)  # fg = text color
l_minutes.place(x=177, y=40)
c_minutes = Combobox(frame_body, width=2, font=('Ivy 15'))
c_minutes['value'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_minutes.current(0) # setting index order
c_minutes.place(x=130, y=58)

# Seconds
l_seconds = Label(frame_body, text='Seconds', height=1, anchor=NW, font=('arial 7'), background=cr1, fg=cr4)  # fg = text color
l_seconds.place(x=227, y=40)
c_seconds = Combobox(frame_body, width=2, font=('Ivy 15'))
c_seconds['value'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_seconds.current(0) # setting index order
c_seconds.place(x=130, y=58)

# Period
l_period = Label(frame_body, text='Period', height=1, anchor=NW, font=('arial 7'), background=cr1, fg=cr4)  # fg = text color
l_period.place(x=277, y=40)
c_period = Combobox(frame_body, width=2, font=('Ivy 15'))
c_period['value'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_period.current(0) # setting index order
c_period.place(x=130, y=58)

window.mainloop()
