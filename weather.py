import requests

cities = ['svo', 'london', 'cherepovets']
views_params = {'1': '', 'n': '', 'T': '', 'Q': '', 'lang': 'ru'}
for city in cities:
    response = requests.get(f"https://wttr.in/{city}", params=views_params)
    try:
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as exc:
        print(f'Неверно введён адрес запроса: \n{exc}')
    except requests.exceptions.ConnectionError as exc:
        print(f'Ошибка подключения: \n{exc}')
    except requests.exceptions.Timeout as exc:
        print(f'Долгое ожидание ответа от сервер: \n{exc}')
