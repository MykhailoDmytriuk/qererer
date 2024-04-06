import tkinter as tk
my_w = tk.Tk()
my_w.geometry("410x200") 

def my_upd(v):
    color_c='#%02x%02x%02x' % (sc1.get(), sc2.get(), sc3.get())
    b1.config(bg=color_c)  # Updating background colour of button
    b1.config(text=color_c)# Updating text of the button   

font1=('Time',18,'normal')    

sc1 = tk.Scale(my_w, from_=0, to=255,bg='red', orient='horizontal',
    length=250,command=my_upd)
sc1.grid(row=0,column=0,padx=5,pady=10) 

sc2 = tk.Scale(my_w, from_=0, to=255,bg='green', orient='horizontal',
    length=250,command=my_upd)
sc2.grid(row=1,column=0,pady=10) 

sc3 = tk.Scale(my_w, from_=0, to=255,bg='blue', orient='horizontal',
    length=250,command=my_upd)
sc3.grid(row=2,column=0,pady=10) 

b1=tk.Button(my_w,text='My colour',font=font1,width=8)
b1.grid(row=1,column=1,padx=7)
my_w.mainloop()
