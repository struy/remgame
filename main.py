import os
from tkinter import *
from random import shuffle

# Home task:
# 1. Game for time or for steps



SIDE = 4  # size of square
QSIDE = SIDE**2//2  # count of uniq images
prev = None
open_count = 0



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
    global open_count
    btn.configure(image=btn.img)
    if prev is None:
        prev = btn
    else:
        if prev.x != btn.x or prev is btn:
            main_window.after(1000, hide_both, prev, btn)
        else:
            open_count += 1
        prev = None

    Label(main_window, text="step: " + str(change.invocations)).grid(row=0)
    Label(main_window, text='open: ' + str(open_count)).grid(row=0, column=1)
    Label(main_window, text='from' + str(QSIDE)).grid(row=0, column=2)
    if QSIDE is open_count:
        toplevel = Toplevel()
        label1 = Label(toplevel, text="You are win!", height=0, width=50)
        label1.pack()

main_window = Tk()
main_window.title('Remgame')

faq = PhotoImage(file='FAQ.gif')
files = [os.path.join('gif', f) for f in os.listdir('gif')]
shuffle(files)
files = files[0:QSIDE]*2
shuffle(files)

images = [PhotoImage(file=f) for f in files]
buttons = []
windows_label = Label(main_window, text="step: 0", borderwidth=1).grid(row=0)
Label(main_window, text='open: 0').grid(row=0, column=1)
Label(main_window, text='from ' + str(QSIDE)).grid(row=0, column=2)



for i in range(SIDE):
    for j in range(SIDE):
        btn = Button(main_window, image=images[i * SIDE + j], relief=FLAT)
        btn.configure(command=lambda b=btn: change(b))
        btn.x = files[i*SIDE+j]
        btn.img = images[i * SIDE + j]
        btn.grid(row=i+1, column=j)
        buttons.append(btn)

main_window.after(3000, hide_all, buttons)
main_window.mainloop()

