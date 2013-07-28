'''
Created on 2013-7-21

@author: hujin
'''

from PySide.QtCore import *
from PySide.QtGui import *

class AboutDialog(QDialog):
    
    def __init__(self, parent = None):
        super(AboutDialog, self).__init__(parent)
        self.resize(300, 200)
        self.setWindowTitle('About')
    
    def show(self):
        self.exec_()
        
    @classmethod
    def create_and_show(cls, parent):
        dialog = __class__(parent)
        dialog.show()



