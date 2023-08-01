import sys
from custome_errors import *
sys.excepthook = my_excepthook
import googletrans
from webbrowser import open as openLink
import language
import app
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
language.init_translation()
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(app.name + _("version : ") + str(app.version))
        lang=[]
        for code, name in googletrans.LANGUAGES.items():
            lang.append(name)
        self.text=qt.QLineEdit()
        self.text.setAccessibleName(_("text"))
        self.From=qt.QComboBox()
        self.From.setAccessibleName(_("from"))
        self.From.addItems([_("audo detect")]  + lang)
        self.to=qt.QComboBox()
        self.to.setAccessibleName(_("to"))
        self.to.addItems(lang)
        self.translate=qt.QPushButton(_("translate"))
        self.translate.setDefault(True)
        self.translate.clicked.connect(self.ftranslate)
        self.re=qt.QTextEdit()
        self.re.setReadOnly(True)
        self.re.setAccessibleName(_("result"))
        layout=qt.QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.From)
        layout.addWidget(self.to)
        layout.addWidget(self.translate)
        layout.addWidget(self.re)
        w=qt.QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
        mb=self.menuBar()
        help=mb.addMenu(_("help"))
        cus=help.addMenu(_("contact us"))
        telegram=qt1.QAction("telegram",self)
        cus.addAction(telegram)
        telegram.triggered.connect(lambda:openLink("https://t.me/mesteranasm"))
        telegramc=qt1.QAction(_("telegram channel"),self)
        cus.addAction(telegramc)
        telegramc.triggered.connect(lambda:openLink("https://t.me/tprogrammers"))
        donate=qt1.QAction(_("donate"),self)
        help.addAction(donate)
        donate.triggered.connect(lambda:openLink("https://www.paypal.me/AMohammed231"))
        about=qt1.QAction(_("about"),self)
        help.addAction(about)
        about.triggered.connect(lambda:qt.QMessageBox.information(self,_("about"),_("{} version: {} description: {} developer: {}").format(app.name,str(app.version),app.description,app.creater)))
        self.setMenuBar(mb)
    def ftranslate(self):
        translator = googletrans.Translator()
        if self.From.currentIndex()==0:
            From=translator.detect(self.text.text()).lang
        else:
            From=self.From.currentText()
        try:
            a=translator.translate(self.text.text(),src=From,dest=self.to.currentText()).text
        except:
            a=_("error while translating")
        self.re.setText(a)
        self.re.setFocus()

App=qt.QApplication([])
w=main()
w.show()
App.exec()