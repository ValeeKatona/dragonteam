def jelszo_kisbetu(db)
	szoveg""
	tomb="qwertzuiopasdfghjkl�yxcvbnm"
	for x in range (0,db)
		szoveg+=tomb[random.randint(0,len(tomb))]
	return szoveg