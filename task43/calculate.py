from tkinter import *
from tkinter import messagebox as mb

def summ():
    dataFirst = e1.get()
    if not dataFirst.isdigit():
        mb.showerror('Ошибка', 'Введите число в первое поле')
        return

    dataSecond = e2.get()
    if not dataSecond.isdigit():
        mb.showerror('Ошибка', 'Введите число во второе поле')
        return

    dataThird = e3.get()
    integerThird = int(dataThird) if dataThird else 0
    if integerThird == 0:
        mb.showerror('Ошибка', 'Введите число во второе поле')
        return


    integerFirst = int(dataFirst)
    integerSecond = int(dataSecond)
    summa = integerFirst + integerSecond + integerThird

    l2['text'] = f'{dataFirst} + {dataSecond} + {dataThird} = {summa}'
    ans = mb.askokcancel('Выход', 'Вы хотите попробовать снова?')
    if ans:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        l2['text']='Впишите числа снова'
    else:
        window.destroy()




def multiply():
    try:
        integerFirst = int(e1.get())
        integerSecond = int(e2.get())
        integerThird = int(e3.get())

        summa = integerFirst * integerSecond * integerThird

        l2['text'] = f'{integerFirst} * {integerSecond} * {integerThird} = {summa}'
        ans = mb.askokcancel('Выход', 'Вы хотите попробовать снова?')
        if ans:
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            l2['text']=''
        else:
            window.destroy()
    except ValueError:
        mb.showerror('Ошибка', 'Введите три числа')


window = Tk()
window.title("Калькулятор")

l=Label(text="Введите два целых числа в поля ввода и нажмине кнопку")
l.pack()

e1=Entry()
e1.pack()
e1.focus_set()

e2=Entry()
e2.pack()

e3=Entry()
e3.pack()

b=Button(text="Сложить",command=summ)
b.pack()


b2=Button(text="Умножить",command=multiply)
b2.pack()

l2 =Label()
l2.pack()


window.mainloop()