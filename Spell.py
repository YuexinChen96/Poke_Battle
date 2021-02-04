import copy
import Poke_GUI

def rangeCal(x, y, n):
	if n == 1:
		if x % 2 == 0:
			return [[x - 1,y - 1],[x - 2,y],[x - 1,y],[x + 1,y - 1],[x + 1,y],[x + 2,y]]
		if x % 2 == 1:
			return [[x - 1, y],[x - 2, y],[x + 1, y],[x + 2,y],[x - 1,y + 1],[x + 1,y + 1]]
	if n == 2:
		l = []
		for i in range(x - 4, x + 5):
			l.append([i,y])
		if x % 2 == 0:
			for i in range(x - 3, x + 4):
				l.append([i,y - 1])
			l = l + [[x-2,y+1],[x,y+1],[x+2,y+1]]
		if x % 2 == 1:
			for i in range(x - 3, x + 4):
				l.append([i, y + 1])
			l = l + [[x-2,y-1],[x,y-1],[x+2,y-1]]
		return l
	if n == 3:
		l = []
		for i in range(x - 6, x + 7):
			l.append([i,y])
		if x % 2 == 0:
			for i in range(x - 4, x + 5):
				l.append([i,y+1])
			for i in range(x - 5, x + 6):
				l.append([i,y-1])
			l = l + [[x-3,y-2],[x-1,y-2],[x+1,y-2],[x+3,y-2]]
		if x % 2 == 1:
			for i in range(x - 4, x + 5):
				l.append([i,y-2])
			for i in range(x - 5, x + 6):
				l.append([i,y+1])
			l = l + [[x-3,y+2],[x-1,y+2],[x+1,y+2],[x+3,y+2]]
		return l


# MP HP calculate
# iod: increase or decrease / 0 for decrease / 1 for increase
def MHCal(tar, iod, n, full):
	if iod == 0 and tar > n:
		return tar - n
	elif iod == 0 and tar < n:
		return 0
	elif iod == 1 and tar + n > full:
		return full
	elif iod == 1 and tar + n < full:
		return tar + n



# m_p is package of pokemon / tar is index of click
def id1_spell(P1P, P2P, m_p, tar, t, moved):
	# check hit on target
	if m_p.uid < 4:
		enemy = copy.copy(P2P)
	else:
		enemy = copy.copy(P1P)
	tar_on = False
	for i in enemy:
		if tar[0] == i.x and tar[1] == i.y:
			tar_poke = i
			tar_on = True
			print("hit on")

	# 0 spell 1
	if t == 1:
 		# check mana range hit on
 		if tar in rangeCal(m_p.x, m_p.y, 2) and m_p.cur_MP >= 20 and tar_on:
 			dmg = 60
 			cur_pos = [m_p.x, m_p.y]
 			nt = find_next(cur_pos, enemy, 2)
 			while nt:
 				# reduce HP
 				nt.cur_HP = MHCal(nt.cur_HP, 0, belowZero(dmg - nt.cur_def), nt.HP)
 				# next replace current position
 				cur_pos = [nt.x, nt.y]
 				# enemy remove that one
 				enemy.remove(nt)
 				print('hit --- ' + str(nt.pid) + "   " + str(dmg) + "HP")
 				# reduce dmg
 				dmg = dmg - 15

 				nt = find_next(cur_pos, enemy, 1)
 			m_p.cur_MP = MHCal(m_p.cur_MP, 0, 20, 100)
 			moved.append(m_p.uid)

	elif t == 2:
		if tar in rangeCal(m_p.x, m_p.y, 2) and m_p.cur_MP >= 20 and tar_on:
			dmg = 40
			tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, belowZero(dmg - tar_poke.cur_def), tar_poke.HP)
			m_p.buff_turn = 3
			m_p.buff_def = 5
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, 20, 100)
			moved.append(m_p.uid)

	elif t == 3:
		if tar in rangeCal(m_p.x, m_p.y, 2) and m_p.cur_MP >= 80 and tar_on:
			dmg = 120
			tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, belowZero(dmg - tar_poke.cur_def), tar_poke.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, 80, 100)
			moved.append(m_p.uid)


