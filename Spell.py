import copy, random
import Poke_GUI

MP1 = 20
MP2 = 20
MP3 = 80

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
				l.append([i,y-1])
			for i in range(x - 5, x + 6):
				l.append([i,y+1])
			l = l + [[x-3,y+2],[x-1,y+2],[x+1,y+2],[x+3,y+2]]
		return l
		
	if n == 4:
		l = []
		for i in range(x - 8, x + 9):
			l.append([i, y]) 
		if x % 2 == 0:
			for i in range(x - 6, x + 7):
				l.append([i, y + 1])
			for i in range(x - 7, x + 8):
				l.append([i, y - 1])
			for i in range(x - 5, x + 6):
				l.append([i, y - 2])
			l = l + [[x-4,y+2],[x-2,y+2],[x,y+2],[x+2,y+2],[x+4,y+2]]
		if x % 2 == 1:
			for i in range(x - 7, x + 8):
				l.append([i,y+1])
			for i in range(x - 5, x + 6):
				l.append([i,y+2])
			for i in range(x - 6, x + 7):
				l.append([i,y-1])
			l = l + [[x-4,y-2],[x-2,y-2],[x,y-2],[x+2,y-2],[x+4,y-2]]
		return l


# MP HP calculate
# iod: increase or decrease / 0 for decrease / 1 for increase
def MHCal(tar, iod, n, full):
	if iod == 0:
		if tar >= n:
			return tar - n
		else:
			return 0
	if iod == 1:
		if tar + n >= full:
			return full
		else:
			return tar + n
	return 0



# m_p is package of pokemon / tar is index of click
def id0_spell(P1P, P2P, m_p, tar, t, moved):
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
 		if tar in rangeCal(m_p.x, m_p.y, 2) and m_p.cur_MP >= MP1 and tar_on:
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
 			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
 			moved.append(m_p.uid)

	elif t == 2:
		if tar in rangeCal(m_p.x, m_p.y, 2) and m_p.cur_MP >= MP2 and tar_on:
			dmg = 40
			tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, belowZero(dmg - tar_poke.cur_def), tar_poke.HP)
			m_p.buff_turn = 3
			m_p.buff_def += 5
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP2, 100)
			moved.append(m_p.uid)

	elif t == 3:
		if tar in rangeCal(m_p.x, m_p.y, 2) and m_p.cur_MP >= MP3 and tar_on:
			dmg = 120
			tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, belowZero(dmg - tar_poke.cur_def), tar_poke.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)


def id1_spell(map, P1P, P2P, m_p, tar, t, moved):
	if m_p.uid < 4:
		enemy = P2P
	else:
		enemy = P1P

	if t == 1:
		# check line clicked
		line = checkInLine(m_p, tar)


		
		if line and m_p.cur_MP >= MP1:
			print(line[0], line[2])
			if line[2] < 4:
				dmg = 60
				# get target points in line using line[1] which 1 distance adjacent to current point
				l = findLinePoints(m_p, line[1], 3)
				for i in enemy:
					if [i.x, i.y] in l:
						i.cur_HP  = MHCal(i.cur_HP, 0, belowZero(dmg - i.cur_def), i.HP)
						print("water gun!")
				m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
				moved.append(m_p.uid)

	elif t == 2:
		if tar in rangeCal(m_p.x, m_p.y, 2) and m_p.cur_MP >= MP2:
			x, y = tar[0], tar[1]
			if x % 2 == 0:
				l = [[x - 1,y - 1],[x - 2,y],[x - 1,y],[x + 1,y - 1],[x + 1,y],[x + 2,y],[x, y]]
			if x % 2 == 1:
				l = [[x - 1, y],[x - 2, y],[x + 1, y],[x + 2,y],[x - 1,y + 1],[x + 1,y + 1],[x, y]]
			for i in l:
				if i[0] >= 0 and i[0] < 20 and i[1] >= 0 and i[1] < 20 and map[i[0]][i[1]] != 'spring' and map[i[0]][i[1]] != 'fire'\
				 and map[i[0]][i[1]] != 'telepot' and map[i[0]][i[1]] != 'tree':
					map[i[0]][i[1]] = 'water'
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP2, 100)
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
				l += findLinePoints(m_p,[x+1,y+1],2)
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
		if l != [] and m_p.cur_MP >= MP3:
			for i in enemy:
				if [i.x, i.y] in l:
					print("ulti hit on")
					i.cur_HP  = MHCal(i.cur_HP, 0, belowZero(dmg - i.cur_def), i.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)


