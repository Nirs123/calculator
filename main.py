import tkinter as tk

win = tk.Tk()
win.title("Calculator")
win.geometry('200x390')
win.minsize(200,390)
win.maxsize(200,390)

#Calculator
def op_add(a,b):
    return a+b
def op_div(a,b):
    if b != 0:
        return a/b
    else:
        return None
def op_mult(a,b):
    return a*b
def op_minus(a,b):
    return a-b

#Tkinter
frame_1 = tk.Frame(win)
memory_n = ""
a=""
ope = None
def add_number(n):
    global a
    a = a + str(n)
    change_display(a)

def add_point():
    global a
    if "." not in a:
        a = a + "."
        change_display(a)
    else:
        return None

def delete():
    global memory_n,ope,a
    memory_n = ""
    ope = None
    a = ""
    change_display(0)

def supp():
    global a
    if a != "":
        a = a[:-1]
        change_display(a)
    else:
        return None

def result():
    global ope,memory_n,a
    if memory_n != "" and a != "" and ope != None:
        if ope == "/":
            re = op_div(float(memory_n),float(a))
        elif ope == "*":
            re = op_mult(float(memory_n),float(a))
        elif ope == "+":
            re = op_add(float(memory_n),float(a))
        elif ope == "-":
            re = op_minus(float(memory_n),float(a))
        a = ""
        ope = None
        if re != None:
            memory_n = re
            if re.is_integer():
                change_display(int(re))
            else:
                change_display(round(re,2))
        else:
            memory_n = ""
            change_display("Error")

def div():
    global ope
    ope = "/"
    store()

def mult():
    global ope
    ope = "*"
    store()

def plus():
    global ope,memory_n
    ope = "+"
    store()

def minus():
    global ope
    ope = "-"
    store()

def store():
    global memory_n,a
    if memory_n == "":
        memory_n = a
    a = ""
    change_display(a)

n_displayed = tk.Label(frame_1,text=str("0"),font=('Segoe UI Black',"30"))
n_displayed.grid(row=0,column=0,rowspan=1,columnspan=4)
def change_display(n):
    global n_displayed
    n_displayed.grid_forget()
    if n == "":
        n_displayed = tk.Label(frame_1,text=str("0"),font=('Segoe UI Black',"30"))
    else:
        n_displayed = tk.Label(frame_1,text=str(n),font=('Segoe UI Black',"30"))
    n_displayed.grid(row=0,column=0,rowspan=1,columnspan=4)

b_0 = tk.Button(frame_1,text="0",font=('Segoe UI Black',"20"),command = lambda n=0:add_number(n),height=1,width=5)
b_1 = tk.Button(frame_1,text="1",font=('Segoe UI Black',"20"),command = lambda n=1:add_number(n),width=2,height=1)
b_2 = tk.Button(frame_1,text="2",font=('Segoe UI Black',"20"),command = lambda n=2:add_number(n),width=2,height=1)
b_3 = tk.Button(frame_1,text="3",font=('Segoe UI Black',"20"),command = lambda n=3:add_number(n),width=2,height=1)
b_4 = tk.Button(frame_1,text="4",font=('Segoe UI Black',"20"),command = lambda n=4:add_number(n),width=2,height=1)
b_5 = tk.Button(frame_1,text="5",font=('Segoe UI Black',"20"),command = lambda n=5:add_number(n),width=2,height=1)
b_6 = tk.Button(frame_1,text="6",font=('Segoe UI Black',"20"),command = lambda n=6:add_number(n),width=2,height=1)
b_7 = tk.Button(frame_1,text="7",font=('Segoe UI Black',"20"),command = lambda n=7:add_number(n),width=2,height=1)
b_8 = tk.Button(frame_1,text="8",font=('Segoe UI Black',"20"),command = lambda n=8:add_number(n),width=2,height=1)
b_9 = tk.Button(frame_1,text="9",font=('Segoe UI Black',"20"),command = lambda n=9:add_number(n),width=2,height=1)
b_p = tk.Button(frame_1,text=",",font=('Segoe UI Black',"20"),command = add_point,width=2,height=1)
b_c = tk.Button(frame_1,text="C",font=('Segoe UI Black',"20"),command = delete,width=5,height=1)
b_de = tk.Button(frame_1,text="#",font=('Segoe UI Black',"20"),command = supp,width=2,height=1)
b_div = tk.Button(frame_1,text="/",font=('Segoe UI Black',"20"),command = div,width=2,height=1)
b_plus = tk.Button(frame_1,text="+",font=('Segoe UI Black',"20"),command = plus,width=2,height=1)
b_minus = tk.Button(frame_1,text="-",font=('Segoe UI Black',"20"),command = minus,width=2,height=1)
b_mult = tk.Button(frame_1,text="*",font=('Segoe UI Black',"20"),command = mult,width=2,height=1)
b_re = tk.Button(frame_1,text="=",font=('Segoe UI Black',"20"),command = result,width=2,height=1)

b_0.grid(row=5, column=0,rowspan=1,columnspan=2)
b_1.grid(row=4, column=0,rowspan=1,columnspan=1)
b_2.grid(row=4, column=1,rowspan=1,columnspan=1)
b_3.grid(row=4, column=2,rowspan=1,columnspan=1)
b_4.grid(row=3, column=0,rowspan=1,columnspan=1)
b_5.grid(row=3, column=1,rowspan=1,columnspan=1)
b_6.grid(row=3, column=2,rowspan=1,columnspan=1)
b_7.grid(row=2, column=0,rowspan=1,columnspan=1)
b_8.grid(row=2, column=1,rowspan=1,columnspan=1)
b_9.grid(row=2, column=2,rowspan=1,columnspan=1)
b_p.grid(row=5, column=2,rowspan=1,columnspan=1)

b_c.grid(row=1, column=0,rowspan=1,columnspan=2)
b_de.grid(row=1, column=2,rowspan=1,columnspan=1)
b_div.grid(row=1, column=3,rowspan=1,columnspan=1)
b_plus.grid(row=4, column=3,rowspan=1,columnspan=1)
b_minus.grid(row=3, column=3,rowspan=1,columnspan=1)
b_mult.grid(row=2, column=3,rowspan=1,columnspan=1)
b_re.grid(row=5, column=3,rowspan=1,columnspan=1)

frame_1.pack()

win.mainloop()