def id2_spell(P1P, P2P, m_p, tar, t, moved, tree):
	if m_p.uid < 4:
		enemy = P2P
	else:
		enemy = P1P

	if t == 1:
		# check line clicked
		line = checkInLine(m_p, tar)
		
		if line and m_p.cur_MP >= 20:
			if line[2] < 4:
				dmg = 60
				# get target points in line using line[1] which 1 distance adjacent to current point
				l = findLinePoints(m_p, line[1], 3)
				for i in enemy:
					if [i.x, i.y] in l:
						i.cur_HP  = MHCal(i.cur_HP, 0, belowZero(dmg - i.cur_def), i.HP)
						print("water gun!")
				m_p.cur_MP = MHCal(m_p.cur_MP, 0, 20, 100)
				moved.append(m_p.uid)

	elif t == 2:
		if tar in rangeCal(m_p.x, m_p.y, 2) and m_p.cur_MP >= 20:
			x, y = tar[0], tar[1]
			if x % 2 == 0:
				l = [[x - 1,y - 1],[x - 2,y],[x - 1,y],[x + 1,y - 1],[x + 1,y],[x + 2,y]]
			if x % 2 == 1:
				l = [[x - 1, y],[x - 2, y],[x + 1, y],[x + 2,y],[x - 1,y + 1],[x + 1,y + 1]]
			for i in l:
				if i[0] >= 0 and i[0] < 20 and i[1] >= 0 and i[1] < 20 and i not in Poke_GUI.spring and i not in Poke_GUI.fire and i not in Poke_GUI.water and i not in Poke_GUI.telepot and i not in tree:
					if i in Poke_GUI.firer:
						Poke_GUI.firer.remove(i)
					Poke_GUI.water.append(i)
			if tar not in Poke_GUI.spring and tar not in Poke_GUI.fire and tar not in Poke_GUI.water and tar not in Poke_GUI.telepot and tar not in tree:
				if tar in Poke_GUI.firer:
					Poke_GUI.firer.remove(tar)
				Poke_GUI.water.append(tar)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, 20, 100)
			moved.append(m_p.uid)

	elif t == 3:
		l = []
		x, y = m_p.x, m_p.y
		
		if m_p.x % 2 == 0:
			if tar == [x - 3, y - 1]:
				l += findLinePoints(m_p,[x-2,y],2)
				l += findLinePoints(m_p,[x-1,y-1],2)
				l.append([x - 3, y - 1])
			elif tar == [x - 3, y]:
				l += findLinePoints(m_p,[x-2,y],2)
				l += findLinePoints(m_p,[x-1,y],2)
				l.append([x - 3, y])
			elif tar == [x, y + 1]:
				l += findLinePoints(m_p,[x-1,y],2)
				l += findLinePoints(m_p,[x+1,y],2)
				l.append([x, y + 1])
			elif tar == [x + 3, y]:
				l += findLinePoints(m_p,[x+1,y],2)
				l += findLinePoints(m_p,[x+2,y],2)
				l.append([x + 3, y])
			elif tar == [x + 3, y - 1]:
				l += findLinePoints(m_p,[x+2,y],2)
				l += findLinePoints(m_p,[x+1,y-1],2)
				l.append([x + 3, y - 1])
			elif tar == [x , y - 1]:
				l += findLinePoints(m_p,[x+1,y-1],2)
				l += findLinePoints(m_p,[x-1,y-1],2)
				l.append([x, y - 1])
		elif m_p.x % 2 == 1:
			if tar == [x - 3, y]:
				l += findLinePoints(m_p,[x-1,y],2)
				l += findLinePoints(m_p,[x-2,y],2)
				l.append([x - 3, y])
			elif tar == [x - 3, y + 1]:
				l += findLinePoints(m_p,[x-2,y],2)
				l += findLinePoints(m_p,[x-1,y+1],2)
				l.append([x - 3, y + 1])
			elif tar == [x, y + 1]:
				l += findLinePoints(m_p,[x-1,y+1],2)
				l += findLinePoints(m_p,[x+1,y+1],2)
				l.append([x, y + 1])
			elif tar == [x + 3, y + 1]:
				l += findLinePoints(m_p,[x+2,y+1],2)
				l += findLinePoints(m_p,[x+2,y],2)
				l.append([x + 3, y + 1])
			elif tar == [x + 3, y]:
				l += findLinePoints(m_p,[x+2,y],2)
				l += findLinePoints(m_p,[x+1,y],2)
				l.append([x + 3, y])
			elif tar == [x, y - 1]:
				l += findLinePoints(m_p,[x+1,y],2)
				l += findLinePoints(m_p,[x-1,y],2)
				l.append([x, y - 1])
		dmg = 80
		if l != [] and m_p.cur_MP >= 20:
			for i in enemy:
				if [i.x, i.y] in l:
					print("ulti hit on")
					i.cur_HP  = MHCal(i.cur_HP, 0, belowZero(dmg - i.cur_def), i.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, 20, 100)
			moved.append(m_p.uid)












