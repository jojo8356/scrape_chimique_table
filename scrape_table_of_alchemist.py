import requests
from bs4 import BeautifulSoup as bs
import re

atomes, masses = [], []
table = {}
url = "https://fr.wikipedia.org/wiki/Liste_des_%C3%A9l%C3%A9ments_chimiques"
response = requests.get(url)
soup = bs(response.text, "html.parser")
body = soup.find("tbody")
tr = body.find_all("tr")

for x in tr:
    td = x.find_all("td")
    try:
        atomes.append(td[2].text)
        liste = td[3].text.split(" ")
        masses.append(liste[0].encode("utf-8").decode("utf-8").replace("\xa0", " "))
    except:
        pass

for x in range(len(masses)):
    masses[x] = round(float(masses[x].split(" ")[0].replace(",",".")))
for x in range(len(atomes)):
    table[atomes[x]] = masses[x]

print("quel est ta molécule")
molecule = str(input())
compo = re.findall('[A-Z][^A-Z]*', molecule)
result = 0

for x in compo:
    positions = [match.start() for match in re.finditer(r'\d+', x)]
    positions = [0] + positions + [len(x)]
    y = [x[positions[i]:positions[i+1]] for i in range(len(positions)-1)]
    if len(y) >= 2:
        result += table[y[0]]*int(y[1])
    else:
        result += table[y[0]]

print(str(result)+" g/mol")
