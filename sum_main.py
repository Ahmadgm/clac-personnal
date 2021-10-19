import json
i = 0
with open("json/main.json","r") as f :
	file = json.load(f)
for x in file:
	majmoa = file[x]
	i += int(majmoa)

print(i)
