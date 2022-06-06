import sys

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

def run_qml():
	app = QGuiApplication([])

	engine = QQmlApplicationEngine()
	engine.quit.connect(app.quit)
	engine.load('main.qml')
	
	return app.exec_()


if __name__ == "__main__":
	sys.exit(run_qml())