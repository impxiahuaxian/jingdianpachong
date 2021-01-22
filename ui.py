# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/duan/PycharmProjects/qunar/ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(620, 473)
        self.webView = QtWebEngineWidgets.QWebEngineView(Form)
        self.webView.setGeometry(QtCore.QRect(50, 20, 451, 341))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.query = QtWidgets.QPushButton(Form)
        self.query.setGeometry(QtCore.QRect(240, 400, 89, 25))
        self.query.setObjectName("query")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(530, 40, 85, 311))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.price = QtWidgets.QPushButton(self.widget)
        self.price.setObjectName("price")
        self.verticalLayout.addWidget(self.price)
        self.salesVolume = QtWidgets.QPushButton(self.widget)
        self.salesVolume.setObjectName("salesVolume")
        self.verticalLayout.addWidget(self.salesVolume)
        self.valueOfSales = QtWidgets.QPushButton(self.widget)
        self.valueOfSales.setObjectName("valueOfSales")
        self.verticalLayout.addWidget(self.valueOfSales)
        self.score = QtWidgets.QPushButton(self.widget)
        self.score.setObjectName("score")
        self.verticalLayout.addWidget(self.score)
        self.recommendation = QtWidgets.QPushButton(self.widget)
        self.recommendation.setObjectName("recommendation")
        self.verticalLayout.addWidget(self.recommendation)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.query.setText(_translate("Form", "开始查询"))
        self.price.setText(_translate("Form", "门票价格"))
        self.salesVolume.setText(_translate("Form", "门票销量"))
        self.valueOfSales.setText(_translate("Form", "门票销售额"))
        self.score.setText(_translate("Form", "景点评分"))
        self.recommendation.setText(_translate("Form", "景点推荐"))

if __name__ == '__main__':
    import sys
    ui = Ui_Form()
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())