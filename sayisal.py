import random
kupon=[]
for i in range(0,8):
	kolon = []
	elli  = range(1,50)
	for j in range (0,6):
		sayi=random.choice(elli)
		kolon.append(sayi)
		elli.remove(sayi)
		kolon.sort()
		j=j+1
	kupon.append(kolon)
	i=i+1
print kupon


