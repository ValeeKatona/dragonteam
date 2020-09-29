def jelszo_szam(db):
	szoveg=""
	tomb="0123456789"
	for x in range(0,db):
		szoveg+=tomb[random.randint(0,len(tomb))]
	return szoveg
print(jelszo_szam(1))
print(jelszo_szam(3))
print(jelszo_szam(5))