def id2_spell(map, P1P, P2P, m_p, tar, t, moved):
	if m_p.uid < 4:
		enemy = P2P
	else:
		enemy = P1P

	tar_on = False
	for i in enemy:
		if tar[0] == i.x and tar[1] == i.y:
			tar_poke = i
			tar_on = True
			print("hit on")

	if t == 1:
		line = checkInLine(m_p, tar)
		
		if line and m_p.cur_MP >= MP1:
			if line[2] < 4:
				dmg = 60
				# get target points in line using line[1] which 1 distance adjacent to current point
				l = findLinePoints(m_p, line[1], 3)
				for i in enemy:
					if [i.x, i.y] in l:
						i.cur_HP  = MHCal(i.cur_HP, 0, belowZero(dmg - i.cur_def), i.HP)
				for i in l:
					if map[i[0]][i[1]] == 'tree':
						map[i[0]][i[1]] = '0'

				m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
				moved.append(m_p.uid)

	elif t == 2:
		if m_p.cur_MP >= MP2:
			l = rangeCal(m_p.x, m_p.y, 1) + [[m_p.x,m_p.y]]
			for i in l:
				if i[0] >= 0 and i[0] < 20 and i[1] >= 0 and i[1] < 10:
					if map[i[0]][i[1]] != 'spring' and map[i[0]][i[1]] != 'water' and map[i[0]][i[1]] != 'telepot'\
					 and map[i[0]][i[1]] != 'fire' and map[i[0]][i[1]] != 'ocean':
						map[i[0]][i[1]] = 'firer'
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP2, 100)
			moved.append(m_p.uid)
	elif t == 3:
		if tar in rangeCal(m_p.x, m_p.y, 1) and m_p.cur_MP >= MP3 and tar_on:
			dmg = 160
			tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, belowZero(dmg - tar_poke.cur_def), tar_poke.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)

# miao wa zhong zi
def id3_spell(map, P1P, P2P, m_p, tar, t, moved, turn):
	if m_p.uid < 4:
		enemy = P2P
	else:
		enemy = P1P

	if t == 1:
		line = checkInLine(m_p, tar)

		
		if line and m_p.cur_MP >= MP1 and line[2] < 5:
			dmg = 60
			l = findLinePoints(m_p, line[1], 4)

			#print(l)
			
			fir_e = []

			for i in l:
				a, b = i[0], i[1]
				if a >= 0 and a < 20 and b >= 0 and b < 20 and fir_e == []:
					for e_ in enemy:
						if a == e_.x and b == e_.y:
							e_.cur_HP = MHCal(e_.cur_HP, 0, belowZero(dmg - e_.cur_def), e_.HP)
							fir_e.append(e_)

			print(fir_e)
			if fir_e != []:
				if checkSpaceAva(map,line[1][0], line[1][1], P1P, P2P) and map[line[1][0]][line[1][1]] != 'tree':
					fir_e[0].x = line[1][0]
					fir_e[0].y = line[1][1]
					m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
					moved.append(m_p.uid)
	elif t == 2:
		line = checkInLine(m_p, tar)
		if line and m_p.cur_MP >= MP1 and line[2] < 7:
			l = findLinePoints(m_p, line[1], 6)
			for i in l: 
				if map[i[0]][i[1]] != 'firer' and map[i[0]][i[1]] != 'tree':
					if checkSpaceAva(map, i[0], i[1], P1P, P2P):
						map[i[0]][i[1]] = 'tree'
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP2, 100)
			moved.append(m_p.uid)
	elif t == 3:
		if not m_p.ult:
			m_p.cur_turn = turn
			m_p.ult = True
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)

def id3_ult(P1P, P2P, m_p, moved):
	if m_p.uid < 4:
		enemy = P2P
	else:
		enemy = P1P

	m_p.ult = False
	dmg = 240
	for i in enemy:
		if [i.x, i.y] in rangeCal(m_p.x, m_p.y, 2):
			i.cur_HP = MHCal(i.cur_HP, 0, belowZero(dmg - i.cur_def), i.HP)
			break
	moved.append(m_p.uid)

