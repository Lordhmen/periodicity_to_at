import tkinter as tk
from tkinter import *
from tkinter import messagebox
import math
from random import randint
import matplotlib.pyplot as plt


def ramka():
    global cmb, gr2, aaa, gr3
    rm = Tk()
    rm.geometry('500x400')
    rm.config(bg='lightblue')
    rm.title('Периодичность ТО')
    rm.resizable(width=False, height=False)

    Label(rm,
          text='Число контролируемых изделий\n      Средняя наработка на отказ\n                    Периодичность ТО',
          font='arial 13', bg='lightblue').place(x=0, y=330)
    Label(rm, text='Количество запасных агрегатов на интервале', font='arial 13', bg='lightblue').place(x=74, y=10)
    Label(rm, text=agregat, font='arial 13', bg='lightblue').place(x=260, y=330)
    Label(rm, text=str(round(srnarabotka)) + ' час.', font='arial 13', bg='lightblue').place(x=260, y=349)
    Label(rm, text=str(round(perto)) + ' час.', font='arial 13', bg='lightblue').place(x=260, y=368)
    # Интервалы
    Label(rm, text=gr3 + 'Всего: ', font='arial 13', bg='lightblue').place(x=40, y=40)
    Label(rm, text=cmb + str(round(aaa)) + ' шт.', font='arial 13', bg='lightblue').place(x=300, y=40)


