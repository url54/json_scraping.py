# This program was created for an assignment.  The assignment requires us to visit and pull JSON data from a website.  Then to sum up all the integar values in that JSON
# file together.  The original instructions are included below this text.

# The program will prompt for a URL, http://py4e-data.dr-chuck.net/comments_1139135.json, read the JSON data from that URL using requests and then parse and extract the
# comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:


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
