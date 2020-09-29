import random
def jelszo_szam(db):
	szoveg=""
	tomb="123456789"
	for x in range (0,db):
		szoveg+=tomb[random.randint(0,len(tomb))]:
	return szoveg
print (jelszo_szam(1))
print (jelszo_szam(5))
print (jelszo_szam(8))

def jelszo_spec(db):
	szoveg=""
	tomb="*>;<@&#~"
	for x in range (0,db):
			szoveg+=tomb[random.randint(0,len(tomb))]
	return szoveg
print (jelszo_szam(1))
print (jelszo_szam(5))
print (jelszo_szam(8))	
	
print (jelszo_szam(2))
print (jelszo_kisbetu(3))
print (jelszo_nagybetu(3))
print (jelszo_spec(2))

def jelszo_abc(db)
	szoveg=""
	tomb="abcdefghijklmnopqrstuvwxyz"
	for x in range (0,db)
		szoveg+=tomb[random.randint(0,len(tomb))]:
	return szoveg
	
print (jelszo_kisbetu(3))