# ka bi shou
def id4_spell(P1P, P2P, m_p, tar, t, moved, turn):
	if m_p.uid < 4:
		enemy = P2P
	else:
		enemy = P1P

	tar_on = False
	for i in enemy:
		if tar[0] == i.x and tar[1] == i.y:
			tar_poke = i
			tar_on = True
			print("hit on")

	if t == 1:
		if tar in rangeCal(m_p.x, m_p.y, 1) and m_p.cur_MP >= MP1 and tar_on:
			dmg = 50
			tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, belowZero(dmg - tar_poke.cur_def), tar_poke.HP)
			m_p.buff_turn = 1
			m_p.buff_att -= 10
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
			moved.append(m_p.uid)
	elif t == 2:
		if m_p.cur_MP >= MP2:
			m_p.buff_turn = 5
			m_p.buff_def += 5
			m_p.buff_att += 10
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP2, 100)
			moved.append(m_p.uid)
	elif t == 3:
		if m_p.cur_MP >= MP3:
			m_p.cur_HP = m_p.HP
			m_p.cur_turn = turn
			m_p.ult = True
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)

#tu tou long
def id5_spell(P1P, P2P, m_p, tar, t, moved):
	if m_p.uid < 4:
		enemy = P2P
	else:
		enemy = P1P

	tar_on = False
	for i in enemy:
		if tar[0] == i.x and tar[1] == i.y:
			tar_poke = i
			tar_on = True
			print("hit on")

	if t == 1:
		if tar in rangeCal(m_p.x, m_p.y, 2) and m_p.cur_MP >= MP1 and tar_on:
			dmg = 40
			tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, dmg, tar_poke.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
			moved.append(m_p.uid)
	elif t == 2:
		for i in enemy:
			if [i.x, i.y] in rangeCal(m_p.x, m_p.y, 2):
				i.buff_turn = 1
				i.buff_def -= 10
		m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP2, 100)
		moved.append(m_p.uid)
	elif t == 3:
		line = checkInLine(m_p, tar)

		if line and m_p.cur_MP >= MP1 and line[2] < 4:
			dmg_t = 0
			dmg = 80
			# get target points in line using line[1] which 1 distance adjacent to current point
			l = findLinePoints(m_p, line[1], 3)
			for i in enemy:
				if [i.x, i.y] in l:
					i.cur_HP  = MHCal(i.cur_HP, 0, belowZero(dmg - i.cur_def), i.HP)
					dmg_t += belowZero(dmg - i.cur_def)
					print("Dragon fire!")
			m_p.cur_HP = MHCal(m_p.cur_HP, 1, int(dmg_t * 0.3), m_p.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)

# du she
def id6_spell(P1P, P2P, m_p, tar, t, moved):
	if m_p.uid < 4:
		enemy = P2P
	else:
		enemy = P1P

	tar_on = False
	for i in enemy:
		if tar[0] == i.x and tar[1] == i.y:
			tar_poke = i
			tar_on = True
			print("hit on")

	if t == 1:
		if tar in rangeCal(m_p.x, m_p.y, 2) and m_p.cur_MP >= MP1 and tar_on:
			tar_poke.poison_turn += 3
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
			moved.append(m_p.uid)

	elif t == 2:
		if tar in rangeCal(m_p.x, m_p.y, 2) and m_p.cur_MP >= MP2 and tar_on:
			tar_poke.cur_MP = MHCal(tar_poke.cur_MP, 0, 28, 100)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP2, 100)
			moved.append(m_p.uid)

	elif t == 3:
		if tar in rangeCal(m_p.x, m_p.y, 3) and m_p.cur_MP >= MP3 and tar_on:
			tar_poke.poison_turn += 7
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)

# zheng fu pai pai
def id7_spell(P1P, P2P, m_p, tar, t, moved):
	enemy, ours, tar_on, tar_ours, tar_poke = targetSetup(m_p, P1P, P2P, tar)

	if t == 1:
		if tar in rangeCal(m_p.x, m_p.y, 2) and m_p.cur_MP >= MP1 and tar_on:
			dmg = 60
			tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, dmg, tar_poke.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
			moved.append(m_p.uid)
		elif tar in rangeCal(m_p.x, m_p.y, 2) and m_p.cur_MP >= MP1 and tar_ours:
			tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 1, 40, tar_poke.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
			moved.append(m_p.uid)

	elif t == 2:
		if tar in rangeCal(m_p.x, m_p.y, 3) and m_p.cur_MP >= MP2 and (tar_on or tar_ours):
			tar_poke.x = m_p.x
			tar_poke.y = m_p.y
			m_p.x = tar[0]
			m_p.y = tar[1]
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP2, 100)
			moved.append(m_p.uid)

	elif t == 3:
		if m_p.cur_MP >= MP3:
			for i in ours:
				if i.uid in moved:
					moved.remove(i.uid)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)


