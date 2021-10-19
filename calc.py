import json
va = [0]
numfat = input("num of fatora:")
foda = int(input('1  : '))
fodb = int(input("2  : "))
fodc = int(input('3 :  '))
fodd = int(input("4  : "))
hvak = int(foda+fodb+fodc+fodd)
print(hvak)
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
	print(rea)
else:
    rea = int(ha-x+10)
    print(rea)

awal = int(rea/10)
hf = int(awal//10)
y  = int(str(awal)[-1])
if y in va:
	reb = int(str(hf)+"0")
	print(reb)
else:
	reb = int(awal-y+10)
	print(reb)
	
tani = int(rea/20)
hg = int(tani//10)
vc = int(str(tani)[-1])
if vc in va:
	rec = int(str(hg)+"0")
	print(rec)
else:
	rec = int(tani-vc+10)
	print(rec)
	
mainas = rec+rea+reb+hvak
print(mainas)

with open("json/main.json","r") as f :
	file = json.load(f)
	file[numfat] = mainas
	
with open("json/main.json","w") as f :
	json.dump(file,f)
	
with open("json/emmar.json","r") as em :
	filem = json.load(em)
	filem[numfat] = reb
with open("json/emmar.json","w") as em :
	json.dump(filem,em)
	
with open("json/enfak.json","r") as en :
	filen = json.load(en)
	filen[numfat] = rea
with open("json/enfak.json","w") as en :
	json.dump(filen,en)
	
	
with open("json/adara.json","r") as ad :
	filead = json.load(ad)
	filead[numfat] = rec
with open("json/adara.json","w") as ad:
	json.dump(filead,ad)
