import requests


def main():
    cities = ['svo', 'london', 'cherepovets']
    cities_view_params = {'nTqM': '', 'lang': 'ru'}
    for city in cities:
        response = requests.get(f"https://wttr.in/{city}", params=cities_view_params)
        try:
            response.raise_for_status()
            print(response.text)
        except requests.exceptions.HTTPError as exc:
            print(f'Неверно введён адрес запроса: \n{exc}')


if __name__ == '__main__':
    main()
