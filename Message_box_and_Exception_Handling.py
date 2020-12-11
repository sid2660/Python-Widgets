import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box 
win = tk.Tk()

## *********** Label frame ********************
label_frame = ttk.Labelframe(win,text='Contact Detail')
label_frame.grid(row=0,column=0,padx=40,pady=10)

## ************************** Labels ***************
name_label = ttk.Label(label_frame,text='Enter your name please : ',font=('Helvetica',12,'bold'))
age_label = ttk.Label(label_frame,text='Enter your age please : ',font=('Helvetica',12,'bold'))


### ************************ Entry box  variables *********************
name_var = tk.StringVar()
age_var = tk.StringVar()

#### *********************** Entry Boxes ********************

name_entry = ttk.Entry(label_frame,width=36,textvariable=name_var)
age_entry = ttk.Entry(label_frame,width=36,textvariable=age_var)


####********************* Grid ************
name_label.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
age_label.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)
name_entry.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
age_entry.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)

####****************** Submit button ******
def submit():
    # m_box.showinfo('title','Contant of this message box !!!!')
    name = name_var.get()
    age = age_var.get()
    if name == '' or age == '':
        m_box.showerror('Error','Please fill both name and age !!')
    else:
        try:
            ##age = 'abc' # vaue error
            ## age = '20'
            age = int(age)
        except ValueError:
            m_box.showerror('ValueError','Only numbers are allowed in age box !!!!')
        else:
            if age <= 17:
                m_box.showwarning('Under age','You are less than 18, visit this page on your risk!!')
            print(f'{name} : {age}')    
            





submit_btn = ttk.Button(win,text='Submit',command=submit)
submit_btn.grid(row=1,columnspan=2,padx=40)
win.mainloop()