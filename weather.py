import requests

cities = ['svo', 'london', 'cherepovets']
# views_params = {'1': '', 'n': '', 'T': '', 'Q': '', 'lang': 'ru'}
views_params = {'1nTQ': '', 'lang': 'ru'}
for city in cities:
    response = requests.get(f"https://wttr.in/{city}", params=views_params)
    print(response.url)
    try:
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as exc:
        print(f'Неверно введён адрес запроса: \n{exc}')
