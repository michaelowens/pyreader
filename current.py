import feedparser
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow

class PyReaderProgram(Ui_MainWindow):
  def __init__(self, dialog):
    Ui_MainWindow.__init__(self)
    self.setupUi(dialog)

    # Connect "add" button with a custom function (addInputTextToListbox)
    self.pushButton.clicked.connect(self.addInputTextToListbox)

    self.loadData()

  def addInputTextToListbox(self):
    txt = "hello again"
    self.listWidget.addItem(txt)

  def loadData(self):
    d = feedparser.parse('http://www.reddit.com/r/python/.rss')
    for post in d.entries:
      self.listWidget.addItem(post.title + ": " + post.link)
      self.treeWidget.addTopLevelItem(QtWidgets.QTreeWidgetItem([post.author, post.title]))

if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  dialog = QtWidgets.QMainWindow()

  prog = PyReaderProgram(dialog)

  dialog.show()
  sys.exit(app.exec_())