# bi diao
def id8_spell(map, P1P, P2P, m_p, tar, t, moved):
	if m_p.uid < 4:
		enemy = P2P
		ours = P1P
	else:
		enemy = P1P
		ours = P2P

	tar_on = False
	for a in enemy:
		if tar[0] == a.x and tar[1] == a.y:
			tar_poke = a
			tar_on = True
			print("hit on")
	tar_ours = False
	for b in ours:
		if tar[0] == b.x and tar[1] == b.y:
			tar_poke = b
			tar_ours = True
	
	if t == 1:
		if tar in rangeCal(m_p.x, m_p.y, 1) and m_p.cur_MP >= MP1 and tar_on:
			dmg = 60
			tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, dmg, tar_poke.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
			moved.append(m_p.uid)

			line = checkInLine(m_p, tar)
			print(line)
			l = (findLinePoints(m_p, line[3], 2))[::-1]
			print(l)
			for i in l:
				if checkSpaceAva(map, i[0], i[1], P1P, P2P):
					m_p.x, m_p.y = i[0], i[1]
					break

	elif t == 2:
		if tar in rangeCal(m_p.x, m_p.y, 2) and m_p.cur_MP >= MP2 and (tar_on or tar_ours):
			m_p.type2 = tar_poke.type
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP2, 100)
			moved.append(m_p.uid)

	elif t == 3:
		line = checkInLine(m_p, tar)
		
		if line and m_p.cur_MP >= MP3 and line[2] < 6:
			dmg = 80
			# get target points in line using line[1] which 1 distance adjacent to current point
			l = findLinePoints(m_p, line[1], 5)
			for i in enemy:
				if [i.x, i.y] in l:
					i.cur_HP  = MHCal(i.cur_HP, 0, belowZero(dmg - i.cur_def), i.HP)
			for i in l[::-1]:
				if checkSpaceAva(map, i[0], i[1], P1P, P2P):
					m_p.x, m_p.y = i[0], i[1]
					break

			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)


# pang ding
def id9_spell(P1P, P2P, m_p, tar, t, moved):	
	if m_p.uid < 4:
		enemy = P2P
		ours = P1P
	else:
		enemy = P1P
		ours = P2P
	if t == 1:
		if m_p.cur_MP >= MP1:
			for i in ours:
				if [i.x, i.y] in rangeCal(m_p.x, m_p.y, 2):
					i.cur_HP  = MHCal(i.cur_HP, 1, 30, i.HP)
					print("HP up")
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
			moved.append(m_p.uid)
	elif t == 2:
		if m_p.cur_MP >= MP2:
			for i in ours:
				if [i.x, i.y] in rangeCal(m_p.x, m_p.y, 2):
					i.cur_MP  = MHCal(i.cur_MP, 1, 12, 100)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, 24, 100)
			moved.append(m_p.uid)
	elif t == 3:
		if m_p.cur_MP >= MP3:
			for i in enemy:
				if [i.x, i.y] in rangeCal(m_p.x, m_p.y, 3):
					i.stun = True
					print("Sleep!")
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)

# gu la duo
def id10_spell(map, P1P, P2P, m_p, tar, t, moved):
	enemy, ours, tar_on, tar_ours, tar_poke = targetSetup(m_p, P1P, P2P, tar)
	if t == 1:
		if tar in rangeCal(m_p.x, m_p.y, 3) and  m_p.cur_MP >= MP1 and tar_on:
			if map[m_p.x][m_p.y] == 'firer':
				dmg = 100
			else:
				dmg = 70
			tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, belowZero(dmg - tar_poke.cur_def), tar_poke.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
			moved.append(m_p.uid)
	elif t == 2:
		if m_p.cur_MP >= MP2:
			l = rangeCal(m_p.x, m_p.y, 2) + [[m_p.x, m_p.y]]
			for i in l:
				if i[0] >= 0 and i[0] < 20 and i[1] >= 0 and i[1] < 10 and map[i[0]][i[1]] != 'spring' and\
				 map[i[0]][i[1]] != 'fire' and map[i[0]][i[1]] != 'telepot':
					map[i[0]][i[1]] = 'firer'
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP2, 100)
			moved.append(m_p.uid)
	elif t == 3:
		dmg = 140
		if m_p.cur_MP >= MP3:
			l = rangeCal(m_p.x, m_p.y, 2)
			print(l)
			for i in enemy:
				if [i.x, i.y] in l:
					i.cur_HP = MHCal(i.cur_HP, 0, belowZero(dmg - i.cur_def), i.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)




