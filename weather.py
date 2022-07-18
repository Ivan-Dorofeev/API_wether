import requests

cities = ['svo', 'lond232on', 'cherepovets']
data = {'?M': '', '?1': '', '?n': '', '?T': '', '?Q': '', 'lang': 'ru'}
for city in cities:
    response = requests.get(f"https://wttr.in/{city}", params=data)
    try:
        if response.raise_for_status() is None:
            print(response.text)
    except Exception as exc:
        print(f'При запросе возникла ошибка: \n{exc}')
