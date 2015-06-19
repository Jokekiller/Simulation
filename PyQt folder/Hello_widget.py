#Hello widget
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class backWidget(QWidget):
    Back = pyqtSignal()
    def __init__(self):
        super(). __init__()

        #create components
        self.label = QLabel()
        self.back = QPushButton("Back")

        #creating layout
        self.layout = QVBoxLayout()

        #add to layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.back)

        #add layout to widget
        self.setLayout(self.layout)

        #connections
        self.back.clicked.connect(self.back_to_main)
        
    def changeLabel(self,name):
        name_string = "Hello {0}".format(name)
        self.label.setText(name_string)

    def back_to_main(self):
        self.Back.emit()
