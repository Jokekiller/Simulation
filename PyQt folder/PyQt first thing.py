#Harry Robinosn
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Name_widget import *
from Hello_widget import *

import sys

class ExampleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")

        #create stacked layout
        self.stack = QStackedLayout()

        #create ui widgets
        self.name = NameWidget()
        self.back = backWidget()

        #add widgets to stack
        self.stack.addWidget(self.name)
        self.stack.addWidget(self.back)

        #wrap stack in a widget
        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        #set central widget
        self.setCentralWidget(self.widget)

        #connections
        self.name.NameEntered.connect(self.name_entered)
        self.back.Back.connect(self.clear_name)

    def name_entered(self):
        print("A name entered")
        self.stack.setCurrentIndex(1)
        name = self.name.name.text()
        self.back.changeLabel(name)

    def clear_name(self):
        self.stack.setCurrentIndex(0)
        self.name.name.clear()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExampleWindow()
    window.show()
    window.raise_()
    app.exec_()
