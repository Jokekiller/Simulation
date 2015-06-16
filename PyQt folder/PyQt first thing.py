#Harry Robinosn
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Name_widget import *

import sys

class ExampleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")

        #create stacked layout
        self.stack = QStackedLayout()

        #create ui widgets
        self.name = NameWidget()

        #add widgets to stack
        self.stack.addWidget(self.name)

        #wrap stack in a widget
        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        #set central widget
        self.setCentralWidget(self.widget)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExampleWindow()
    window.show()
    window.raise_()
    app.exec_()