def rasschets():
    root.withdraw()  # скрыть окно
    global agregat, otkaz, resyrs, sr1, srnarabotka, perto, nachalo, X, Z, Y, konec, vopen, gr2, cmb, aaa, gr3
    agregat = agrent.get()  # количество агрегатов
    otkaz = otkent.get()  # количество отказавших агрегатов
    resyrs = resent.get()  # назначенный ресурс

    if len(agregat) == 0 or len(otkaz) == 0 or len(resyrs) == 0:
        tk.messagebox.showerror("Ошибка", "Введите данные в пустую ячейку!")
        return
    if agregat.isalpha() == True:
        tk.messagebox.showerror("Ошибка", "Введите в поле число, а не символ!")
        return
    if otkaz.isalpha() == True:
        tk.messagebox.showerror("Ошибка", "Введите в поле число, а не символ!")
        return
    if resyrs.isalpha() == True:
        tk.messagebox.showerror("Ошибка", "Введите в поле число, а не символ!")
        return

        # Создание окна
    ras = Tk()
    ras.geometry('1360x340')
    ras.config(bg='lightblue')
    ras.title('Таблица расчетов')
    ras.resizable(width=False, height=False)

    # Таблица
    Label(ras, text='№ интер \n вала \n \n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n', width=7, font='arial 12',
          bg='lightblue').place(x=1, y=1)
    Label(ras, text='Границы\nинтервала', width=16, font='arial 12', bg='lightblue').place(x=75, y=1)
    gr1 = Label(ras, text='b', width=16, font='arial 12', bg='lightblue')
    gr1.place(x=75, y=54)
    Label(ras, text='Середина\nинтервала', width=12, font='arial 12', bg='lightblue').place(x=230, y=1)
    sr1 = Label(ras, text='\n', width=12, font='arial 12', bg='lightblue')
    sr1.place(x=230, y=54)
    Label(ras, text='Число\nОтказов', width=8, font='arial 12', bg='lightblue').place(x=349, y=1)
    ch1 = Label(ras, text='b', width=8, font='arial 12', bg='lightblue')
    ch1.place(x=349, y=54)
    Label(ras, text='Относительная\nчастота', width=13, font='arial 12', bg='lightblue').place(x=432, y=1)
    ot1 = Label(ras, text='b', width=13, font='arial 12', bg='lightblue')
    ot1.place(x=432, y=54)
    Label(ras, text='Эмпирическая\nнадежность', width=13, font='arial 12', bg='lightblue').place(x=560, y=1)
    emna1 = Label(ras, text='b', width=13, font='arial 12', bg='lightblue')
    emna1.place(x=560, y=54)
    Label(ras, text='Эмпирическая\nинтенсивность', width=13, font='arial 12', bg='lightblue').place(x=688, y=1)
    emin1 = Label(ras, text='b', width=13, font='arial 12', bg='lightblue')
    emin1.place(x=688, y=54)
    Label(ras, text='Произведение\n', width=12, font='arial 12', bg='lightblue').place(x=815, y=1)
    pr1 = Label(ras, text='b', width=12, font='arial 12', bg='lightblue')
    pr1.place(x=815, y=54)
    Label(ras, text='Вер. безотказной\nработы на интервале', width=18, font='arial 12', bg='lightblue').place(x=933,
                                                                                                              y=1)
    verb1 = Label(ras, text='b', width=18, font='arial 12', bg='lightblue')
    verb1.place(x=933, y=54)
    Label(ras, text='Вер. отказа\nна интервале', width=12, font='arial 12', bg='lightblue').place(x=1105, y=1)
    verot1 = Label(ras, text='b', width=12, font='arial 12', bg='lightblue')
    verot1.place(x=1105, y=54)
    Label(ras, text='Плотность\nраспределения', width=13, font='arial 12', bg='lightblue').place(x=1223, y=1)
    pl1 = Label(ras, text='b', width=13, font='arial 12', bg='lightblue')
    pl1.place(x=1223, y=54)
    nazad = Button(ras, text="Назад", font='arial 15', bg='lightgreen', fg='black', width=15,
                   command=lambda: root.deiconify() + ras.withdraw())  # vivod
    nazad.place(x=10, y=290)
    graf = Button(ras, text="Открыть график", font='arial 15', bg='lightgreen', fg='black', width=15, command=grafic)
    graf.place(x=390, y=290)
    rmk = Button(ras, text="Результат", font='arial 15', bg='lightgreen', fg='black', width=15, command=ramka)  # vivod
    rmk.place(x=200, y=290)
    agregat = int(agregat)
    otkaz = int(otkaz)
    resyrs = int(resyrs)

    # Рандомное заполнение значений отказов
    massiv = sorted([randint(1, resyrs) for i in range(otkaz)])
    print(massiv)
    i = 0
    e = 2.71828
    shag = 0.5
    interval = resyrs / 10  # Определение интервалов
    chisotkaz = []  # Число отказов в определенном массиве
    nachalo = 0  # Начало интервала
    konec = interval  # Конец интервала
    dlina = 0  # Количество элементов в интервале
    verotkaz = 0
    aaa = 0
    emp1 = 1
    z = 0
    x = 0
    verotag1 = 0
    cmb = 0
    # Создание списков хранения данных
    sr2 = ''
    gr3 = ''
    gr2 = ''
    ch2 = ''
    ot2 = ''
    emna2 = ''
    emin2 = ''
    pr2 = ''
    verb2 = ''
    verot2 = ''
    pl2 = ''
    X = []
    Y = []
    Z = []
    fig = plt.figure(0)
    fig.canvas.set_window_title('График')
    for h in range(10):  # Цикл по 10ти интервалам
        seredina = interval * shag  # Определение середины интервала
        shag += 1
        sr2 += str(str(round(seredina)) + '\n')

        for i in massiv:  # Цикл по массиву
            if i > nachalo and i <= konec:  # Условие по интервалу
                chisotkaz.append(i)
        print(chisotkaz)
        konec = round(konec)  # Начало интервала
        nachalo = round(nachalo)  # Конец интервала
        nachalo = str(nachalo)
        konec = str(konec)
        gra = nachalo + '-' + konec  # Границы интервала
        gr2 += str(str(gra) + '\n')
        gr3 += str('через ' + str(gra) + ' час.\n')
        nachalo = int(nachalo)
        konec = int(konec)
        ch2 += str(str(len(chisotkaz)) + '\n')  # Число отказов
        otnosch = len(chisotkaz) / (agregat * interval)  # Нахождение относительной частоты
        otnosch *= 10000
        ot2 += str(str(round(otnosch, 2)) + '\n')
        dlina = dlina + len(chisotkaz)
        emp = (agregat - dlina) / agregat  # Нахождение эмперической надежности
        emna2 += str(str(round(emp, 3)) + '\n')
        empinten = otnosch / emp1  # Эмперическая интенсивность отказов
        emp1 = emp
        emin2 += str(str(round(empinten, 2)) + '\n')
        srnarabotka = sum(massiv) / otkaz  # Средняя наработка на отказ
        lmbd = (otkaz / (sum(massiv) + (agregat - otkaz) * resyrs))  # LAMBDA
        proizv = lmbd * konec  # Произведение лямбда на т-итое
        pr2 += str(str(round(proizv, 2)) + '\n')
        bezotrab = e ** (proizv * (-1))  # Вероятность безотказной работы на интервале
        verb2 += str(str(round(bezotrab, 3)) + '\n')
        vr = verotkaz
        verotkaz = 1 - bezotrab  # Вероятность отказа на интервале
        verot2 += str(str(round(verotkaz, 3)) + '\n')
        plotras = (lmbd * (e ** ((lmbd * nachalo) * (-1)))) * 10000  # Плотность распределения
        pl2 += str(str(round(plotras, 2)) + '\n')

        chisotkaz = []
        p = e ** (-lmbd)
        p = float((str(p))[0:3])
        perto = -(srnarabotka) * math.log(p)  # Периодичность ТО
        z += 1

        if z == 1:
            x = verotkaz

        verotag = agregat * (verotkaz - vr)  # Вероятность отказа агрегата
        if z == 1:
            cmb = str(str(round(verotag)) + ' шт.\n')
            aaa = round(verotag)
        if h != 0:
            verotag1 = verotag + round(verotag * x)
            cmb += str(str(round(verotag1)) + ' шт.\n')
            aaa += round(verotag1)  # Всего запасных агрегатов

        X.append(verotkaz)
        Y.append(bezotrab)
        Z.append(konec)

        nachalo += interval
        konec += interval

        # Вывод данных в таблицу
    sr1.configure(text=sr2)
    emin1.configure(text=emin2)
    ch1.configure(text=ch2)
    pl1.configure(text=pl2)
    verb1.configure(text=verb2)
    verot1.configure(text=verot2)
    emna1.configure(text=emna2)
    ot1.configure(text=ot2)
    gr1.configure(text=gr2)
    pr1.configure(text=pr2)


