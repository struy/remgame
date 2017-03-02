import os
from tkinter import  *


print(os.listdir('gif'))
flles = [os.path.join('gif', f) for f in os.listdir('gif')]

main_window = Tk()
main_window.title('Remgame')
for i in range(10):
    for j in range(10):
        btn = Button(main_window, text='?', font=('Courier New', 14, 'normal'), relief=FLAT)
        btn.grid(row=i, column=j)

main_window.mainloop()

