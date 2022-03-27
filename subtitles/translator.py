from tkinter import *
from googletrans import Translator


def translation():
    text = t.get('1.0', END)
    a = translator.translate(text, dest='en')
    t1.delete('1.0', END)
    t1.insert('1.0', a.text)

root = Tk()
root.geometry('500x350')
root.title('Переводчик')
root.resizable(width=False, height=False)
root['bg'] = 'black'
translator = Translator()


label = Label(root, fg='black', bg='white', font='Arial 15 bold', text='Тут должен быть текст, но как хотите)')
label.place(relx=0.5, y=30, anchor=CENTER)
t = Text(root, width=45, height=5, font='Arial 12 bold')
t.place(relx=0.5, y=100, anchor=CENTER)

btn = Button(root, width=45, text='Перевести', command=translation)
btn.place(relx=0.5, y=170, anchor=CENTER)

t1 = Text(root, width=45, height=5, font='Arial 12 bold')
t1.place(relx=0.5, y=240, anchor=CENTER)


root.mainloop()