# hai huang ya
def id11_spell(map, P1P, P2P, m_p, tar, t, moved):
	enemy, ours, tar_on, tar_ours, tar_poke = targetSetup(m_p, P1P, P2P, tar)
	if t == 1:
		if tar in rangeCal(m_p.x, m_p.y, 3) and  m_p.cur_MP >= MP1 and tar_on:
			if map[m_p.x][m_p.y] == 'water' or map[m_p.x][m_p.y] == 'ocean':
				dmg = 100
			else:
				dmg = 70
			tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, belowZero(dmg - tar_poke.cur_def), tar_poke.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
			moved.append(m_p.uid)
	elif t == 2:
		if m_p.cur_MP >= MP2:
			for a in range(m_p.x - 2,m_p.x + 3):
				for b in range(m_p.y - 2,m_p.y + 2):
					if a >= 0 and a < 20 and b >= 0 and b < 10 and map[a][b] != 'srping' and map[a][b] != 'fire' and map[a][b] != 'telepot':
						map[a][b] = 'water'
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP2, 100)
			moved.append(m_p.uid)
	elif t == 3:
		dmg = 60
		if m_p.cur_MP >= MP3:
			l = []
			for i in rangeCal(m_p.x, m_p.y, 3):
				if i not in rangeCal(m_p.x, m_p.y, 1):
					l.append(i)
			Poke_GUI.ocean_center = [m_p.x, m_p.y]
			for i in l:
				if i[0] >= 0 and i[0] < 20 and i[1] >= 0 and i[1] < 10 and map[i[0]][i[1]] != 'spring' \
				and map[i[0]][i[1]] != 'fire' and map[i[0]][i[1]] != 'telepot':
					map[i[0]][i[1]] = 'ocean'
			for i in enemy:
				if map[i.x][i.y] == 'ocean':
					i.cur_HP = MHCal(i.cur_HP, 0, belowZero(dmg - i.cur_def), i.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)

# tian kong long
def id12_spell(P1P, P2P, m_p, tar, t, moved):
	enemy, ours, tar_on, tar_ours, tar_poke = targetSetup(m_p, P1P, P2P, tar)
	print(m_p.spell_extra)
	if t == 1:
		if tar in rangeCal(m_p.x, m_p.y, 3) and  m_p.cur_MP >= MP1 and tar_on:
			if m_p.spell_extra == 0:
				tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, belowZero(70), tar_poke.HP)
			else:
				tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, belowZero(70 + m_p.spell_extra), tar_poke.HP)
				m_p.spell_extra = 0
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
			moved.append(m_p.uid)
	elif t == 2:
		if m_p.cur_MP >= MP2:
			m_p.spell_extra += 25
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP2, 100)
			moved.append(m_p.uid)
	elif t == 3:
		if m_p.cur_MP >= MP3:
			if m_p.spell_extra == 0:
				dmg = 140
			else:
				dmg = 140 + m_p.spell_extra
				m_p.spell_extra = 0
			for i in enemy:
				if m_p.spell_extra == 0:
					i.cur_HP = MHCal(i.cur_HP, 0, belowZero(dmg - i.cur_def), i.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)


# luo qi ya
def id13_spell(P1P, P2P, m_p, tar, t, moved):
	enemy, ours, tar_on, tar_ours, tar_poke = targetSetup(m_p, P1P, P2P, tar)
	if t == 1:
		if tar in rangeCal(m_p.x, m_p.y, 3) and  m_p.cur_MP >= MP1 and tar_on:
			dmg = 80
			tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, belowZero(dmg - tar_poke.cur_def), tar_poke.HP)
			for i in ours:
				if i.type == 'water' or i.type2 == 'water':
					i.buff_turn = 2
					i.buff_att += 10
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)
	elif t == 2:
		if m_p.cur_MP > MP2:
			m_p.cur_HP = MHCal(m_p.cur_HP, 1, 195, m_p.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP2, 100)
			moved.append(m_p.uid)
	elif t == 3:
		if tar in rangeCal(m_p.x, m_p.y, 3) and  m_p.cur_MP >= MP3 and tar_on:
			dmg = 130
			tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, belowZero(dmg - tar_poke.cur_def), tar_poke.HP)
			tar_poke.buff_turn = 2
			tar_poke.buff_def = 0 - tar_poke.cur_def
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)

