import requests
import json
import re

r = requests.get("http://py4e-data.dr-chuck.net/comments_1139135.json")
res = r.json()

nmlst = list()

# Dump data as string
data = json.dumps(res)
for dat in data.split():
    nms = re.findall('([0-9]+)', dat)
    nlist = [int(i) for i in nms]
    if len(nlist) == 0:
        continue
    nmlst.append(sum(nlist))
print(sum(nmlst))
