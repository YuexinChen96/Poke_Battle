import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

root3 = pow(3, 0.5) # root 3
root6 = pow(6, 0.5) # root 6

class Poke_GUI(QWidget):

	Play1_Pokemons = []
	Play2_Pokemons = []

	def __init__(self):
		super().__init__()
		QtWidgets.QWidget.__init__(self)
		self.initUI()
		self.page = 0

	def initUI(self):
		self.setGeometry(0, 0, 1500, 900)
		self.setWindowTitle('Pokemon Battle')

	# all drawing logics
	def paintEvent(self, e):
		p = QPainter()
		p.begin(self)
		p.setPen(QColor(0,0,0))
		#Page 1
		if self.page == 0:
			self.Page1_UI(e, p)
		elif self.page == 1:
			self.Page2_UI(e, p)
		elif self.page == 2:
			self.Page3_UI(e, p)
		p.end()

	# Welcome Page
	def Page1_UI(self, e, p):
		p.drawRect(300, 500, 200, 100)
		p.drawRect(700, 500, 200, 100)
		p.setFont(QFont("Arial", 40))
		p.drawText(120, 300, 'Welcome to the Pokemon Battle!')
		p.drawText(330, 570, 'Start')
		p.drawText(745, 570, 'Exit')
		p.setFont(QFont("Arial", 20))
		p.drawText(400, 400, 'Press the start button to start.')

	# Pokemon select page
	def Page2_UI(self, e, p):
		p.setFont(QFont("Arial", 20))
		p.drawText(100, 100, 'Select three Pokemons to Fight!')

		# draw Polygon
		for a in range(10):
			for b in range(2):
				n = 10 * b + a
				self.drawPokemon(40 + a * 120, 200 + b * 100, 50, p, 'Pics/pic' + str(n) + '.jpg')
				self.drawPolygonByPos(40 + a * 120, 200 + b * 100, 50, p)
				
		# selected Pokemon
		p.drawText(40, 680, 'Player 1')
		p.drawText(880, 680, 'Player 2')
		for a in range(3):
			self.drawPolygonByPos(40 + a * 120, 700, 50, p)
			self.drawPolygonByPos(880 + a * 120, 700, 50, p)
		counter = 0
		# draw Player 1 Pokemon
		for i in self.Play1_Pokemons:
			n = i[1] * 10 + i[0]
			self.drawPokemon(40 + counter * 120, 700, 50, p, 'Pics/pic' + str(n) + '.jpg')
			counter = counter + 1
		counter = 0
		# draw Player 2 Pokemon
		for i in self.Play2_Pokemons:
			n = i[1] * 10 + i[0]
			self.drawPokemon(880 + counter * 120, 700, 50, p, 'Pics/pic' + str(n) + '.jpg')
			counter = counter + 1

		# start buttons
		p.drawText(520, 640, 'Start')
		p.drawRect(500, 600, 110, 60)

	# Map UI
	def Page3_UI(self, e, p):
		#draw the map
		self.Mapping(e, p)
		

	def Mapping(self, e, p):
		# Basic Polygons
		for a in range(10):
			for b in range(2):
				for c in range(10):
					if b == 0:
						self.drawPolygonByPos(20 + c * 120, a * 40 * root3, 40, p)
					elif b == 1:
						self.drawPolygonByPos(80 + c * 120, 20 * root3 + a * 40 * root3, 40, p)



	# buttons click events - UI part
	def mousePressEvent(self, e):
		# left click event
		if e.buttons() == QtCore.Qt.LeftButton:
			# get x, y pos
			x = e.x()
			y = e.y()
			# Page 1: start button
			if self.page == 0 and x > 300 and x < 500 and y > 500 and y < 600:
				self.page = 1

			# Page 2: select Pokemons
			# boardary 40, 1120 + 50, 200, ----------------------------------------------need change if more pokemons
			if self.page == 1 and x > 40 and x < 1170 and y > 200 and y < 300 + 50 * root3:
				# click on pokemons
				i_x, i_y = int((x - 40) / 120), int((y - 200) / 100)
				if len(self.Play1_Pokemons) < 3 and [i_x, i_y] not in self.Play1_Pokemons:
					self.Play1_Pokemons.append([i_x, i_y]) #---------------------------------need more logical
				elif len(self.Play1_Pokemons) == 3 and [i_x, i_y] not in self.Play2_Pokemons and len(self.Play2_Pokemons) < 3:
					self.Play2_Pokemons.append([i_x, i_y])
			elif self.page == 1 and x > 40 and x < 330 and y > 700 and y < 700 + 50 * root3:
				i_x = int((x - 40) / 120)
				if (i_x < len(self.Play1_Pokemons)):
					self.Play1_Pokemons.pop(i_x)
			elif self.page == 1 and x > 880 and x < 1170 and y > 700 and y < 700 + 50 * root3:
				i_x = int((x - 880) / 120)
				if (i_x < len(self.Play2_Pokemons)):
					self.Play2_Pokemons.pop(i_x)
			#start the game
			elif self.page == 1 and len(self.Play1_Pokemons) == 3 and len(self.Play2_Pokemons) == 3 and x > 500 and x < 610 and y < 660 and y > 600:
				self.page = 2

			# Page 3: Map and Algo



			# reload page
			self.update()

	# x, y: pos
	# l: length, p: painter
	def drawPolygonByPos(self, x, y, l, p):
		polygon = QPolygon()
		polygon.setPoints(x, y, x + l, y, x + 1.5 * l, y + 0.5 * root3 * l, x + l, y + l * root3, x, y + l * root3, x - 0.5 * l, y + 0.5 * root3 * l)
		p.drawPolygon(polygon)

	# similar to above / img: img_dir
	def drawPokemon(self, x, y, l, p, img):
		pimg = QPixmap(img)
		y_off = root3 / 2 - root6 / 4
		area = QRect(x - (root6 - 2) / 4 * l, y + y_off * l, l * root6 / 2, l * root6 / 2)
		p.drawPixmap(area, pimg)