import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('loop widgets')

## label 

labels = ['What is your name: ','What is your age : ','What is your gender: ','Country: ','State: ','City : ']

for i in range(len(labels)):
    cur_label = 'label' + str(i)
    cur_lebel = ttk.Label(win,text=labels[i])
    cur_lebel.grid(row=i,column=0,sticky=tk.W)


##### Entry box

user_info ={
    'name' : tk.StringVar(),
    'age' : tk.StringVar(),
    'gender' : tk.StringVar(),
    'country' : tk.StringVar(),
    'state' : tk.StringVar(),
    'city' : tk.StringVar()
}
counter = 0
for i in user_info:
    cur_entrybox = 'entry' + i
    cur_entrybox = ttk.Entry(win,width=16,textvariable = user_info[i])
    cur_entrybox.grid(column= 1,row=counter)
    cur_entrybox.focus()
    counter +=1


def submit():
    print(user_info.get('name').get())
    print(user_info.get('age').get())
    print(user_info.get('gender').get())
    print(user_info.get('country').get())
    print(user_info.get('state').get())
    print(user_info.get('city').get())


submit_btn = ttk.Button(win,text='Submit',command = submit)
submit_btn.grid(row=7,column = 1) 

win.mainloop()