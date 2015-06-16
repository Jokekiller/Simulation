#Name widget
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class NameWidget(QWidget):
    NameEntered = PyqtSignal()
    def __init__(self):
        super().__init__()

        #create components
        self.label = QLabel("Enter name: ")
        self.name = QLineEdit()
        self.submit = QPushButton("Submit")

        #creating layout
        self.layout = QVBoxLayout()

        #Add to layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.name)
        self.layout.addWidget(self.submit)

        #Add layout to widget
        self.setLayout(self.layout)

        #connections
        self.submit.clicked.connect(self.display_name)
        
    def display_name(self):
        name = self.name.text()
        print(name)
        self.NameEntered.
