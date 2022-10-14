import math
from tkinter import *

calc = Tk()
calc["bg"] = "gray25"

# bellow the group for taking arguments from Tk.window input lines

def type_of_x():
    try:
        x = float(first_operand.get())  # gets a parameters from window input line
    except ValueError:                  # processing input of other signs than numbers
        result["text"] = "Вводите только число в первое значение, попробуйте еще"
        return result
    return x


def type_of_y():
    try:
        y = float(second_operand.get())
    except ValueError:
        result["text"] = "Вводите только число во второе значение, попробуйте еще"
        return result
    return y

# bellow a group for operating math functions

def plus():
    try:
        result["text"] = f"{str(type_of_x() + type_of_y())}"
    except TypeError:   # processing core Error for taking other-than-number argument too early
        pass

def difference():
    try:
        result["text"] = f"{str(type_of_x() - type_of_y())}"
    except TypeError:
        pass

def multyplying():
    try:
        result["text"] = f"{str(type_of_x() * type_of_y())}"
    except TypeError:
        pass

def divide():
    try:
        if type_of_y() == 0:
            result["text"] = "На ноль делить нельзя"
        else:
            result["text"] = f"{str(type_of_x() / type_of_y())}"
    except TypeError:
        pass

def grading():
    try:
        result["text"] = f"{str(type_of_x() ** type_of_y())}"
    except TypeError:
        pass

def sqrt_():
    try:
        result["text"] = f"Корень первого числа: {str(type_of_x() ** 0.5)}"
    except TypeError:
        pass

def cub_sqrt_():
    try:
        result["text"] = f"Кубический корень первого числа: {str(type_of_x() ** (1./3.))}"
    except TypeError:
        pass

def sin_():
    try:
        result["text"] = f"Синус первого числа: {str(math.sin(type_of_x()))}"
    except TypeError:
        pass

def cos_():
    try:
        result["text"] = f"Косинус первого числа: {str(math.cos(type_of_x()))}"
    except TypeError:
        pass

def tan_():
    try:
        result["text"] = f"Тангенс первого числа: {str(math.tan(type_of_x()))}"
    except TypeError:
        pass

# bellow window parameters

calc.title("Инжинерный калькулятор made by Gennadii Patenko")
calc.geometry("900x750")
calc.resizable(width=False, height=False)

title_ = Label(text="Введите числа и выберите операцию", width=35, height=5, bg="lightgreen", font=("TimesNewRoman 15"))
title_.pack()

f_top = LabelFrame(calc, text="Введите первое значение", font="TimesNewRoman 12", bg='#6699cc', bd=5)
f_top.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.1)
f_middle = LabelFrame(calc, text="Выберите операцию", font="TimesNewRoman 12", bg='light goldenrod', bd=10)
f_middle.place(relx=0.35, rely=0.35, relwidth=0.32, relheight=0.2)
f_between = LabelFrame(calc, text="Введите второе значение, если требуется", font="TimesNewRoman 12", bg='#6699cc', bd=5)
f_between.place(relx=0.2, rely=0.6, relwidth=0.6, relheight=0.1)
f_bottom = Frame(calc, bg="medium violet red")
f_bottom.place(relx=0.15, rely=0.75, relwidth=0.7, relheight=0.2)

result = Label(f_bottom, text="ОТВЕТ", font="TimesNewRoman 15", bg="yellow", width=70)
result.pack(expand=1)

first_operand = Entry(f_top, bg="snow3", font=20)
first_operand.pack()
second_operand = Entry(f_between, bg="snow3", font=20)
second_operand.pack()

# Bellow operators for the window, operators connected to operating math functions above

sqrt_button = Button(f_middle, text="√", font="TimesNewRoman 23", width=1, height=1, command=sqrt_).pack(side=LEFT)
с_sqrtbutton = Button(f_middle, text="∛", font="TimesNewRoman 23", width=1, height=1, command=cub_sqrt_).pack(side=LEFT)
sin_button = Button(f_middle, text="sin", font="TimesNewRoman 10", width=3, height=3, command=sin_).pack(side=LEFT)
cos_button = Button(f_middle, text="cos", font="TimesNewRoman 10", width=3, height=3, command=cos_).pack(side=LEFT)
tan_button = Button(f_middle, text="tan", font="TimesNewRoman 10", width=3, height=3, command=tan_).pack(side=LEFT)
pl_button = Button(f_middle, text="+", font="TimesNewRoman 23", width=1, height=1, command=plus).pack(side=LEFT)
min_button = Button(f_middle, text="-", font="TimesNewRoman 23", width=1, height=1, command=difference).pack(side=LEFT)
mult_button = Button(f_middle, text="×", font="TimesNewRoman 23", width=1, height=1, command=multyplying).pack(side=LEFT)
div_button = Button(f_middle, text="/", font="TimesNewRoman 23", width=1, height=1, command=divide).pack(side=LEFT)
gr_button = Button(f_middle, text="^", font="TimesNewRoman 23", width=1, height=1, command=grading).pack(side=LEFT)


calc.mainloop()   # Grafic interface starts the program
