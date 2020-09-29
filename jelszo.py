import random
def jelszo_szam(db):
	szoveg=""
	tomb="123456789"
	for x in range (0,db):
		szoveg+=tomb[random.randint(0,len(tomb))]:
	return szoveg

def jelszo_spec(db):
	szoveg2=""
	tomb2="*>;<@&#~"
	for x in range (0,db):
			szoveg2+=tomb2[random.randint(0,len(tomb))]
	return szoveg2
	
def jelszo_nagybetu(db):
	szoveg3=""
	tomb3="QWERTZUIOPASDFGHJKLYXCVBNM"
for x in range (0,db):
	szoveg3+=tomb3[random.randint(0,len(abc)-1)]
	return szoveg3

	
def jelszo_kisbetu(db)
	szoveg4=""
	tomb4="abcdefghijklmnopqrstuvwxyz"
	for x in range (0,db)
		szoveg4+=tomb4[random.randint(0,len(tomb))]
	return szoveg4
	
jelszo=jelszo_szam(2)+jelszo_nagybetu(3)+jelszo_kisbetu(3)+jelszo_spec(2)+jelszo_szam(1)
print(jelszo)