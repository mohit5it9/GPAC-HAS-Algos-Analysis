f = open("rep.txt", "r")
switches = 0
init = False
count = 0
s = 0
ma = 0
for x_read in f:
	x = int(x_read)
	if x > ma:
		ma = x
	count += 1.0
	s += x
	if init == False:
		prev = x
		init = True
	else:
		if x != prev:
			switches += 1
			prev = x
print "switches: ", switches
print "total rep: ", count
print "avg repr: ", s/count
print "max rep:", ma




f = open("buf.txt", "r")
underrun = 0
count = 0
s = 0
for x_read in f:
	x= int(x_read)
	count += 1
	if x == 0:
		underrun += 1
	s += x
print "underrun: ", underrun

print "avg buff: ", s/count
