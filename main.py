import os
from tkinter import *
from random import shuffle

SIDE = 8  # size of square
QSIDE = SIDE**2//2  # count of uniq images


def cmd():
    print('Yes')
    print('....')

main_window = Tk()
main_window.title('Remgame')

faq = PhotoImage(file='FAQ.gif')

files = [os.path.join('gif', f) for f in os.listdir('gif')]
shuffle(files)
files = files[0:QSIDE]*2
shuffle(files)

images = [PhotoImage(file=f) for f in files]

for i in range(SIDE):
    for j in range(SIDE):
        btn = Button(main_window, image=images[i * SIDE + j], relief=FLAT, command=cmd)
        btn.grid(row=i, column=j)

main_window.mainloop()

