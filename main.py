import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        self.data = list(self.cur.execute("SELECT * FROM coffee"))
        self.table.setRowCount(len(self.data))
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.table.addItem(i, j, QTableWidgetItem(self.data[i][j]))
        self.con.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
