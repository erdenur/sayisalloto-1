import random
kolonlar = []
for i in range(0,8):
	loto = []
	for a in range(0,6):
		b =random.randrange(1,50)
		loto.append(b)
		if loto.count(b) == 0:
		   loto.append(b)
		   a = a+1
                loto.sort()
		if kolonlar.count(loto) == 0:
		   kolonlar.append(loto)
print kolonlar