# lei gong
def id14_spell(map, P1P, P2P, m_p, tar, t, moved, thunder):
	enemy, ours, tar_on, tar_ours, tar_poke = targetSetup(m_p, P1P, P2P, tar)
	if t == 1:
		if tar in rangeCal(m_p.x, m_p.y, 3) and m_p.cur_MP >= MP1 and tar_on:
			dmg = 65
			tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, belowZero(dmg - tar_poke.cur_def), tar_poke.HP)
			tar_poke.stun = True
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
			moved.append(m_p.uid)
	elif t == 2:
		if tar in rangeCal(m_p.x, m_p.y, 3) and m_p.cur_MP >= MP2 and tar_on:
			l = rangeCal(tar[0], tar[1], 1) + [[tar[0], tar[1]]]
			for i in enemy:
				if [i.x, i.y] in l:
					i.stun = True
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP2, 100)
			moved.append(m_p.uid)
	elif t == 3:
		if m_p.cur_MP >= MP3:
			l = []
			for i in rangeCal(m_p.x, m_p.y, 3):
				if i not in rangeCal(m_p.x, m_p.y, 2):
					l.append(i)
			thunder.append([0,6])
			for i in l:
				if i[0] >= 0 and i[0] < 20 and i[1] >= 0 and i[1] < 10 and map[i[0]][i[1]] != 'spring'\
				 and map[i[0]][i[1]] != 'fire' and map[i[0]][i[1]] != 'telepot' :
					thunder.append(i)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)


# kuai long
def id15_spell(P1P, P2P, m_p, tar, t, moved):
	enemy, ours, tar_on, tar_ours, tar_poke = targetSetup(m_p, P1P, P2P, tar)
	if t == 1:
		if tar in rangeCal(m_p.x, m_p.y, 2) and m_p.cur_MP >= MP1 and tar_on:
			l = rangeCal(tar[0], tar[1], 1) + [tar]
			for i in enemy:
				if [i.x, i.y] in l:
					i.cur_HP = MHCal(i.cur_HP, 0, 60, i.HP)
			m_p.cur_HP = MHCal(m_p.cur_HP, 0, 50, m_p.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
			moved.append(m_p.uid)
	elif t == 2:
		if tar in rangeCal(m_p.x, m_p.y, 2) and m_p.cur_MP >= MP2 and (tar_on or tar_ours):
			if tar_on:
				tar_poke.buff_turn = 2
				tar_poke.buff_def -= 10
			if tar_ours:
				tar_poke.buff_turn = 2
				tar_poke.buff_att += 20
			m_p.buff_turn = 2
			m_p.buff_def -= 10
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP2, 100)
			moved.append(m_p.uid)
	elif t == 3:
		if m_p.cur_MP >= MP3:
			l = rangeCal(m_p.x, m_p.y, 2)
			for i in ours:
				if [i.x, i.y] in l:
					i.buff_turn = 2
					i.buff_att += 30
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)


# cao ci wei
def id16_spell(P1P, P2P, m_p, tar, t, moved):
	enemy, ours, tar_on, tar_ours, tar_poke = targetSetup(m_p, P1P, P2P, tar)
	if t == 1:
		if m_p.cur_MP >= MP1:
			l = rangeCal(m_p.x, m_p.y, 2) + [[m_p.x, m_p.y]]
			for i in ours:
				if [i.x, i.y] in l:
					i.cur_HP = MHCal(i.cur_HP, 1, int(i.HP * 0.15), i.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
			moved.append(m_p.uid)
	elif t == 2:
		if m_p.cur_MP >= MP2:
			l = rangeCal(m_p.x, m_p.y, 2) + [[m_p.x, m_p.y]]
			for i in ours:
				if [i.x, i.y] in l:
					i.buff_turn = 5
					i.buff_att += 6
					i.buff_def += 12
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP2, 100)
			moved.append(m_p.uid)
	elif t == 3:
		if m_p.cur_MP >= MP3:
			l = rangeCal(m_p.x, m_p.y, 2) + [[m_p.x, m_p.y]]
			for i in ours:
				if [i.x, i.y] in l:
					i.cur_HP = MHCal(i.cur_HP, 1, int(i.HP * 0.6), i.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)

