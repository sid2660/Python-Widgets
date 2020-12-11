import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('Menubar totorial')


def func():
    print('func called')

## *********** menu class  **************************

##********************* Simple menubar*************************
# menubar = tk.Menu(win)
# menubar.add_command(label='Save',command=func)
# menubar.add_command(label='Save as',command=func)
# menubar.add_command(label='Copy',command=func)
# menubar.add_command(label='Paste',command=func)


### *********************** Drop Down menubar  **************

main_menu = tk.Menu(win)
file_menu = tk.Menu(main_menu,tearoff=0)
edit_menu = tk.Menu(main_menu,tearoff=0)
##*************** Menu in file_menu **********
file_menu.add_command(label='New File',command=func)
file_menu.add_command(label='New Window',command=func)
file_menu.add_separator() ### (use to create seprate by line )
file_menu.add_command(label='Open File',command=func)
file_menu.add_command(label='Open folder',command=func)
file_menu.add_separator()
file_menu.add_command(label='Save',command=func)
file_menu.add_command(label='Save As',command=func)
file_menu.add_command(label='Auto Save',command=func)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=func)

main_menu.add_cascade(label = 'File', menu=file_menu)


## ******************** Menu in Edit menu *************
edit_menu.add_command(label='Undo',command=func)
edit_menu.add_command(label='Redo',command=func)
edit_menu.add_separator()
edit_menu.add_command(label='Cut',command=func)
edit_menu.add_command(label='Copy',command=func)
edit_menu.add_command(label='Paste',command=func)
edit_menu.add_separator()
edit_menu.add_command(label='Find',command=func)
edit_menu.add_command(label='Replace',command=func)
edit_menu.add_separator()
edit_menu.add_command(label='Exit',command=func)


main_menu.add_cascade(label='Edit',menu=edit_menu)




win.config(menu=main_menu)


win.mainloop()