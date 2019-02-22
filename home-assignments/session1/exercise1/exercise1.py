import json
import yaml
from pprint import pprint
with open ('my_list.json') as f:
	data = json.load(f)
buckets = data["buckets"]
ppl_ages = data["ppl_ages"]
temp = []
answer = {}
max_age = max(ppl_ages.values())
sorted_buckets = sorted(buckets)
current = 0
next = sorted_buckets[0]
results = []
for p in ppl_ages:
	age = ppl_ages[p]
	if age >= current and age < next:
		results.append(p)
	elif (age >= current and age == max_age and age == next):
		results.append(p)

answer[str(current)+"-"+str(next)] = results

for i in range(len(sorted_buckets)):
	results = []
	if i+1 < len(sorted_buckets):
		current = sorted_buckets[i]
		next = sorted_buckets[i+1]
	else:
		current = sorted_buckets[i]
		next = max_age
	for p in ppl_ages:
		age = ppl_ages[p]
		if age >= current and age < next:
			results.append(p)
		elif (age >= current and age == max_age and age == next):
			results.append(p)

	answer[str(current)+"-"+str(next)] = results
print(answer)

with open ('my_list.yaml','w') as outfile:
	yaml.dump(answer, outfile, default_flow_style=False)