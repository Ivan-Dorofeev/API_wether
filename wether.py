import requests

svo = requests.get("https://wttr.in/svo?M?0?n&lang=ru")
london = requests.get("https://wttr.in/london?M?0?n&lang=ru")
cherepovets = requests.get("https://wttr.in/cherepovets?M?0?n&lang=ru")
print(svo.text, london.text, cherepovets.text)
