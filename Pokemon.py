

MP_MAX = 100
class Pokemon():


	def __init__(self, x, y, pid, uid):
		self.x = x
		self.y = y
		self.pid = pid
		self.cur_MP = 100
		self.uid = uid
		self.fire_mark = False
		self.poison_mark = 0
		self.poison_dmg = 0
		self.fire_turn = 0
		self.fire_dmg = 0
		self.poison_turn = 0
		self.buff_turn = 0
		self.buff_att = 0
		self.buff_def = 0
		self.stun = False

		self.setupPokemon(pid)
		self.cur_HP = self.HP
		self.cur_att = self.attack
		self.cur_def = self.defence


	def setupPokemon(self, pid):
		# pi ka qiu
		if pid == 0:
			self.attack = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'elec'
			self.type2 = 'normal'
			self.name1 = '电击'
			self.name2 = '钢尾'
			self.name3 = '打雷'

		# jie ni gui
		if pid == 1:
			self.attack = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'water'
			self.type2 = 'normal'
			self.name1 = '水炮'
			self.name2 = '求雨'
			self.name3 = '冲浪'

		# xiao huo long
		if pid == 2:
			self.attack = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'fire'
			self.type2 = 'normal'
			self.name1 = '喷射火焰'
			self.name2 = '火焰漩涡'
			self.name3 = '大字火'

		# miao wa zhong zi
		if pid == 3:
			self.attack = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'grass'
			self.type2 = 'normal'
			self.name1 = '藤鞭'
			self.name2 = '种子'
			self.name3 = '阳光烈焰'

			self.ult = False
			self.cur_turn = 0

		# ka bi shou
		if pid == 4:
			self.attack = 30
			self.defence = 23
			self.HP = 340
			self.MP = 0
			self.type = 'normal'
			self.type2 = 'normal'
			self.name1 = '电击'
			self.name2 = '钢尾'
			self.name3 = '打雷'

		# tu tou long
		if pid == 5:
			self.attack = 48
			self.dra_att = 48
			self.defence = 10
			self.HP = 228
			self.MP = 0
			self.type = 'dragon'
			self.type2 = 'normal'
			self.name1 = '电击'
			self.name2 = '钢尾'
			self.name3 = '打雷'
			

		# du she
		if pid == 6:
			self.attack = 30
			self.defence = 12
			self.HP = 238
			self.MP = 0
			self.type = 'poison'
			self.type2 = 'normal'
			self.name1 = '电击'
			self.name2 = '钢尾'
			self.name3 = '打雷'

		# zhen fu pai pai
		if pid == 7:
			self.attack = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'elec'
			self.type2 = 'normal'
			self.name1 = '电击'
			self.name2 = '钢尾'
			self.name3 = '打雷'

		# bi diao
		if pid == 8:
			self.attack = 46
			self.defence = 17
			self.HP = 200
			self.MP = 0
			self.type = 'fly'
			self.type2 = 'normal'
			self.name1 = '电击'
			self.name2 = '钢尾'
			self.name3 = '打雷'

		# pang ding
		if pid == 9:
			self.attack = 30
			self.defence = 15
			self.HP = 250
			self.MP = 0
			self.type = 'fairy'
			self.type2 = 'normal'
			self.name1 = '电击'
			self.name2 = '钢尾'
			self.name3 = '打雷'

		# gu la duo
		if pid == 10:
			self.attack = 55
			self.defence = 29
			self.HP = 420
			self.MP = 0
			self.type = 'fire'
			self.type2 = 'normal'
			self.name1 = '电击'
			self.name2 = '钢尾'
			self.name3 = '打雷'

		# hai huang ya
		if pid == 11:
			self.attack = 55
			self.defence = 29
			self.HP = 420
			self.MP = 0
			self.type = 'water'
			self.type2 = 'normal'
			self.name1 = '电击'
			self.name2 = '钢尾'
			self.name3 = '打雷'

		# tian kong long
		if pid == 12:
			self.attack = 50
			self.dra_att = 50
			self.defence = 17
			self.HP = 340
			self.MP = 0
			self.type = 'dragon'
			self.type2 = 'fly'
			self.name1 = '电击'
			self.name2 = '钢尾'
			self.name3 = '打雷'

		# luo qi ya
		if pid == 13:
			self.attack = 59
			self.defence = 20
			self.HP = 390
			self.MP = 0
			self.type = 'water'
			self.type2 = 'fly'
			self.name1 = '电击'
			self.name2 = '钢尾'
			self.name3 = '打雷'

		# lei jing ling
		if pid == 14:
			self.attack = 45
			self.defence = 24
			self.HP = 340
			self.MP = 0
			self.type = 'elec'
			self.type2 = 'normal'
			self.name1 = '电击'
			self.name2 = '钢尾'
			self.name3 = '打雷'

		# kuai long
		if pid == 15:
			self.attack = 52
			self.dra_att = 52
			self.defence = 27
			self.HP = 400
			self.MP = 0
			self.type = 'elec'
			self.type2 = 'dragon'
			self.name1 = '电击'
			self.name2 = '钢尾'
			self.name3 = '打雷'

		# mei na si
		if pid == 16:
			self.attack = 48
			self.defence = 22
			self.HP = 350
			self.MP = 0
			self.type = 'water'
			self.type2 = 'fairy'
			self.name1 = '电击'
			self.name2 = '钢尾'
			self.name3 = '打雷'

		# feng huang
		if pid == 17:
			self.attack = 59
			self.defence = 20
			self.HP = 390
			self.MP = 0
			self.type = 'fire'
			self.type2 = 'fly'
			self.name1 = '电击'
			self.name2 = '钢尾'
			self.name3 = '打雷'

		# xue la bi
		if pid == 18:
			self.attack = 45
			self.defence = 20
			self.HP = 340
			self.MP = 0
			self.type = 'grass'
			self.type2 = 'fairy'
			self.name1 = '电击'
			self.name2 = '钢尾'
			self.name3 = '打雷'

		# ji la qi
		if pid == 19:
			self.attack = 45
			self.defence = 20
			self.HP = 340
			self.MP = 0
			self.type = 'star'
			self.type2 = 'star'
			self.name1 = '电击'
			self.name2 = '钢尾'
			self.name3 = '打雷'

		

