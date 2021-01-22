import ui
import os
from qunar import GetInfo
from analysis import Analysis
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainProgram(ui.Ui_Form, QWidget):
    def __init__(self):
        super(MainProgram, self).__init__()
        self.ui = ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.query.clicked.connect(self.on_clicked_query)
        self.ui.price.clicked.connect(self.on_clicked_price)
        self.ui.salesVolume.clicked.connect(self.on_clicked_salesVolume)
        self.ui.valueOfSales.clicked.connect(self.on_clicked_valueOfSales)
        self.ui.score.clicked.connect(self.on_clicked_score)
        self.ui.recommendation.clicked.connect(self.on_clicked_recommendation)

    def on_clicked_query(self):

         getinfo = GetInfo()
         getinfo.patch_spider_place('热门景点')
         analysis = Analysis()
         analysis.analysis_sale()
         analysis.analysis_amount()
         analysis.jingqu_pingfen()
         analysis.diqu_mingcheng()
         analysis.analysis_recommend()


    def on_clicked_price(self):


        url = 'file:///C:/Users/Jerrysdragon/Desktop/untitled/热门旅游景点门票价格TOP20.html'
        print(url)
        self.ui.webView.load(QtCore.QUrl(url))


    def on_clicked_salesVolume(self):
        url = 'file:///C:/Users/Jerrysdragon/Desktop/untitled/热门旅游景点门票销量TOP20.html'
        print(url)
        self.ui.webView.load(QtCore.QUrl(url))
        print("销量")

    def on_clicked_valueOfSales(self):
        url = 'file:///C:/Users/Jerrysdragon/Desktop/untitled/热门旅游景点门票销售额TOP20.html'
        print(url)
        self.ui.webView.load(QtCore.QUrl(url))
        print("销售额")

    def on_clicked_score(self):
        url = 'file:///C:/Users/Jerrysdragon/Desktop/untitled/热门旅游景点评分TOP20.html'
        print(url)
        self.ui.webView.load(QtCore.QUrl(url))
        print("评分")

    def on_clicked_recommendation(self):
        url = 'file:///C:/Users/Jerrysdragon/Desktop/untitled/热门旅游景点推荐TOP20.html'
        print(url)
        self.ui.webView.load(QtCore.QUrl(url))
        print("推荐")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainUI = MainProgram()
    mainUI.show()
    sys.exit(app.exec_())