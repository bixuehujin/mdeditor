'''
Created on 2013-7-21

@author: hujin
'''
import os
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader

from mdeditor.ui.dialog import AboutDialog
from mdeditor.ui.widget import MarkdownEdit

class MainWindow(QWidget):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        loader = QUiLoader()
        self.ui = loader.load('res/main.ui', self)
        self.ui.setWindowTitle('markdown-editor')
        self.ui.setWindowIcon(QIcon('/home/hujin/Pictures/avatar.jpg'))
        __class__.center(self.ui)
        
        self.ui.action_open.triggered.connect(self.on_open)
        self.ui.action_save.triggered.connect(self.on_save)
        
        self.ui.action_about.triggered.connect(self.on_about)
        
        '''
        self.resize(900, 500)
        #self.move(300, 300)
        self.center()
        
        #self.setGeometry(300, 300, 250, 250)
        #self.setToolTip('This is a <b>QWidget</b> widget')
        
        self.statusBar().showMessage('Ready')
        
        self.init_ui()
        self.init_menu()
        self.init_toolbar()
        '''
        
    def init_ui(self):
        '''
        btnOk = QPushButton('Ok', self)
        btnOk.setToolTip('Click Me')
        btnOk.resize(btnOk.sizeHint())
        btnOk.clicked.connect(QCoreApplication.instance().quit)
        
        btnCancel = QPushButton('Cancel')
        
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btnOk)
        hbox.addWidget(btnCancel)
        self.setLayout(hbox)
        '''
        central = QWidget()
        
        fileTree = QTreeView()
        
        model = QFileSystemModel()
        model.setRootPath('file:///home/hujin')   
        
        fileTree.setModel(model)
        
        
        
        textEdit = MarkdownEdit()

        hbox = QHBoxLayout(central)
        splitter = QSplitter()
        splitter.addWidget(fileTree)
        splitter.addWidget(textEdit)
        #hbox.addStretch()
        hbox.addWidget(splitter)
        
        self.setCentralWidget(central)
        #self.setLayout(hbox)    
       
    
    
    def init_toolbar(self):
        
        exitAction = QAction(QIcon('/home/hujin/Pictures/avatar.jpg'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QApplication.instance().quit)
        
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def show(self):
        self.ui.show()
    
    '''
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'quit', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if (reply == QMessageBox.Yes):
            event.accept()
        else:
            event.ignore()
    '''

    def on_save(self):
        fname, _ = QFileDialog.getSaveFileName(self, 'Save file')
        print(fname)
    
    
    def on_open(self):
        fname, _ = QFileDialog.getOpenFileName(self.ui, 'Open file', os.getenv('HOME'))
        print(fname)
    
    def on_about(self):
        AboutDialog.create_and_show(self.ui)
