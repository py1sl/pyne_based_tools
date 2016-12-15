"""
fispact gui for looking at outputs
Author: S Lilley

"""
import sys
import glob
import numpy as np
from pyne import fispact
from PySide import QtGui, QtCore

import plot_inv
import plot_act
import plot_comp
import plot_dominant
import plot_spectra


class qtinter(QtGui.QMainWindow):
    def __init__(self):
        super(qtinter,self).__init__()
        
        # set up main window
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Fispact output reviewer')    
        #self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.statusBar()
        self.setup_actions_menus()
        
        # main widgets 
        
        central_wid = QtGui.QWidget()
        
        # sort main layouts
        vbox1 = QtGui.QVBoxLayout(central_wid)     
        hbox1 = QtGui.QHBoxLayout()
        
        self.setCentralWidget(central_wid)        
        self.show()

    def setup_actions_menus(self):
        
        # set up actions
        exitAction = QtGui.QAction('Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit, Quit, leave, runaway')       
        exitAction.triggered.connect(self.close)
        
        aboutAction = QtGui.QAction('About',self)
        aboutAction.setStatusTip('A little bit about the program')
        
        
        read_output_action = QtGui.QAction('Open Output file', self)
        read_output_action.setStatusTip('Open Fispact-II output file')
        read_output_action.triggered.connect(self.open_file_pressed)

        plot_inv_action = QtGui.QAction('Plot Inventory', self)
        plot_inv_action.setStatusTip('plot inventory at timestep')
        plot_inv_action.triggered.connect(self.plot_inv_pressed)

        plot_act_action = QtGui.QAction('Plot lifetime parameters', self)
        plot_act_action.setStatusTip('Plot parameters')
        plot_act_action.triggered.connect(self.plot_act_pressed)

        plot_dominant_action = QtGui.QAction('Plot Dominant', self)
        plot_dominant_action.setStatusTip('Plot dominant nuclides at timestep')
        plot_dominant_action.triggered.connect(self.plot_dom_pressed)

        plot_spectra_action = QtGui.QAction('Plot gamma spectra', self)
        plot_spectra_action.setStatusTip('Plot gamma spectra at timestep')
        plot_spectra_action.triggered.connect(self.plot_spectra_pressed)

        # sort out menu bar
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(aboutAction)        
        
        analysisMenu = menuBar.addMenu('&Analysis')
        analysisMenu.addAction(read_output_action)
        analysisMenu.addAction(plot_inv_action)
        analysisMenu.addAction(plot_act_action)
        analysisMenu.addAction(plot_dominant_action)
        analysisMenu.addAction(plot_spectra_action)

    def closeEvent(self, event):
        
        # confirm to close 
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you really sure you want quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def open_file_pressed(self):
        """ """
        fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open output file', '.')
        fo = fispact.read_fis_out(fname)


    def plot_inv_pressed(self):
        """ """


    def plot_act_pressed(self):
        """ """


    def plot_dom_pressed(self):
        """ """


    def plot_spectra_pressed(self):
        """ """

    
    
def main():
    qt_app = QtGui.QApplication(sys.argv)
    ex = qtinter()
    ex.show()
    sys.exit(qt_app.exec_())


if __name__ ==  '__main__':
    main()




