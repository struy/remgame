import os
from tkinter import *
from random import shuffle

SIDE = 8  # size of square
QSIDE = SIDE**2//2  # count of uniq images
prev = None
count = 0

def cmd():
    pass


def counter(fn):
    def _counted(*largs, **kargs):
        _counted.invocations += 1
        fn(*largs, **kargs)

    _counted.invocations = 0
    return _counted


def hide_all(buttons):
    """ Hide all buttons"""
    for btn in buttons:
        btn.configure(image=faq)


def hide_both(prev, btn):
    prev.configure(image=faq)
    btn.configure(image=faq)


@counter
def change(btn):
    global prev
    btn.configure(image=btn.img)
    if prev is None:
        prev = btn
    else:
        if prev.x != btn.x or prev is btn:
            main_window.after(1000, hide_both, prev, btn)
        prev = None
    # print(change.invocations)



main_window = Tk()
main_window.title('Remgame')

faq = PhotoImage(file='FAQ.gif')

files = [os.path.join('gif', f) for f in os.listdir('gif')]
shuffle(files)
files = files[0:QSIDE]*2
shuffle(files)

images = [PhotoImage(file=f) for f in files]
buttons = []


for i in range(SIDE):
    for j in range(SIDE):
        btn = Button(main_window, image=images[i * SIDE + j], relief=FLAT)
        btn.configure(command=lambda b=btn: change(b))
        btn.x = files[i*SIDE+j]
        btn.img = images[i * SIDE + j]
        btn.grid(row=i, column=j)
        buttons.append(btn)




main_window.after(3000, hide_all, buttons)
main_window.mainloop()

