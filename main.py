from PyQt5.QtWidgets import  QMainWindow,QApplication,QFileDialog
from PyQt5.uic import loadUi
import sys

class Main(QMainWindow):   #the basic ui window  ---- Inheritance concept
    def __init__(self):         #runs always as it is a basic constructor
        super(Main,self).__init__()
        loadUi("main.ui",self)

        self.current_path= None
        self.current_fontSize=8
        self.setWindowTitle("Untitled")

        self.actionNew.triggered.connect(self.newFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_As.triggered.connect(self.saveFileAs)
        self.actionOpen.triggered.connect(self.OpenFile)
        self.actionUndo.triggered.connect(self.undo)
        self.actionredo.triggered.connect(self.redo)
        self.actionCut.triggered.connect(self.cut)
        self.actionCopy.triggered.connect(self.copy)
        self.actionpaste.triggered.connect(self.paste)
        self.actionSet_Dark_mod.triggered.connect(self.setDarkMode)
        self.actionSet_Light_Mode.triggered.connect(self.setLightMode)
        self.actionIncrease_Font.triggered.connect(self.incFontSize)
        self.actionDecrease_Font.triggered.connect(self.decFontSize)

    def newFile(self):
        print("New file clicked")
        self.edit.clear()  #to clear the text of the editor
        self.setWindowTitle("Untitled")  #to show new file is opened
        self.current_path=None

    def saveFile(self):
        # print("File saved")
        if self.current_path is not None:
            # save changes without opening dialog
            filetext=self.edit.toPlainText()   #basically stores the text of the file
            # print(filetext)
            with open(self.current_path,'w') as f:
                f.write(filetext)
        else:
            self.saveFileAs()

    def saveFileAs(self):
        print("File saved as")
        pathname=QFileDialog.getSaveFileName(self,'Save file','D:\Text-Editor','Text files(*.txt)')
        filetext=self.edit.toPlainText()
        with open(pathname[0],'w') as f:
            f.write(filetext)
        self.setWindowTitle(pathname[0])
        self.current_path=pathname[0]


    def OpenFile(self):
        print("File opened")
        fname=QFileDialog.getOpenFileName(self,'Open File','D:\Text-Editor','Text files(*.txt)')
        self.setWindowTitle(fname[0])   # to know which file is opened
        with open(fname[0],'r') as f:
            filetext=f.read()
            self.edit.setText(filetext)

        self.current_path=fname[0]


    def undo(self):
        print("undo opr")
        self.edit.undo()   #undo comes by default with editor
    def redo(self):
        print("Redo opr")
        self.edit.redo()
    def cut(self):
        print("Cut txt")
        self.edit.cut()
    def copy(self):
        print("copy text")
        self.edit.copy()
    def paste(self):
        print("Paste txt")
        self.edit.paste()
    def setDarkMode(self):
        print("Dark")
        self.setStyleSheet('''QWidget{
            background-color:rgb(33,33,33);
            color:#FFFFFF
            }
            QTextEdit{
            background-color: rgb(46,46,46);
            }
            QMenuBar::item:selected{
            color:#000000
            }  ''')


    def setLightMode(self):
        print("Light")
        self.setStyleSheet("")

    def incFontSize(self):
        print("Font increased")
        self.current_fontSize+=1
        self.edit.setFontPointSize(self.current_fontSize)

    def decFontSize(self):
        print("Font decreased")
        self.current_fontSize-=1
        self.edit.setFontPointSize(self.current_fontSize)




if __name__=="__main__":
    app=QApplication(sys.argv)  #needed to execute
    ui=Main()                   #ui is a instance of Main class we created
    ui.show()
    app.exec_()