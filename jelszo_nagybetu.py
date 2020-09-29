def jelszo_nagybetu(db):
abc = "QWERTZUIOPASDFGHJKLYXCVBNM"
jelszohossz=3
jelszo=""
for i in range (0,jelszohossz):
	jelszo+=abc[random.randint(0,len(abc)-1)]
