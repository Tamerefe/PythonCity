def sag(adet):
	for a in range(int(adet)):
		print("/",end="")

def sol(adet):
	for a in range(int(adet)):
		print("\\",end="")

def satir(adet):
	for a in range(int(adet)):
		print()

def bosluk(adet):
	for a in range(int(adet)):
		print(" ",end="")		

def istek(cap):
	baslangic = cap/2-1
	for a in range(int(cap/2)):
		bosluk(baslangic-a)
		sag(1)
		bosluk(a*2)
		sol(1)
		satir(1)

def alt(cap):
	baslangic = cap-2
	for a in range(int(cap/2)):
		bosluk(a)
		sol(1)
		bosluk(baslangic - a*2)
		sag(1)
		satir(1)

def paralel(cap):
	istek(cap)
	alt(cap)		


paralel(40)
