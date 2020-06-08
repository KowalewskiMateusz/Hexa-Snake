#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from client import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from untiltled import Ui_Dialog
import sys
import json
from Snake import *
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
import copy

"""
Sterowanie:
Gracz 1:
u - prawo góra
t - lewo góra
g - lewo
j - prawo
m - prawo dół
b - lewo dół

Gracz 2:
e - prawo góra
q - lewo góra
a - lewo
d - prawo
c - prawo dół
z - lewo dół

W trybie gry przez sieć obaj gracze sterują swoimi wężami za pomocą sterowania gracza 1.
Po naciśnięciu przycisku "Zapisz ustawienia" ustawienia wpisane w pola tekstowe zostaje zapisane do pliku json.
Po naciśnięciu przycisku "Wczytaj ustawienia" ustawienia zostają wczytane z plikus json.
Po naciśnięciu przycisku "Zapisuj gre" historia gry zostaje zapisana. Gra kończy się zapisywać w przypadku przegranej
lub w przypadku zmiany gry na inny tryb w trakcie grania. 
Po naciśnięciu przycisku "Wczytaj gre" historia ostatniej zapisywanej gry zostaje wczytana.
Po naciśnięciu przycisku "Replay" cała poprzednia rozgrywka zostaje odtworzona. W momencie odtwarzania gracz nie ma
możliwościu ingerencji w gre.
"""


