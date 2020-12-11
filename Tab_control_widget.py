##### Notebook ----> contain two pages
## page 1                    ### page 2
### widgets                   ### widgets


import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('Tab Control')
nb = ttk.Notebook(win)  

page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)

nb.add(page1,text='One')
nb.add(page2,text='Two')
nb.pack(expand=True,fill='both')

##page 1
label1= ttk.Label(page1,text='This is page 1:')
label1.grid(row=0,column=0)

entry1= ttk.Entry(page1,width=26)
entry1.grid(row=0,column=1)

##page 2
label2= ttk.Label(page2,text='This is page 2:')
label2.grid(row=0,column=0)

entry2= ttk.Entry(page2,width=26)
entry2.grid(row=0,column=1)



win.mainloop()