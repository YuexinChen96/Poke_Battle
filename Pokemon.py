

MP_MAX = 100
class Pokemon():


	def __init__(self, x, y, pid, uid):
		self.x = x
		self.y = y
		self.pid = pid
		self.setupPokemon(pid)
		self.cur_HP = self.HP
		self.cur_MP = 0
		self.uid = uid

	def setupPokemon(self, pid):
		# pi ka qiu
		if pid == 0:
			self.attack = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'elec'
			self.type2 = 'normal'

		# jie ni gui
		if pid == 1:
			self.attack = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'water'
			self.type2 = 'normal'

		# xiao huo long
		if pid == 2:
			self.attack = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'fire'
			self.type2 = 'normal'

		# miao wa zhong zi
		if pid == 3:
			self.attack = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'grass'
			self.type2 = 'normal'

		# ka bi shou
		if pid == 4:
			self.attack = 30
			self.defence = 23
			self.HP = 340
			self.MP = 0
			self.type = 'normal'
			self.type2 = 'normal'

		# tu tou long
		if pid == 5:
			self.attack = 48
			self.dattack = 48
			self.defence = 10
			self.HP = 228
			self.MP = 0
			self.type = 'dragon'
			self.type2 = 'normal'

		# du she
		if pid == 6:
			self.attack = 30
			self.defence = 12
			self.HP = 238
			self.MP = 0
			self.type = 'poison'
			self.type2 = 'normal'

		# zhen fu pai pai
		if pid == 7:
			self.attack = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'elec'
			self.type2 = 'normal'

		# bi diao
		if pid == 8:
			self.attack = 46
			self.defence = 17
			self.HP = 200
			self.MP = 0
			self.type = 'fly'
			self.type2 = 'normal'

		# pang ding
		if pid == 9:
			self.attack = 30
			self.defence = 15
			self.HP = 250
			self.MP = 0
			self.type = 'fairy'
			self.type2 = 'normal'

		# gu la duo
		if pid == 10:
			self.attack = 55
			self.defence = 29
			self.HP = 420
			self.MP = 0
			self.type = 'fire'
			self.type2 = 'normal'

		# hai huang ya
		if pid == 11:
			self.attack = 55
			self.defence = 29
			self.HP = 420
			self.MP = 0
			self.type = 'water'
			self.type2 = 'normal'

		# tian kong long
		if pid == 12:
			self.attack = 50
			self.dattack = 50
			self.defence = 17
			self.HP = 340
			self.MP = 0
			self.type = 'dragon'
			self.type2 = 'fly'

		# luo qi ya
		if pid == 13:
			self.attack = 59
			self.defence = 20
			self.HP = 390
			self.MP = 0
			self.type = 'water'
			self.type2 = 'fly'

		# lei jing ling
		if pid == 14:
			self.attack = 45
			self.defence = 24
			self.HP = 340
			self.MP = 0
			self.type = 'elec'
			self.type2 = 'normal'

		# kuai long
		if pid == 15:
			self.attack = 52
			self.dattack = 52
			self.defence = 27
			self.HP = 400
			self.MP = 0
			self.type = 'elec'
			self.type2 = 'dragon'

		# mei na si
		if pid == 16:
			self.attack = 48
			self.defence = 22
			self.HP = 350
			self.MP = 0
			self.type = 'water'
			self.type2 = 'fairy'

		# feng huang
		if pid == 17:
			self.attack = 59
			self.defence = 20
			self.HP = 390
			self.MP = 0
			self.type = 'fire'
			self.type2 = 'fly'

		# xue la bi
		if pid == 18:
			self.attack = 45
			self.defence = 20
			self.HP = 340
			self.MP = 0
			self.type = 'grass'
			self.type2 = 'fairy'

		# ji la qi
		if pid == 19:
			self.attack = 45
			self.defence = 20
			self.HP = 340
			self.MP = 0
			self.type = 'star'
			self.type2 = 'star'

		