class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pole = Pole(70, 25)
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(QRect(0, 0, 560, 200))
        self.scene.setBackgroundBrush(QBrush(QColor(52, 56, 56), Qt.SolidPattern))
        self.graphicsView.setScene(self.scene)
        self.pushButton.clicked.connect(self.on_click_1)
        self.pushButton_2.clicked.connect(self.on_click_2)
        self.pushButton_3.clicked.connect(self.on_click_3)
        self.pushButton_4.clicked.connect(self.on_click_4)
        self.pushButton_5.clicked.connect(self.on_click_5)
        self.pushButton_6.clicked.connect(self.on_click_6)
        self.pushButton_7.clicked.connect(self.on_click_7)
        self.pushButton_8.clicked.connect(self.on_click_8)
        self.QRadioButton.toggled.connect(self.game_type)
        self.QRadioButton2.toggled.connect(self.game_type)
        self.QRadioButton3.toggled.connect(self.game_type)
        self.QRadioButton4.toggled.connect(self.game_type)
        self.setFocusPolicy(Qt.StrongFocus)
        self.timer = QBasicTimer()
        self.host = "localhost"
        self.port = 5000
        self.nick_1 = "User 1"
        self.nick_2 = "User 2"
        self.QLineEdit1.setText(self.host)
        self.QLineEdit2.setText(str(self.port))
        self.QLineEdit3.setText(self.nick_1)
        self.QLineEdit4.setText(self.nick_2)
        self.lost_1 = False
        self.lost_2 = False
        self.multi = False
        self.ai = False
        self.online = False
        self.record = False
        self.replay = False
        self.client = None
        self.keys1 = []
        self.keys2 = []
        self.show()

    def on_click_1(self):
        self.record = False
        self.replay = False
        if self.online:
            self.keys1.clear()
            self.keys2.clear()
            self.client = Client(self.host, self.port)

        else:
            self.clear_keys()
            if self.timer:
                self.timer.stop()
            self.pole = Pole(70, 25)
            self.lost_1 = False
            self.lost_2 = False
            valid = False
            while not valid:
                x = random.randint(1, self.pole.x - 1)
                y = random.randint(1, self.pole.y - 1)
                valid, self.pole.owoc = is_valid([x, y], 1, self.pole, 'owoc', 0)

            valid = False
            while not valid:
                x = random.randint(1, self.pole.x - 1)
                y = random.randint(1, self.pole.y - 1)
                valid, self.snake_1 = is_valid([x, y], 1, self.pole, 'snake', 1)

            valid = False
            if self.multi or self.ai:
                while not valid:
                    x = random.randint(1, self.pole.x - 1)
                    y = random.randint(1, self.pole.y - 1)
                    valid, self.snake_2 = is_valid([x, y], 1, self.pole, 'snake', 2)
            self.update()

    def clear_keys(self):
        global keys1
        global keys2
        self.keys1.clear()
        self.keys2.clear()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_G:
            self.keys1.append('g')
        elif event.key() == Qt.Key_J:
            self.keys1.append('j')
        elif event.key() == Qt.Key_T:
            self.keys1.append('t')
        elif event.key() == Qt.Key_U:
            self.keys1.append('u')
        elif event.key() == Qt.Key_B:
            self.keys1.append('b')
        elif event.key() == Qt.Key_M:
            self.keys1.append('m')
        if self.multi:
            if event.key() == Qt.Key_Q:
                self.keys2.append('q')
            elif event.key() == Qt.Key_E:
                self.keys2.append('e')
            elif event.key() == Qt.Key_A:
                self.keys2.append('a')
            elif event.key() == Qt.Key_D:
                self.keys2.append('d')
            elif event.key() == Qt.Key_Z:
                self.keys2.append('z')
            elif event.key() == Qt.Key_C:
                self.keys2.append('c')

    def on_click_2(self):
        if self.online:
            while 1:
                start = self.client.s.recv(1024).decode()
                if start == "True":
                    self.timer.start(1000, self)
                    break
                else:
                    pass
        else:
            self.timer.start(1000, self)

    def on_click_3(self):
        sys.exit()

    def timerEvent(self, event):
        if self.replay:
            if self.moves:
                self.pole.map = self.moves[0]
                self.moves.pop(0)
            else:
                self.timer.stop()
                self.replay = False
            return

        if self.online:
            try:
                self.client.send_mes(self.keys1)
            except:
                self.timer.stop()
                self.record = False
            try:
                self.pole = self.client.recv_pole()
            except:
                self.timer.stop()
                self.record = False
        else:
            if len(self.keys1) > 0:
                self.lost_1 = ruch(self.pole, self.snake_1, self.pole.owoc, self.keys1[-1], 1)
            if self.multi and len(self.keys2):
                self.lost_2 = ruch(self.pole, self.snake_2, self.pole.owoc, self.keys2[-1], 2)
            if self.ai:
                self.move = self.bot()
                self.lost_2 = ruch(self.pole, self.snake_2, self.pole.owoc, self.move, 2)
            if self.lost_1 or self.lost_2:
                self.timer.stop()
                self.clear_keys()
                self.record = False

        if self.record and not self.lost_1 and not self.lost_2:
            self.append_xml()
        self.update()

    def paintEvent(self, event):
        self.scene.clear()
        for i in range(self.pole.y):
            for j in range(self.pole.x):
                if self.pole.map[i][j] == "s":
                    x = i * 8
                    y = j * 8
                    self.scene.addRect(y, x, 8, 8).setBrush(QColor("green"))
                elif self.pole.map[i][j] == "o":
                    x = i * 8
                    y = j * 8
                    self.scene.addRect(y, x, 8, 8).setBrush(QColor("yellow"))
                elif self.pole.map[i][j] == "w":
                    x = i * 8
                    y = j * 8
                    self.scene.addRect(y, x, 8, 8).setBrush(QColor("blue"))
                elif self.pole.map[i][j] == "#":
                    x = i * 8
                    y = j * 8
                    # self.scene.addRect(y, x, 8, 8).setBrush(QColor("purple")) #Tu albo normalnie albo resources
                    self.qrc = QGraphicsPixmapItem(':/qrc_rect')  # Nie wiedzialem gdzie mógłbym użyć resources
                    self.qrc.setPos(y, x)  # Więc po prostu użyłem ich zamiast kwadratów
                    self.scene.addItem(self.qrc)  # Tworzących granice mapy
        self.update()

    def game_type(self):
        if self.QRadioButton.isChecked():
            self.multi = True
            self.online = False
            self.ai = False
            self.record = False
        if self.QRadioButton2.isChecked():
            self.multi = False
            self.online = True
            self.ai = False
            self.record = False
        if self.QRadioButton3.isChecked():
            self.multi = False
            self.online = False
            self.ai = False
            self.record = False
        if self.QRadioButton4.isChecked():
            self.multi = False
            self.online = False
            self.record = False
            self.ai = True

    def on_click_4(self):
        self.host = self.QLineEdit1.text()
        self.port = int(self.QLineEdit2.text())
        self.nick_1 = self.QLineEdit3.text()
        self.nick_2 = self.QLineEdit4.text()
        self.QTextEdit5.setText(self.nick_1)
        self.QTextEdit6.setText(self.nick_2)
        data = [self.host, self.port, self.nick_1, self.nick_2]
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)

    def on_click_5(self):
        self.timer.stop()
        self.load_xml()

    def on_click_6(self):
        self.timer.start(1000, self)
        self.replay = True

    def on_click_8(self):
        self.record = True
        self.setup_xml()

    def on_click_7(self):
        with open('data.json', 'r') as outfile:
            self.data = json.load(outfile)
        self.host = self.data[0]
        self.port = self.data[1]
        self.nick_1 = self.data[2]
        self.nick_2 = self.data[3]
        self.QLineEdit1.setText(self.host)
        self.QLineEdit2.setText(str(self.port))
        self.QLineEdit3.setText(self.nick_1)
        self.QLineEdit4.setText(self.nick_2)
        self.QTextEdit5.setText(self.nick_1)
        self.QTextEdit6.setText(self.nick_2)


    def setup_xml(self):
        self.root = Element('root')

    def append_xml(self):
        if self.lost_1 or self.lost_2:
            self.record = False
            self.output_file.close()

        if self.record:
            print("TU", self.record)
            self.round = SubElement(self.root, 'round')
            for i in range(self.pole.y):
                for j in range(self.pole.x):
                    SubElement(self.round, 'tile', x=str(i), y=str(j), sign=self.pole.map[i][j])

            self.output_file = open('save_game.xml', 'w')
            self.output_file.write(ElementTree.tostring(self.root).decode("UTF-8"))

    def load_xml(self):
        self.moves = []
        self.root = ElementTree.parse('save_game.xml')
        self.rounds = self.root.findall('round')
        for round in self.rounds:
            for tile in round:
                self.pole.map[int(tile.attrib['x'])][int(tile.attrib['y'])] = str(tile.attrib['sign'])
            self.history = copy.deepcopy(self.pole.map)
            self.moves.append(self.history)

    def bot(self):
        self.pos_moves = {'1': 'q', '2': 'e',' 3': 'd', '4': 'a', '5': 'z', '6': 'c'}
        self.bot_y = self.snake_2.body[-1]
        self.bot_x = self.snake_2.body[-2]
        self.direction_x = self.pole.owoc.x - self.bot_x
        self.direction_y = self.pole.owoc.y - self.bot_y
        move = None
        if self.direction_x == 0 and self.direction_y < 0:
            move = 'e'
        if self.direction_x == 0 and self.direction_y > 0:
            move = 'z'
        if self.direction_x > 0 and self.direction_y == 0:
            move = 'd'
        if self.direction_x < 0 and self.direction_y < 0:
            move = 'a'
        if self.direction_x > 0 and self.direction_y > 0:
            move = 'c'
        if self.direction_x < 0 and self.direction_y < 0:
            move = 'q'
        if self.direction_x < 0 and self.direction_y > 0:
            move = 'z'
        if self.direction_x > 0 and self.direction_y < 0:
            move = 'e'

        valid = self.check(move)
        if valid:
            return move
        else:
            for a in self.pos_moves.keys():
                move = self.pos_moves[a]
                valid = self.check(move)
                if valid:
                    return move
        return 'q'

    def check(self,komenda):
        pole = copy.deepcopy(self.pole)
        snake_2 = copy.deepcopy(self.snake_2)
        valid = ruch(pole, snake_2, pole.owoc,komenda ,2)
        if valid:
            return False
        else:
            return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
