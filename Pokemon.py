

MP_MAX = 100
class Pokemon():


	def __init__(self, x, y, pid, uid):
		self.x = x
		self.y = y
		self.pid = pid
		self.cur_MP = 100
		self.uid = uid
		self.fire_mark = False
		self.poison_mark = 1
		self.poison_dmg = 10
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
			self.attack = 35
			self.defence = 23
			self.HP = 340
			self.MP = 0
			self.type = 'normal'
			self.type2 = 'normal'
			self.name1 = '直冲拳'
			self.name2 = '强化'
			self.name3 = '睡觉'

			self.ult = False
			self.cur_turn = 0

		# tu tou long
		if pid == 5:
			self.attack = 48
			self.dra_att = 48
			self.defence = 10
			self.HP = 228
			self.MP = 0
			self.type = 'dragon'
			self.type2 = 'normal'
			self.name1 = '龙爪'
			self.name2 = '恐惧颜'
			self.name3 = '龙之虹吸'
			

		# du she
		if pid == 6:
			self.attack = 35
			self.defence = 12
			self.HP = 238
			self.MP = 0
			self.type = 'poison'
			self.type2 = 'normal'
			self.name1 = '毒镖'
			self.name2 = '魔法震荡'
			self.name3 = '毒箭'

		# zhen fu pai pai
		if pid == 7:
			self.attack = 40
			self.defence = 15
			self.HP = 238
			self.MP = 0
			self.type = 'elec'
			self.type2 = 'normal'
			self.name1 = '正负交换'
			self.name2 = '交接棒'
			self.name3 = '紧密节奏'

		# bi diao
		if pid == 8:
			self.attack = 46
			self.defence = 17
			self.HP = 200
			self.MP = 0
			self.type = 'fly'
			self.type2 = 'normal'
			self.name1 = '急速折返'
			self.name2 = '羽栖'
			self.name3 = '神鸟猛击'

		# pang ding
		if pid == 9:
			self.attack = 35
			self.defence = 15
			self.HP = 250
			self.MP = 0
			self.type = 'fairy'
			self.type2 = 'normal'
			self.name1 = '赞美之声'
			self.name2 = '悦耳之声'
			self.name3 = '睡眠之声'

		# gu la duo
		if pid == 10:
			self.attack = 55
			self.defence = 29
			self.HP = 420
			self.MP = 0
			self.type = 'fire'
			self.type2 = 'normal'
			self.name1 = '火之牙'
			self.name2 = '岩浆领域'
			self.name3 = '地震'

		# hai huang ya
		if pid == 11:
			self.attack = 55
			self.defence = 29
			self.HP = 420
			self.MP = 0
			self.type = 'water'
			self.type2 = 'normal'
			self.name1 = '热水'
			self.name2 = '海潮领域'
			self.name3 = '水之牢笼'

		# tian kong long
		if pid == 12:
			self.attack = 50
			self.dra_att = 50
			self.defence = 17
			self.HP = 340
			self.MP = 0
			self.type = 'dragon'
			self.type2 = 'fly'
			self.name1 = '龙之吐息'
			self.name2 = '帝王之怒'
			self.name3 = '龙星群'

			self.spell_extra = 0
		# luo qi ya
		if pid == 13:
			self.attack = 59
			self.defence = 20
			self.HP = 390
			self.MP = 0
			self.type = 'water'
			self.type2 = 'fly'
			self.name1 = '水之波动'
			self.name2 = '自我再生'
			self.name3 = '飓风'

		# lei gong
		if pid == 14:
			self.attack = 55
			self.defence = 25
			self.HP = 420
			self.MP = 0
			self.type = 'elec'
			self.type2 = 'normal'
			self.name1 = '雷电锁定'
			self.name2 = '电网'
			self.name3 = '雷公神柱'

		# kuai long
		if pid == 15:
			self.attack = 52
			self.dra_att = 52
			self.defence = 30
			self.HP = 460
			self.MP = 0
			self.type = 'fly'
			self.type2 = 'dragon'
			self.name1 = '舍身攻击'
			self.name2 = '龙焰'
			self.name3 = '龙之战歌'

		# cao ci wei
		if pid == 16:
			self.attack = 48
			self.defence = 22
			self.HP = 350  
			self.MP = 0
			self.type = 'grass'
			self.type2 = 'fairy'
			self.name1 = '芳草气息'
			self.name2 = '振奋'
			self.name3 = '花团锦簇'

		# feng huang
		if pid == 17:
			self.attack = 59
			self.defence = 20
			self.HP = 390
			self.MP = 0
			self.type = 'fire'
			self.type2 = 'fly'
			self.name1 = '焚烧殆尽'
			self.name2 = '五彩斑斓'
			self.name3 = '浴血重生'

			self.ult = False
			self.once = False

		# xue la bi
		if pid == 18:
			self.attack = 45
			self.defence = 20
			self.HP = 340
			self.MP = 0
			self.type = 'grass'
			self.type2 = 'fairy'
			self.name1 = '空间跳跃'
			self.name2 = '疯狂生长'
			self.name3 = '时空裂缝'

		# ji la qi
		if pid == 19:
			self.attack = 45
			self.defence = 20
			self.HP = 340
			self.MP = 0
			self.type = 'normal'
			self.type2 = 'star'
			self.name1 = '祈愿星'
			self.name2 = '彗星'
			self.name3 = '行星咏叹'

		

