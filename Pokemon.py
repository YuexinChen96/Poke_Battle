

MP_MAX = 100
class Pokemon():


	def __init__(self, x, y, pid):
		self.x = x
		self.y = y
		self.pid = pid
		self.setupPokemon(pid)
		self.cur_HP = self.HP

	def setupPokemon(self, pid):
		# pi ka qiu
		if pid == 0:
			self.attach = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'elec'

		# jie ni gui
		if pid == 1:
			self.attach = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'water'

		# xiao huo long
		if pid == 2:
			self.attach = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'fire'

		# miao wa zhong zi
		if pid == 3:
			self.attach = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'grass'

		# ka bi shou
		if pid == 4:
			self.attach = 30
			self.defence = 23
			self.HP = 340
			self.MP = 0
			self.type = 'normal'

		# tu tou long
		if pid == 5:
			self.attach = 48
			self.defence = 10
			self.HP = 228
			self.MP = 0
			self.type = 'dragon'

		# du she
		if pid == 6:
			self.attach = 30
			self.defence = 12
			self.HP = 238
			self.MP = 0
			self.type = 'poison'

		# zhen fu pai pai
		if pid == 7:
			self.attach = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'elec'

		# bi diao
		if pid == 8:
			self.attach = 46
			self.defence = 17
			self.HP = 200
			self.MP = 0
			self.type = 'fly'

		# pang ding
		if pid == 9:
			self.attach = 
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'fairy'

		# gu la duo
		if pid == 10:
			self.attach = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'elec'

		# hai huang ya
		if pid == 11:
			self.attach = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'elec'

		# tian kong long
		if pid == 12:
			self.attach = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'elec'

		# luo qi ya
		if pid == 13:
			self.attach = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'elec'

		# xue yao nv
		if pid == 14:
			self.attach = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'elec'

		# kuai long
		if pid == 15:
			self.attach = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'elec'

		# mei na si
		if pid == 16:
			self.attach = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'elec'

		# cao jing ling
		if pid == 17:
			self.attach = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'elec'

		# xue la bi
		if pid == 18:
			self.attach = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'elec'

		# ji la qi
		if pid == 19:
			self.attach = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'elec'

		

