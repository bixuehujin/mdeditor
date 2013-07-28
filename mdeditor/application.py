'''
Created on 2013-7-21

@author: hujin
'''

import sys
from PySide.QtGui import QApplication
from mdeditor.ui.window import MainWindow

class Application(QApplication):
    
    def __init__(self):
        '''
        Constructor
        '''
        super(Application, self).__init__(sys.argv)
        
    def run(self):
        '''
        Run the application.
        '''
        frame = MainWindow()
        frame.show()
        self.exec_()
        sys.exit()
    
