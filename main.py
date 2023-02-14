import requests
from bs4 import BeautifulSoup
import lxml
import csv


headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    "Accept-Language" : "en-US,en;q=0.9"
}

URL = "https://baloncestoenvivo.feb.es/rankings/ligaeba/3/2022"

response = requests.get(url=URL, headers=headers)

website_html = response.text

soup = BeautifulSoup(website_html, "lxml")

header = []
rows = []

table = soup.find('table', id="_ctl0_MainContentPlaceHolderMaster_rankingAcumuladosDataGrid")


for i, row in enumerate(table.find_all('tr')):
    if i == 0:
        header = [x.text.strip() for x in row.find_all('th')]
    else:
        rows.append([x.text.strip() for x in row.find_all('td')])

print(header)
for row in rows:
    print(row)


file_title = "EBA Group A-A Points Rankings"

with open(file_title, "w", encoding="utf-8") as f:
    f.write = csv.writer(f)
    f.write.writerow(["No", header[1], header[2], header[3], header[4], header[5]])
    for a in range(len(rows)):
        f.write.writerow([rows[a]])
