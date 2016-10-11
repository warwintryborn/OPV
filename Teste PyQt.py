# Interface gráfica com ícone e POO
import sys
import threading
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class janelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(0, 30, 1366, 738)
        self.setWindowTitle('Janela com ícone')
        self.setWindowIcon(QIcon('world.png'))
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = janelaPrincipal()
    sys.exit(app.exec_()) 
