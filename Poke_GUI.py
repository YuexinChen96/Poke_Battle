import sys, random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Pokemon import Pokemon

root3 = pow(3, 0.5) # root 3
root6 = pow(6, 0.5) # root 6

spring = [[0, 5], [19, 4]]
fire = [[10, 5]]
firer = [[8, 5], [9, 4], [9, 5], [11, 4], [11, 5], [12, 5]]
water = [[0,4],[1,4],[2,5],[3,5],[4,6],[5,6],[6,7],[7,7],[8,8],[9,8],[10,9],[11,9],[12,9],[13,8],[14,8],[15,7],[16,7],[17,6],[18,6],[19,5],
[18,5],[17,4],[16,4],[15,3],[14,3],[13,2],[12,2],[11,1],[10,1],[9,0],[8,0],[7,0],[6,1],[5,1],[4,2],[3,2],[2,3],[1,3]]
telepot = [[0,9],[19,0]]
s_void = [[0,0],[1,0],[2,0],[19,9],[18,9],[17,9],[3,0],[4,1],[16,9],[15,8]]

class Poke_GUI(QWidget):
	# for drawing
	Play1_Pokemons = []
	Play2_Pokemons = []
	# for logic store
	P1P = []
	P2P = []
	# selected pokemon
	select_poke = False
	target_poke = None

	# check each pokemon moved
	moved = []
	move, spell1, spell2, ulti = False, False, False, False
	p1uid = []
	water_extra = []

	def __init__(self):
		super().__init__()
		QtWidgets.QWidget.__init__(self)
		self.initUI()
		self.page = 0
		self.map = [['0' for x in range(10)] for y in range(20)]
		self.tree = []
		# game related
		self.turn = 0


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
		p.drawRect(150, 790, 80, 80)
		p.drawRect(300, 800, 120, 60)
		p.drawText(320, 840, 'Hold')
		p.drawRect(500, 800, 120, 60)
		p.drawText(520, 840, 'Spell')
		p.drawRect(700, 800, 120, 60)
		p.drawText(720, 840, 'Spell_')
		p.drawRect(900, 800, 120, 60)
		p.drawText(920, 840, '*Ulti*')
		p.drawText(1300, 840, str(self.turn) + ' Round')
		if self.select_poke:
			pimg = QPixmap('Pics/pic' + str(self.target_poke.pid) + '.jpg')
			p.drawPixmap(QRect(150, 790, 80, 80), pimg)


		# draw Pokemons on Map
		for i in self.P1P:
			x, y = self.indexToPos(i.x, i.y)
			self.drawPokemon(x, y, 40, p, 'Pics/pic' + str(i.pid) + '.jpg')
		for i in self.P2P:
			x, y = self.indexToPos(i.x, i.y)
			self.drawPokemon(x, y, 40, p, 'Pics/pic' + str(i.pid) + '.jpg')

		# draw Pokemons Infos
		n = 130
		for i in range(6):
			p.setFont(QFont("Arial", 12))
			p.setBrush(QColor(255, 255, 255))
			if i > 2:
				pkmn = self.P2P[i - 3]
				p.drawText(1240, 60 + n * i, 'Play2 Pokemon' + str(i - 2))
			else:
				pkmn = self.P1P[i]
				p.drawText(1240, 60 + n * i, 'Play1 Pokemon' + str(i + 1))
			p.drawRect(1400, 30 + n * i, 40, 40)
			p.drawRect(1240, 80 + n * i, 200, 5)
			p.drawRect(1240, 100 + n * i, 200, 5)
			p.setFont(QFont("Arial", 7))
			p.drawText(1448, 85 + n * i, str(pkmn.cur_HP) + '/' + str(pkmn.HP))
			p.drawText(1448, 105 + n * i, str(pkmn.cur_MP) + '/100' )
			p.drawText(1240, 120 + n * i, str(pkmn.attack))
			p.drawText(1260, 120 + n * i, str(pkmn.defence))
			pimg = QPixmap('Pics/pic' + str(pkmn.pid) + '.jpg')
			p.drawPixmap(QRect(1400, 30 + n * i, 40, 40 ), pimg)
			p.setBrush(QColor(255, 0, 0))
			p.drawRect(1240, 80 + n * i, 200 * pkmn.cur_HP / pkmn.HP, 5)
			p.setBrush(QColor(0, 0, 255))
			p.drawRect(1240, 100 + n * i, 200 * pkmn.cur_MP / 100, 5)
			if pkmn.uid in self.moved:
				p.setBrush(QColor(255, 0, 0))
			else:
				p.setBrush(QColor(255, 255, 255))
			p.drawRect(1460, 46 + n * i, 8, 8)

	# generate water, tree, springs
	def init_logical_Graph(self):
		while(len(self.tree) < 60):
			x = int(random.random() * 20)
			y = int(random.random() * 10)
			if [x, y] not in spring and [x, y] not in fire and [x, y] not in telepot and [x, y] not in s_void and [x, y] not in self.tree and [x, y] not in water and [x, y] not in firer:
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
		for i in firer:
			self.map[i[0]][i[1]] = 'firer'
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
				self.P1P.append(Pokemon(1, 0, self.Play1_Pokemons[0][1] * 10 + self.Play1_Pokemons[0][0], 1))
				self.P1P.append(Pokemon(2, 0, self.Play1_Pokemons[1][1] * 10 + self.Play1_Pokemons[1][0], 2))
				self.P1P.append(Pokemon(0, 0, self.Play1_Pokemons[2][1] * 10 + self.Play1_Pokemons[2][0], 3))
				self.P2P.append(Pokemon(18, 9, self.Play2_Pokemons[0][1] * 10 + self.Play2_Pokemons[0][0], 4))
				self.P2P.append(Pokemon(17, 9, self.Play2_Pokemons[1][1] * 10 + self.Play2_Pokemons[1][0], 5))
				self.P2P.append(Pokemon(19, 9, self.Play2_Pokemons[2][1] * 10 + self.Play2_Pokemons[2][0], 6))
				for i in self.P1P:
					self.p1uid.append(i.uid)
			# Page 3: Map and Algo
			elif self.page == 2:
				# check click points
				point = self.posToIndex(x, y)
				# click on Pokemons
				if not self.select_poke:
					for i in self.P1P:
						if point[0] == i.x and point[1] == i.y:
							self.select_poke = True
							self.target_poke = i
					for i in self.P2P:
						if point[0] == i.x and point[1] == i.y:
							self.select_poke = True
							self.target_poke = i
				else:
					another_flag = False
					for i in self.P1P:
						if point[0] == i.x and point[1] == i.y:
							another_flag = True
							self.target_poke = i
							self.move, self.spell1, self.spell2, self.ulti = False, False, False, False
					for i in self.P2P:
						if point[0] == i.x and point[1] == i.y:
							another_flag = True
							self.target_poke = i
							self.move, self.spell1, self.spell2, self.ulti = False, False, False, False
					p1finish = True
					for i in self.p1uid:
						if i not in self.moved:
							p1finish = False
					if another_flag or self.checkButtonClick(x, y):
						pass
					elif (self.move or self.spell1 or self.spell2 or self.ulti) and ((self.target_poke.uid in self.p1uid and not p1finish) or p1finish) and self.target_poke.uid not in self.moved:
						if self.move:
							pass
							
					
					# short case for movement
					elif self.checkMovement(point[0], point[1]) and ((self.target_poke.uid in self.p1uid and not p1finish) or p1finish) and self.target_poke.uid not in self.moved:
						self.movePokemon(point[0], point[1])
						self.attackEnemy()


			if len(self.moved) == 6:
				self.moved = []
				self.turn = self.turn + 1
				self.water_extra = []
				for a in self.P1P:
					self.endOfRound(a, self.P1P)
				for a in self.P2P:
					self.endOfRound(a, self.P2P)


			# reload page
			self.update()


	# execute the movement
	def movePokemon(self, x, y):
		if (self.target_poke.type == 'water' or self.target_poke.type2 == 'water') and self.target_poke.uid not in self.water_extra and self.turn % 2 == 0 and (self.map[self.target_poke.x][self.target_poke.y] == 'water' or self.map[x][y] == 'water'):
			self.target_poke.x = x
			self.target_poke.y = y
			self.water_extra.append(self.target_poke.uid)
		else:
			self.target_poke.x = x
			self.target_poke.y = y
			self.moved.append(self.target_poke.uid)

	# check next position legal or not
	def checkMovement(self, x, y):
		if self.checkAdjacent(x, y, self.target_poke.x, self.target_poke.y):
			if [x, y] not in spring and [x, y] not in telepot and [x, y] not in fire:
				if self.target_poke.type != 'fly' and self.target_poke.type2 != 'fly' and [x, y] in self.tree:
					return False
				else:
					return True


	def checkAdjacent(self, x, y, x_c, y_c):
		if x_c % 2 == 0:
			if [x, y] in [[x_c - 1, y_c - 1], [x_c - 2, y_c], [x_c - 1, y_c], [x_c + 1, y_c - 1], [x_c + 1, y_c], [x_c + 2, y_c]]:
				return True
			else:
				return False
		if x_c % 2 == 1:
			if [x, y] in [[x_c - 1, y_c], [x_c - 2, y_c], [x_c - 1, y_c + 1], [x_c + 1, y_c], [x_c + 2, y_c], [x_c + 1, y_c + 1]]:
				return True
			else:
				return False

	def attackEnemy(self):
		if self.target_poke.uid in self.p1uid:
			tar = self.P2P
		else:
			tar = self.P1P
		my = self.target_poke
		if self.target_poke.type == 'elec' or self.target_poke.type2 == 'elec':
			elec_list = []
			for a in range(2):
				for b in tar:
					if b.uid not in elec_list:
						if self.dmgCal(my, b) != 100:
							elec_list.append(b.uid)
							break
		else:
			for b in tar:
				if self.dmgCal(my, b) != 100:
					break



	def dmgCal(self, my, tar):
		if self.checkAdjacent(tar.x, tar.y, my.x, my.y):
			tar.cur_HP = tar.cur_HP - (my.attack - tar.defence)
			if my.cur_MP + 4 > 100:
				my.cur_MP = 100
			else:
				my.cur_MP = my.cur_MP + 4
			return tar.uid
		else:
			return 100

	def useSpell1(self, x, y):
		print("Using Spell_1")



	def endOfRound(self, i, dra):
		spring_range = [[1, 4], [1, 5], [2, 5], [17, 4], [18, 4], [18, 5]]
		# fire dmg
		if [i.x, i.y] in firer and i.type != 'fire' and i.type2 != 'fire':
			i.cur_HP = i.cur_HP - 40
		# spring effect
		if [i.x, i.y] in spring_range:
			if i.cur_HP + 10 > i.HP:
				i.cur_HP = i.HP
			else:
				i.cur_HP = i.cur_HP + 10
		# telepot effect
		if [i.x, i.y] == [0, 9]:
			i.x, i.y = 19, 0
		if [i.x, i.y] == [19,0]:
			i.x, i.y = [0, 9]
		# grass effect
		if i.type == 'grass' or i.type2 == 'grass':
			r = int(random.random() * 4)
			if i.cur_HP + r > i.HP:
				i.cur_HP = i.HP
			else:
				i.cur_HP = i.cur_HP + r
		# fairy recover
		if i.type == 'fairy' or i.type2 == 'fairy':
			if i.cur_MP + 4 > 100:
				i.cur_MP = 100
			else:
				i.cur_MP = i.cur_MP + 4
		# dragon effect
		if i.type == 'dragon' or i.type2 == 'dragon':
			dra_flag = False
			for a in dra:
				if self.checkAdjacent(a.x, a.y, i.x, i.y):
					dra_flag = True
					i.attack = i.dattack + 15
			if not dra_flag:
				i.attack = i.dattack
		# final MP recover
		if i.cur_MP + 4 > 100:
			i.cur_MP = 100
		else:
			i.cur_MP = i.cur_MP + 4



	# check which button is clicked
	def checkButtonClick(self, x, y):
		flag = False
		if x > 300 and x < 420 and y > 800 and y < 860:
			self.attackEnemy()
			self.moved.append(self.target_poke.uid)
			flag = True
		elif x > 500 and x < 620 and y > 800 and y < 860:
			self.move, self.spell1, self.spell2, self.ulti = False, True, False, False
			flag = True
		elif x > 700 and x < 820 and y > 800 and y < 860:
			self.move, self.spell1, self.spell2, self.ulti = False, False, True, False
			flag = True
		elif x > 900 and x < 1020 and y > 800 and y < 860:
			self.move, self.spell1, self.spell2, self.ulti = False, False, False, True
			flag = True
		return flag	

	# two Page 3 helper functions
	def posToIndex(self, x, y):
		x_start = 40 - 10 * root6
		y_ = 40 * root3 # height of polygon
		if x > 1200 + x_start or y > 10.5 * y_:
			return [30,30]
		else:
			r_x = int((x - x_start) / 60)
			if r_x % 2 == 0:
				r_y = int(y / y_)
				return [2 * r_y, int(r_x / 2)]
			elif r_x % 2 == 1:
				r_y = int((y - 0.5 * y_) / y_)
				return [2 * r_y + 1, int(r_x / 2)]

	# two Page 3 helper functions
	def indexToPos(self, x, y):
		if x > 19 or y > 19 or x < 0 or y < 0:
			return 0, 0
		else:
			if x % 2 == 0:
				return 20 + y * 120, 40 * root3 * x / 2
			elif x % 2 == 1:
				return 80 + y * 120, 40 * root3 * (int(x / 2) + 0.5)


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