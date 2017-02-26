from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import sys
from python_org_search import Searcher
from subprocess import Popen


class MainWindow(QMainWindow):
  def __init__(self):
    super(QMainWindow, self).__init__()
    self._TITLE = "DANK MEME FINDER 11/10 IGN \ue420 \ue420 \ue420"
    self.setGeometry (100, 100, 800, 400)
    self.setWindowTitle(self._TITLE)
    self.findButton = QPushButton("FIND THE LATEST \ue41f DANK \ue41f MEMES \ue41f", self)
    self.rateButton = QPushButton("RATE MY MEME (COMING SOON)", self)
    self.imageLabel = QLabel(self)
    self.imageLabel.setScaledContents(True)
    self.findButton.setGeometry(10, 10, 200, 50)
    self.rateButton.setGeometry(10, 200, 200, 50)
    self.imageLabel.setGeometry(220, 0, 400, 400)
    self.findButton.clicked.connect(self.doFind)
    self.show()

  def doFind(self):
    self.findButton.setText("SEARCHING...")
    self.findButton.setEnabled(False)
    bat = Popen("download.bat", cwd=r".")
    stdout, stderr = bat.communicate()
    if bat.returncode == 0:
      Searcher(self).pullImages()

  def saved_a_picture(self, filename):
    self.imageLabel.setPixmap(QPixmap(filename))
    self.imageLabel.repaint()

  def search_done(self):
    self.findButton.setText("FIND THE LATEST \ue41f DANK \ue41f MEMES \ue41f")
    self.findButton.setEnabled(True)

class Main():
  def __init__(self):
    self.app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(self.app.exec_())

Main()
