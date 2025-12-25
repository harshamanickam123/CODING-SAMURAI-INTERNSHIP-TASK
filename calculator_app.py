import tkinter as tk
root=tk.Tk()
root.title("MYCALCULATOR")
root.geometry("300x400")
root.resizable(False,False)
display=tk.Entry(root,font=("Arial",20),borderwidth=5,relief="ridge",justify="right")
display.grid(row=0,column=0,columnspan=4,padx=10,pady=15,sticky="nsew")
def click_button(value):
    display.insert('end',value)
def clear_display():
    display.delete(0,'end')
def calculate():
    try: 
        exp=display.get()
        result=eval(exp)
        display.delete(0,'end')
        display.insert('end',result)
    except Exception as e:
        display.delete(0,'end')
        display.insert('end',"Error")
buttons=[('7',1,0),('8',1,1),('9',1,2),('/',1,3),
         ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
         ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
         ('0',4,0),('.',4,1),('+',4,2),('=',4,3),
         ]
for text, row, col in buttons:
    if text== '=':
        button =tk.Button(root,text=text,font=("Arial",14),command=calculate,bg="#4CAF50",fg="white")
    else:
        button=tk.Button(root,text=text,font=("Arial",14),command=lambda t=text: click_button(t))
    button.grid(row=row,column=col,sticky="nsew",padx=5,pady=5)
clear_button=tk.Button(root,text='C',font=("Arial",14),command=clear_display,bg="#f44336",fg="white")
clear_button.grid(row=5,column=0,columnspan=4,sticky="nsew",padx=10,pady=10)
for i in range(6):
    root.rowconfigure(i,weight=1)
for i in range(4):
    root.columnconfigure(i,weight=1)
root.mainloop()
