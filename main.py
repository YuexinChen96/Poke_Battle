import sys, time
from PyQt5.QtWidgets import QApplication, QMainWindow

import Poke_GUI


if __name__ == '__main__':

	app = QApplication(sys.argv)
	ui = Poke_GUI.Poke_GUI() 
	ui.show()

	
	sys.exit(app.exec_())