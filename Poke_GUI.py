import sys, random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

root3 = pow(3, 0.5) # root 3
root6 = pow(6, 0.5) # root 6

spring = [[0, 5], [19, 4]]
fire = [[10, 5]]
water = [[0,4],[1,4],[2,5],[3,5],[4,6],[5,6],[6,7],[7,7],[8,8],[9,8],[10,9],[11,9],[12,9],[13,8],[14,8],[15,7],[16,7],[17,6],[18,6],[19,5],
[18,5],[17,4],[16,4],[15,3],[14,3],[13,2],[12,2],[11,1],[10,1],[9,0],[8,0],[7,0],[6,1],[5,1],[4,2],[3,2],[2,3],[1,3]]
telepot = [[0,9],[19,0]]
s_void = [[0,0],[1,0],[2,0],[19,9],[18,9],[17,9],[9,4],[9,5],[11,4],[11,5],[8,5],[12,5],[3,0],[4,1],[16,9],[15,8]]

class Poke_GUI(QWidget):
	# for drawing
	Play1_Pokemons = []
	Play2_Pokemons = []
	# for logic store
	P1P = []
	P2P = []

	def __init__(self):
		super().__init__()
		QtWidgets.QWidget.__init__(self)
		self.initUI()
		self.page = 0
		self.map = [['0' for x in range(10)] for y in range(20)]
		self.tree = []


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
		self.turn = 0
		

	# draw basic blocks and control buttons
	def Mapping(self, e, p):
		self.init_logical_Graph()

		p.setBrush(QColor(255,255,255))
		# Basic Polygons
		for a in range(10):
			for b in range(2):
				for c in range(10):
					# setup color
					pic_ = self.map[2 * a + b][c]
					# drawBlocks
					if b == 0:
						self.drawPolygonByPos(20 + c * 120, a * 40 * root3, 40, p)
						self.drawPokemon(20 + c * 120, a * 40 * root3, 40, p, 'Pics/' + pic_ + '.jpg')
					elif b == 1:
						self.drawPolygonByPos(80 + c * 120, 20 * root3 + a * 40 * root3, 40, p)
						self.drawPokemon(80 + c * 120, 20 * root3 + a * 40 * root3, 40, p, 'Pics/' + pic_ + '.jpg')
		p.setFont(QFont("Arial", 20))
		p.drawRect(100, 800, 60, 60)
		p.drawRect(300, 800, 120, 60)
		p.drawText(320, 840, 'Move')
		p.drawRect(500, 800, 120, 60)
		p.drawText(520, 840, 'Spell')
		p.drawRect(700, 800, 120, 60)
		p.drawText(720, 840, 'Spell_')
		p.drawRect(900, 800, 120, 60)
		p.drawText(920, 840, '*Ulti*')



	# generate water, tree, springs
	def init_logical_Graph(self):
		while(len(self.tree) < 60):
			x = int(random.random() * 20)
			y = int(random.random() * 10)
			if [x, y] not in spring and [x, y] not in fire and [x, y] not in telepot and [x, y] not in s_void and [x, y] not in self.tree and [x, y] not in water:
				self.tree.append([x, y])
		for i in spring:
			self.map[i[0]][i[1]] = 'spring'
		for i in fire:
			self.map[i[0]][i[1]] = 'fire'
		for i in water:
			self.map[i[0]][i[1]] = 'water'
		for i in telepot:
			self.map[i[0]][i[1]] = 'telepot'
		for i in self.tree:
			self.map[i[0]][i[1]] = 'tree'
		#print(self.map)


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
				#self.P1P.append()
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