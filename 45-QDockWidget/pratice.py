import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DockDemo(QMainWindow):
    def __init__(self, parent=None):
        super(DockDemo, self).__init__(parent)
        # 设置水平布局
        layout = QHBoxLayout()
        # 实例化菜单栏
        bar = self.menuBar()
        # 创建主菜单file，在其中添加子菜单
        file = bar.addMenu('File')
        file.addAction('New')
        file.addAction('Save')
        file.addAction('quit').triggered.connect(lambda: self.close())
        # 创建QDockWidget窗口（标题，自身窗口）
        self.items = QDockWidget('Dockable', self)

        # 实例化列表窗口，添加几个条目
        self.listWidget = QListWidget()
        for i in range(1, 5):
            self.listWidget.addItem(f'Item{i}')
        # 给每个选项添加点击事件
        self.listWidget.itemClicked.connect(lambda: self.result.setText(self.listWidget.currentItem().text()))

        # 在窗口区域设置QWidget，添加列表控件
        self.items.setWidget(self.listWidget)

        # 设置dock窗口是否可以浮动，True，运行浮动在外面，自动与主界面脱离，False，默认浮动主窗口内，可以手动脱离
        self.items.setFloating(True)

        # 设置QTextEdit为中央小控件
        self.result = QTextEdit()
        self.setCentralWidget(self.result)
        # 将窗口放置在中央小控件的右侧
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)

        self.setLayout(layout)
        self.setWindowTitle('Dock 例子')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DockDemo()
    demo.show()
    sys.exit(app.exec_())
