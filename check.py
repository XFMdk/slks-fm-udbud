import requests
from bs4 import BeautifulSoup

slks_url = "https://slks.dk/medier/udbud-og-hoeringer/"

print(f"Finder høringer og udbud på SLKS: {slks_url}")
slks = requests.get(slks_url).text
soup = BeautifulSoup(slks, 'html.parser')
print()

horinger = soup.select("div#c128643 > div > p")
udbud = soup.select("div#c107615 > div > p")

print("Alle aktuelle høringer:")
for horing in horinger:
    print("-", horing.text)

print("Alle aktuelle udbud:")
for u in udbud:
    print("-", u.text)
