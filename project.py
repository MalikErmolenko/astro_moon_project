import math
# импортируем библиотеки
import tkinter as tk
import tkinter.filedialog
from PIL import Image,ImageTk
from tkinter import Label, Entry, Button, filedialog



























# пишем функцию открытия картинки в программе
def openImage():
    url=url=filedialog.askopenfilename()
    if url:
        img=Image.open(url)
        img.thumbnail((600,600))
        img=ImageTk.PhotoImage(img)
        imageLabel.config(image=img)
        imageLabel.image = img


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


def heightMountain():
    try:
        # задаем команды считывания символов по формуле(уже сделал)
        R_0= float(entry_R0.get())
        D_0= float(entry_D0.get())
        D=float(entry_D.get())
        phi_Prime=float(entry_phi_prime.get())
        LT=float(entry_LT.get())
        LM=float(entry_LM.get())
        delta_prime=float(entry_Delta.get())
        S_prime=float(entry_S.get())
    except Exception as E:
        # или ошибку если не получается(отриц.число и тд)
        result_label.config(text=f'invalid data has been entered')
        
    try:
        k = D_0 / D
        phi = math.asin(phi_Prime / R_0)
     # phi=math.degrees(phi)
        R_phi = R_0 * math.cos(phi)
        alpha = math.acos((R_phi - LT) / R_phi) - math.acos((R_phi - LM) / R_phi)
        # alpha=math.degrees(alpha)
        Delta = math.asin(delta_prime / R_phi)
        # Delta=math.degrees(Delta)
        S = k * S_prime / math.cos(Delta)
        H = S * math.tan(alpha)
        result_label.config(text=f'Высота горы: {round(H,4)}')
    except Exception as E:
        result_label.config(text=f'Error {E}')

    


# Создаем главное окно
 
root=tk.Tk()
root.title('calculator')






















# Создаем и размещаем элементы управления
label_R0 = Label(root, text="R0:")
label_R0.grid(row=0, column=0)
entry_R0 = Entry(root)
entry_R0.grid(row=0, column=1)
Label_D = Label(root, text="D:")
Label_D.grid(row=1, column=0)
entry_D = Entry(root)
entry_D.grid(row=1, column=1)
label_LT = Label(root, text="LT':")
label_LT.grid(row=2, column=0)
entry_LT = Entry(root)
entry_LT.grid(row=2, column=1)
label_LM = Label(root, text="LM':")
label_LM.grid(row=3, column=0)
entry_LM = Entry(root)
entry_LM.grid(row=3, column=1)
label_S = Label(root, text="S':")
label_S.grid(row=4, column=0)
entry_S = Entry(root)
entry_S.grid(row=4, column=1)
label_Delta = Label(root, text="δ':")
label_Delta.grid(row=5, column=0)
entry_Delta = Entry(root)
entry_Delta.grid(row=5, column=1)
label_phi_prime = Label(root, text="φ':")
label_phi_prime.grid(row=6, column=0)
entry_phi_prime = Entry(root)
entry_phi_prime.grid(row=6, column=1)
label_D0 = Label(root, text="D0:")
label_D0.grid(row=7, column=0)
entry_D0 = Entry(root)
entry_D0.grid(row=7, column=1)

# ... Аналогично для других переменных ...

button_calculate = Button(root, text="Calculate",command=heightMountain)
button_calculate.grid(row=8 ,columnspan=2)

result_label = tk.Label(root)
result_label.grid(row=10, columnspan=2)

imageLabel= Label(root)
imageLabel.grid(row=0,column=3,rowspan=10)

ButtonImage=Button(root,text='Load image',command=openImage)
ButtonImage.grid(row=11,columnspan=2)

# Запускаем главный цикл программы
root.mainloop()
# запускаем...