# feng huang
def id17_spell(P1P, P2P, m_p, tar, t, moved):
	enemy, ours, tar_on, tar_ours, tar_poke = targetSetup(m_p, P1P, P2P, tar)
	if t == 1:
		if m_p.cur_MP >= MP1:
			l = rangeCal(m_p.x, m_p.y, 2)
			for i in enemy + ours:
				if [i.x, i.y] in l and i != m_p:
					i.cur_HP = MHCal(i.cur_HP, 0, belowZero(80 - i.cur_def), i.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
			moved.append(m_p.uid)
	elif t == 2:
		if m_p.cur_MP >= MP2:
			m_p.buff_turn = 5
			m_p.buff_att += 5
			m_p.buff_def += 5
			m_p.HP += 50
			m_p.cur_HP = MHCal(m_p.cur_HP, 1, 50, m_p.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP2, 100)
			moved.append(m_p.uid)
	elif t == 3:
		if m_p.cur_MP >= MP3:
			if not m_p.once: 
				m_p.ult = True
				m_p.once = True
				m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
				moved.append(m_p.uid)

# xue la bi
def id18_spell(map, P1P, P2P, m_p, tar, t, moved):
	enemy, ours, tar_on, tar_ours, tar_poke = targetSetup(m_p, P1P, P2P, tar)
	if t == 1:
		if tar in rangeCal(m_p.x, m_p.y, 4) and m_p.cur_MP >= 12 and checkSpaceAva(map, tar[0], tar[1], P1P, P2P):
			l = rangeCal(m_p.x, m_p.y, 1) + rangeCal(tar[0], tar[1], 1) + [[m_p.x, m_p.y]] + [tar]
			for i in enemy:
				if [i.x, i.y] in l:
					i.cur_HP = MHCal(i.cur_HP, 0, belowZero(60 - i.cur_def), i.HP)
			m_p.x, m_p.y = tar[0], tar[1]
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, 12, 100)
			moved.append(m_p.uid)
	elif t == 2:
		if tar in rangeCal(m_p.x, m_p.y, 3) and m_p.cur_MP >= 12:
			l = countTree(map, tar[0], tar[1])
			# check how many trees
			if len(l) <= 4:
				for i in l:
					if checkSpaceAva(map, i[0], i[1], P1P, P2P):
						map[i[0]][i[1]] = 'tree'
			# more than 4 space
			else:
				while(len(l) > 4):
					r = int(random.random() * len(l))
					del l[r]
				for i in l:
					if checkSpaceAva(map, i[0], i[1], P1P, P2P):
						map[i[0]][i[1]] = 'tree'

			m_p.cur_MP = MHCal(m_p.cur_MP, 0, 12, 100)
			moved.append(m_p.uid)
	elif t == 3:
		if tar in rangeCal(m_p.x, m_p.y, 3) and m_p.cur_MP >= 80 and tar_on:
			l = rangeCal(tar[0], tar[1], 1)
			death = True
			for i in l:
				print(map[i[0]][i[1]], i[0], i[1])
				if map[i[0]][i[1]] != 'tree':
					death = False
			if death:
				print("Death")
				tar_poke.cur_HP = 0
			else:
				tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, belowZero(100 - tar_poke.cur_def), tar_poke.HP)
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, 80, 100)
			moved.append(m_p.uid)






# xue la bi helper function
def countTree(map, x, y):
	l = rangeCal(x, y, 1)
	for i in l:
		if map[i[0]][i[1]] == 'tree' or i[0] < 0 or i[0] > 19 or i[1] < 0 or i[1] > 9:
			l.remove(i)
	return l