def grafic():
    fig = plt.figure(0)
    fig.canvas.set_window_title('График')
    plt.plot(Z, X, label='F(t)', marker='.')
    plt.plot(Z, Y, label='P(t)', marker='.')
    plt.xlim(0, konec)
    plt.ylim(0, 1)
    plt.grid()

    plt.xlabel('Наработка')
    plt.ylabel('Вероятность безотказной работы')
    plt.legend(loc='upper right')
    plt.show()


def inst():

    pass

def naznachenie():
    tk.messagebox.showinfo('Назначение программы',
                           'Программа предназначенна для определения переодичности ТО и необходимого количества запасных агрегатов для заданной наработки..')


def avtor():
    tk.messagebox.showinfo('Автор', 'Цюра Г.В. и Дианка \nкурсанты 431 группы ТАТК ГА')


root = Tk()
root.geometry('420x220')
root.config(bg='lightblue')
root.title('Переодичность ТО АТ')
root.resizable(width=False, height=False)

mainmenu = Menu(root)
root.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Назначение программы', command=naznachenie)
filemenu.add_command(label='Инструкция', command=inst)
filemenu.add_command(label='Автор', command=avtor)
mainmenu.add_cascade(label='Меню', menu=filemenu)

ok = Button(root, text="Вычислить", font='arial 15', bg='lightgreen', fg='black', width=15, command=rasschets)
ok.place(x=80, y=140)
agrlab = Label(root, text='Количество агрегатов', width=20, font='arial 14', bg='lightblue')
agrlab.place(x=10, y=8)
otklab = Label(root, text='Количество \n отказавших агрегатов', width=20, font='arial 14', bg='lightblue')
otklab.place(x=10, y=40)
reslab = Label(root, text='Назначенный ресурс', width=20, font='arial 14', bg='lightblue')
reslab.place(x=10, y=95)

agrent = Entry(root, width=10, font='arial 14', textvariable='')
agrent.place(x=250, y=9)
otkent = Entry(root, width=10, font='arial 14', textvariable='')
otkent.place(x=250, y=52)
resent = Entry(root, width=10, font='arial 14', textvariable='')
resent.place(x=250, y=95)

root.mainloop()
