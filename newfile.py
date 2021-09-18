va = [0,1,2]
foda = int(input('1   '))
fodb = int(input("2   "))
fodc = int(input('3   '))
fodd = int(input("4   "))
hvak = int(foda+fodb+fodc+fodd)
global ha
ha = int(hvak/20)
global he
he = int(ha//10)
global rea
global reb
global rec
x = int(str(ha)[-1])
if x in va:
	rea = int(str(he)+"0")
	print(str(he)+"0")
else:
    rea = int(ha-x+10)
    print(ha-x+10)

awal = int(rea/10)
hf = int(awal//10)
y  = int(str(awal)[-1])
if y in va:
	print(str(hf)+"0")
	reb = int(str(hf)+"0")
else:
	print(awal-y+10)
	reb = int(awal-y+10)
	
tani = int(rea/20)
hg = int(tani//10)
vc = int(str(tani)[-1])
if vc in va:
	print(str(hg)+"0")
	rec = int(str(hg)+"0")
else:
	print(tani-vc+10)
	rec = int(tani-vc+10)
print(rec+rea+reb+hvak)