# cur_pos: [x, y], enemy: P1P
def find_next(cur_pos, enemy, n):
	for i in enemy:
		if [i.x, i.y] in rangeCal(cur_pos[0], cur_pos[1], n):
			return i
	return False


# return string for direaction / distance 1 adjacent point / distance to tar
def checkInLine(m_p, tar):
	d_x, d_y = tar[0] - m_p.x, tar[1] - m_p.y
	a_x, a_y = abs(d_x), abs(d_y)
	if d_y == 0:
		if d_x % 2 == 0 and d_x > 0:
			return ['b', [m_p.x + 2, m_p.y], int(d_x / 2)]
		elif d_x % 2 == 0 and d_x < 0:
			return ['t', [m_p.x + 2, m_p.y], int(d_x / 2)]
	elif m_p.x % 2 == 0:
		# top left
		if d_x < 0 and d_y < 0:
			if int((a_x + 1) / 2) == a_y:
				return ['tl', [m_p.x - 1, m_p.y - 1], a_x]
		# bot left
		if d_x > 0 and d_y < 0:
			if int((a_x + 1) / 2) == a_y:
				return ['bl', [m_p.x + 1, m_p.y + 1], a_x]
		# top right
		if d_x < 0 and d_y >= 0:
			if int(a_x / 2) == a_y:
				return ['tr', [m_p.x - 1, m_p.y], a_x]
		if d_x > 0 and d_y >= 0:
			if int(a_x / 2) == a_y:
				return ['br', [m_p.x + 1, m_p.y], a_x]
	elif m_p.x % 2 == 1:
		# top left
		if d_x < 0 and d_y <= 0:
			if int(a_x / 2) == a_y:
				return ['tl', [m_p.x - 1, m_p.y], a_x]
		# bot left
		if d_x > 0 and d_y <= 0:
			if int(a_x / 2) == a_y:
				return ['bl', [m_p.x + 1, m_p.y], a_x]
		# top right
		if d_x < 0 and d_y > 0:
			if int((a_x + 1) / 2) == a_y:
				return ['tr', [m_p.x - 1, m_p.y + 1], a_x]
		# bot right
		if d_x > 0 and d_y > 0:
			if int((a_x + 1) / 2) == a_y:
				return ['br', [m_p.x + 1, m_p.y + 1], a_x]
	return False


# find line points / m_p and tar must be adjacent
def findLinePoints(m_p, tar, n):
	del_x, del_y = tar[0] - m_p.x, tar[1] - m_p.y

	l = []

	# down and up
	if (del_x == 2 or del_x == -2 ) and del_y == 0:
		for i in range(n):
			l.append([m_p.x + del_x * (i + 1), m_p.y])
		return l


	if m_p.x % 2 == 0:
		if (del_x == -1 or del_x == 1) and del_y == -1:
			for i in range(n):
				l.append([m_p.x + del_x * (i + 1), m_p.y - int((i + 2) / 2)])
		elif (del_x == -1 or del_x == 1) and del_y == 0:
			for i in range(n):
				l.append([m_p.x + del_x * (i + 1), m_p.y + int((i + 1) / 2)])
		return l

	elif m_p.x % 2 == 1:
		if (del_x == -1 or del_x == 1) and del_y == 0:
			for i in range(n):
				l.append([m_p.x + del_x * (i + 1), m_p.y - int((i + 1) / 2)])
		elif (del_x == -1 or del_x == 1) and del_y == 1:
			for i in range(n):
				l.append([m_p.x + del_x * (i + 1), m_p.y + int((i 	+ 2) / 2)])
		return l


def belowZero(val):
	if val < 0:
		return 0
	else:
		return val