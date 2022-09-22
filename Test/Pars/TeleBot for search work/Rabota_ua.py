import requests
import json


def wac():
    headers = {
        'Host': 'dracula.rabota.ua',
        # 'Content-Length': '1221',
        'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="104"',
        'Accept': 'application/json, text/plain, */*',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'Accept-Language': 'uk',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Origin': 'https://rabota.ua',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://rabota.ua/ua/zapros/junior-python-developer/%D1%83%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0',
        # 'Accept-Encoding': 'gzip, deflate',
    }
    params = {
        'q': 'getPublishedVacancies',
    }
    json_data = {
        'operationName': 'getPublishedVacancies',
        'variables': {
            'filter': {
                'keywords': 'junior python developer',
                'showWithoutSalary': True,
                'showAgencies': True,
            },
            'pagination': {
                'count': 40,
                'page': 0,
            },
        },
        'query': 'query getPublishedVacancies($filter: PublishedVacanciesFilterInput!, $pagination: PublishedVacanciesPaginationInput) {\n  publishedVacancies(filter: $filter, pagination: $pagination) {\n    ...VacanciesList\n    __typename\n  }\n}\n\nfragment VacanciesList on PublishedVacancies {\n  totalCount\n  items {\n    ...Vacancy\n    __typename\n  }\n  __typename\n}\n\nfragment Vacancy on Vacancy {\n  __typename\n  id\n  schedules {\n    id\n    __typename\n  }\n  title\n  description\n  sortDateText\n  hot\n  designBannerUrl\n  badges {\n    name\n    __typename\n  }\n  salary {\n    amount\n    comment\n    amountFrom\n    amountTo\n    __typename\n  }\n  company {\n    ...Company\n    __typename\n  }\n  city {\n    id\n    name\n    __typename\n  }\n  showProfile\n  seekerFavorite {\n    isFavorite\n    __typename\n  }\n  seekerDisliked {\n    isDisliked\n    __typename\n  }\n  formApplyCustomUrl\n  anonymous\n  isActive\n  publicationType\n}\n\nfragment Company on Company {\n  id\n  logoUrl\n  name\n  __typename\n}\n',
    }
    response = requests.post(
        'https://dracula.rabota.ua/',
        params=params,
        headers=headers,
        json=json_data,
        verify=False)
    with open(file='text.json', mode="w", encoding="windows-1251") as file:
        file.write(response.text)


list2 = []


def search():
    with open("text.json", "r", encoding="windows-1251") as f:
        file_content = f.read()
        templates = json.loads(file_content)
        items_list = templates['data']['publishedVacancies']['items']
        for item in items_list:
            result = f'https://rabota.ua/ua/company{item["company"]["id"]}/vacancy{item["id"]}'
            title_result = item["title"]
            list2.append(title_result + ' ' + result)


wac()
search()