# ji la qi
def id19_spell(P1P, P2P, m_p, tar, t, moved):
	enemy, ours, tar_on, tar_ours, tar_poke = targetSetup(m_p, P1P, P2P, tar)
	if t == 1:
		if m_p.cur_MP >= MP1:
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP1, 100)
			moved.append(m_p.uid)
			d = int(random.random() * 4)
			print('Type ' + str(d) + '  effect...')
			if d == 0:
				for i in ours:
					i.cur_HP = MHCal(i.cur_HP, 1, 50, i.HP)
			elif d == 1:
				for i in enemy:
					i.cur_HP = MHCal(i.cur_HP, 0, belowZero(50 - i.cur_def), i.HP)
			elif d == 2:
				for i in ours:
					i.cur_MP = MHCal(i.cur_MP, 1, 16, 100)
			elif d == 3:
				for i in enemy:
					i.cur_MP = MHCal(i.cur_MP, 1, 16, 100)
	if t == 2:
		if tar in rangeCal(m_p.x, m_p.y, 3) and m_p.cur_MP >= MP2 and tar_on:
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP2, 100)
			moved.append(m_p.uid)
			d = int(random.random() * 10)
			if d > 6:
				print("Congratulation")
				tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, belowZero(140 - tar_poke.cur_def), tar_poke.HP)
			else:
				tar_poke.cur_HP = MHCal(tar_poke.cur_HP, 0, belowZero(70 - tar_poke.cur_def), tar_poke.HP)
	if t == 3:
		if m_p.cur_MP >= MP3:
			for i in ours:
				i.buff_turn = 3
				i.buff_def += 1000000
			m_p.cur_MP = MHCal(m_p.cur_MP, 0, MP3, 100)
			moved.append(m_p.uid)



def targetSetup(m_p, P1P, P2P, tar):
	tar_poke = None
	if m_p.uid < 4:
		enemy = P2P
		ours = P1P
	else:
		enemy = P1P
		ours = P2P

	tar_on = False
	for a in enemy:
		if tar[0] == a.x and tar[1] == a.y:
			tar_poke = a
			tar_on = True
			print("hit on")
	tar_ours = False
	for b in ours:
		if tar[0] == b.x and tar[1] == b.y:
			tar_poke = b
			tar_ours = True
	return enemy, ours, tar_on, tar_ours, tar_poke

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
	if d_y == 0 and d_x % 2 == 0:
		if d_x > 0:
			return ['b', [m_p.x + 2, m_p.y], int(d_x / 2), [m_p.x - 2, m_p.y]]
		elif d_x < 0:
			return ['t', [m_p.x - 2, m_p.y], int(d_x / 2), [m_p.x + 2, m_p.y]]
	elif m_p.x % 2 == 0:
		# top left
		if d_x < 0 and d_y < 0:
			if int((a_x + 1) / 2) == a_y:
				return ['tl', [m_p.x - 1, m_p.y - 1], a_x, [m_p.x + 1, m_p.y]]
		# bot left
		if d_x > 0 and d_y < 0:
			if int((a_x + 1) / 2) == a_y:
				return ['bl', [m_p.x + 1, m_p.y - 1], a_x, [m_p.x - 1, m_p.y]]
		# top right
		if d_x < 0 and d_y >= 0:
			if int(a_x / 2) == a_y:
				return ['tr', [m_p.x - 1, m_p.y], a_x, [m_p.x + 1, m_p.y - 1]]
		if d_x > 0 and d_y >= 0:
			if int(a_x / 2) == a_y:
				return ['br', [m_p.x + 1, m_p.y], a_x, [m_p.x - 1, m_p.y - 1]]
	elif m_p.x % 2 == 1:
		# top left
		if d_x < 0 and d_y <= 0:
			if int(a_x / 2) == a_y:
				return ['tl', [m_p.x - 1, m_p.y], a_x, [m_p.x + 1, m_p.y + 1]]
		# bot left
		if d_x > 0 and d_y <= 0:
			if int(a_x / 2) == a_y:
				return ['bl', [m_p.x + 1, m_p.y], a_x, [m_p.x - 1, m_p.y + 1]]
		# top right
		if d_x < 0 and d_y > 0:
			if int((a_x + 1) / 2) == a_y:
				return ['tr', [m_p.x - 1, m_p.y + 1], a_x, [m_p.x + 1, m_p.y]]
		# bot right
		if d_x > 0 and d_y > 0:
			if int((a_x + 1) / 2) == a_y:
				return ['br', [m_p.x + 1, m_p.y + 1], a_x , [m_p.x - 1, m_p.y]]
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

def checkSpaceAva(map, x, y, P1P, P2P):
	for i in P1P:
		if x == i.x and y == i.y:
			return False
	for i in P2P:
		if x == i.x and y == i.y: 
			return False
	if x < 0 or x > 19 or y < 0 or y > 9:
		return False
	elif map[x][y] == 'fire' or map[x][y] == 'spring':
		return False
	else:
		return True