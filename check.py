import requests
from bs4 import BeautifulSoup
import yaml
from message import Messenger
import sys

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
if "Der er ingen igangværende udbud på medieområdet." in udbud[0].text:
    print("- Der er ingen aktuelle udbud.")
else:
    udbud_text = ""
    for u in udbud:
        print("-", u.text)
        udbud_text += u.text + "\n"

    udbud_text += "\n// XFM - SLKS"

    # Read config.yaml
    with open("config.yaml", "r") as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as exc:
            print("exc")
            sys.exit(-1)
    # Setup Texting
    msg = Messenger(twilio_acc = config["twilio"]["account"], twilio_token = config["twilio"]["token"], sender_name = config["twilio"]["sender"])

    # Send SMS to all receivers
    for receiver in config["twilio"]["receivers"]:
        print(f"Texting {receiver}.")
        msg.sms(receiver, f"Der er kommet udbud fra SLKS:\n\n{udbud_text}")

