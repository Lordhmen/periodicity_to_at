# -*- coding: utf-8 -*-
import sys

from PySide2 import QtGui
from PySide2.QtGui import QIntValidator
from PySide2.QtCore import (Qt, QPoint)
from PySide2.QtWidgets import *

from Functionss.ui_functions import *
from uii.ui_main import *
import math
from random import randint
import matplotlib.pyplot as plt


class MainWindows(QMainWindow):
    def __init__(self):
        global agregat, otkaz, resyrs, sr1, srnarabotka, perto, nachalo, X, Z, Y, konec, vopen, gr2, cmb, aaa, gr3
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dragPos = QPoint()
        self.ui.pushButton.clicked.connect(self.ras)
        # self.ui.pushButton_98.clicked.connect(self.printer)
        self.ui.plainTextEdit.setPlainText("Перед начлом работы программа создает экспоненциальный ряд распределения часов наработки до отказа, при запуске пользователь может видеть окно с вывода таблицы с данными о эмпирических показателях надежности, при переходе навторую вкладку программа выдаст рассчет количества запасных агрегатов на отказ при наработке, при переходе на третью вкладку появляется график данных безотказной работы и данных отказа с наработкой, а также на чествертой вкладке доступна информация о программе, авторе и сама инструкция к применению, которую вы только что прочитали.")
        self.ui.plainTextEdit_2.setPlainText('Программа предназначенна для определения переодичности ТО и необходимого количества запасных агрегатов для заданной наработки.')
        self.ui.plainTextEdit_3.setPlainText(
            'Данный программный продукт разработан курсантами 431 группы Кирсанов Г.В. и Заколюжная Е.Н. по специальности: 09.02.03 «Программирование в компьютерных системах»')

        # Установка валидатора
        pintValidator = QIntValidator(self)

        pintLineEdit = self.ui.lineEdit
        pintLineEdit.setValidator(pintValidator)

        self.setWindowTitle('Переодичность ТО АТ')
        UIFunctions.labelTitle(self, 'Переодичность ТО АТ')
        UIFunctions.labelDescription(self, 'Таблица расчетов')

        startSize = QSize(1089, 729)
        self.resize(startSize)
        self.setMinimumSize(startSize)

        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))

        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Таблица расчетов", "btn_report", "url(icons/32x32/cells.png)",
                               True)
        UIFunctions.addNewMenu(self, "Периодичность ТО", "btn_bill", "url(icons/32x32/abacus.png)",
                               True)
        UIFunctions.addNewMenu(self, "График", "btn_2", "url(icons/32x32/profits.png)",
                               True)
        UIFunctions.addNewMenu(self, "Информация", "btn", "url(icons/32x32/information.png)",
                               False)

        UIFunctions.selectStandardMenu(self, "btn_report")

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_report)
        self.ui.frame_label_top_btns.mouseMoveEvent = self.moveWindow
        UIFunctions.uiDefinitions(self)
        self.ui.tableWidget.verticalHeader().hide()
        self.ui.tableWidget.horizontalHeader().hide()

        self.ui.tableWidget.resizeRowsToContents()

        self.show()
        agregat = 110  # количество агрегатов
        otkaz = 100  # количество отказавших агрегатов
        resyrs = 6000  # назначенный ресурс
        # Рандомное заполнение значений отказов
        massiv = sorted([randint(1, resyrs) for i in range(otkaz)])
        file = open('masiv', 'w')
        file.write(str(massiv))
        file.close()
        # print(massiv)
        massiv = [20, 50, 65, 75, 153, 173, 187, 211, 211, 280, 411, 463, 500, 500, 500, 503, 550, 550, 660, 700, 700,
                  700, 750, 850, 900, 940, 1022, 1050, 1050, 1050, 1050, 1070, 1120, 1131, 1158, 1250, 1284, 1289, 1350,
                  1440, 1500, 1614, 1640, 1650, 1700, 1726, 1727, 1750, 1770, 1900, 1908, 1996, 2110, 2110, 2182, 2200,
                  2200, 2375, 2400, 2450, 2456, 2500, 2556, 2800, 2850, 2850, 2852, 2900, 2970, 2990, 3000, 3100, 3100,
                  3120, 3200, 3490, 3500, 3510, 3600, 3710, 3750, 3798, 3800, 4000, 4110, 4200, 4390, 4520, 4600, 4700,
                  4920, 5000, 5100, 5250, 5400, 5650, 5798, 5890, 6000, 6000]
        print(massiv)
        e = 2.71828  # экспонента
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
        intervalH = 0
        seredinaIntervalH = 1
        for h in range(10):  # Цикл по 10ти интервалам
            seredina = interval * shag  # Определение середины интервала
            shag += 1
            sr2 += str(str(round(seredina)))
            self.ui.tableWidget.setItem(seredinaIntervalH, 2, QTableWidgetItem(sr2))
            sr2 = ''
            # seredinaIntervalH += 1

            for i in massiv:  # Цикл по массиву
                if i > nachalo and i <= konec:  # Условие по интервалу
                    chisotkaz.append(i)
            konec = round(konec)  # Начало интервала
            nachalo = round(nachalo)  # Конец интервала
            nachalo = str(nachalo)
            konec = str(konec)
            gra = nachalo + '-' + konec  # Границы интервала
            self.ui.tableWidget.setItem(seredinaIntervalH, 1, QTableWidgetItem(gra))
            # intervalH += 1
            gr2 += str(str(gra))
            gr3 += str('через ' + str(gra) + ' час.')
            self.ui.tableWidget_2.setItem(intervalH, 0, QTableWidgetItem(gr3))
            # intervalH += 1
            gr3 = ''
            nachalo = int(nachalo)
            konec = int(konec)
            ch2 += str(str(len(chisotkaz)))  # Число отказов
            self.ui.tableWidget.setItem(seredinaIntervalH, 3, QTableWidgetItem(ch2))
            ch2 = ''
            # seredinaIntervalH += 1
            otnosch = len(chisotkaz) / (agregat * interval)  # Нахождение относительной частоты
            otnosch *= 10000
            ot2 += str(str(round(otnosch, 2)))
            self.ui.tableWidget.setItem(seredinaIntervalH, 4, QTableWidgetItem(ot2))
            ot2 = ''
            # seredinaIntervalH += 1
            dlina = dlina + len(chisotkaz)
            emp = (agregat - dlina) / agregat  # Нахождение эмперической надежности
            emna2 += str(str(round(emp, 3)))
            self.ui.tableWidget.setItem(seredinaIntervalH, 5, QTableWidgetItem(emna2))
            emna2 = ''
            # seredinaIntervalH += 1
            empinten = otnosch / emp1  # Эмперическая интенсивность отказов
            emp1 = emp
            emin2 += str(str(round(empinten, 2)))
            self.ui.tableWidget.setItem(seredinaIntervalH, 6, QTableWidgetItem(emin2))
            emin2 = ''
            # seredinaIntervalH += 1
            srnarabotka = sum(massiv) / otkaz  # Средняя наработка на отказ
            lmbd = (otkaz / (sum(massiv) + (agregat - otkaz) * resyrs))  # LAMBDA
            proizv = lmbd * konec  # Произведение лямбда на т-итое
            pr2 += str(str(round(proizv, 2)))
            self.ui.tableWidget.setItem(seredinaIntervalH, 7, QTableWidgetItem(pr2))
            pr2 = ''
            # seredinaIntervalH += 1
            bezotrab = e ** (proizv * (-1))  # Вероятность безотказной работы на интервале
            verb2 += str(str(round(bezotrab, 3)))
            self.ui.tableWidget.setItem(seredinaIntervalH, 8, QTableWidgetItem(verb2))
            verb2 = ''
            # seredinaIntervalH += 1
            vr = verotkaz
            verotkaz = 1 - bezotrab  # Вероятность отказа на интервале
            verot2 += str(str(round(verotkaz, 3)))
            self.ui.tableWidget.setItem(seredinaIntervalH, 9, QTableWidgetItem(verot2))
            verot2 = ''
            # seredinaIntervalH += 1
            plotras = (lmbd * (e ** ((lmbd * nachalo) * (-1)))) * 10000  # Плотность распределения
            pl2 += str(str(round(plotras, 2)))
            self.ui.tableWidget.setItem(seredinaIntervalH, 10, QTableWidgetItem(pl2))
            pl2 = ''
            seredinaIntervalH += 1

            chisotkaz = []
            p = e ** (-lmbd)
            p = float((str(p))[0:3])
            perto = -(srnarabotka) * math.log(p)  # Периодичность ТО
            z += 1

            if z == 1:
                x = verotkaz

            verotag = agregat * (verotkaz - vr)  # Вероятность отказа агрегата
            if z == 1:
                cmb = str(str(round(verotag)) + ' шт.')
                aaa = round(verotag)
                self.ui.tableWidget_2.setItem(10, 1, QTableWidgetItem(str(aaa)))
            if h != 0:
                verotag1 = verotag + round(verotag * x)
                cmb += str(str(round(verotag1)) + ' шт.')
                aaa += round(verotag1)  # Всего запасных агрегатов
                self.ui.tableWidget_2.setItem(10, 1, QTableWidgetItem(str(aaa)))
            self.ui.tableWidget_2.setItem(intervalH, 1, QTableWidgetItem(cmb))
            cmb = ''
            intervalH += 1

            X.append(verotkaz)
            Y.append(bezotrab)
            Z.append(konec)

            nachalo += interval
            konec += interval
        # print(aaa)
        # self.ui.tableWidget_2.setItem(9, 1, QTableWidgetItem(aaa))
        self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.tableWidget_2.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.lineEdit.setText(str(agregat))
        self.ui.lineEdit_6.setText(str(round(srnarabotka)) + ' час.')
        self.ui.lineEdit_7.setText(str(round(perto)) + ' час.')

    def ras(self):
        chas = int(self.ui.lineEdit_2.text())
        print(chas)
        massiv = []
        for i in range(10):
            massiv.append([self.ui.tableWidget_2.item(i, 0).text(), self.ui.tableWidget_2.item(i, 1).text()])
        qqqq = 0
        for i in massiv:
            massiv[qqqq][0] = int(massiv[qqqq][0].split()[1].split('-')[1])
            massiv[qqqq][1] = int(massiv[qqqq][1].split()[0])
            qqqq += 1
        print(massiv)
        summ = 0
        qqqq = 1
        for i in massiv:
            if chas > i[0]:
                summ += i[1]
            if chas < i[0]:
                summ += i[1]
                break
            if chas == i[0]:
                summ += i[1]
                break
        print(summ)
        self.ui.label_7.setText(str(summ))
    def grafic(self):
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

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def moveWindow(self, event):
        if UIFunctions.returStatus() == 1:
            UIFunctions.maximize_restore(self)

        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def Button(self):
        btnWidget = self.sender()

        if btnWidget.objectName() == "btn_report":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_report)
            UIFunctions.resetStyle(self, "btn_report")
            UIFunctions.labelPage(self, "Таблица расчетов")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_bill":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_bill)
            UIFunctions.resetStyle(self, "btn_bill")
            UIFunctions.labelPage(self, "Периодичность ТО")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_2":
            self.grafic()

        if btnWidget.objectName() == "btn":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page)
            UIFunctions.resetStyle(self, "btn")
            UIFunctions.labelPage(self, "Информация")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindows()
    sys.exit(app.exec_())
