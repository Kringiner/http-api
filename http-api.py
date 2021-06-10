import argparse
import requests
from config import VK_CONFIG
from tqdm import tqdm


def get_friend(user_id):
    text = make_vk_api(method='friends.get', user_id=user_id, fields='sex')
    answer = []
    body = text['response']['items']
    for i, user in enumerate(tqdm(body, ncols=100)):
        count = get_number_of_subscribers(user["id"])
        if count == -1:
            continue
        answer.append(
            (user['id'], f'{user["first_name"]} {user["last_name"]}', count))
    answer.sort(key=lambda x: (int(x[2])), reverse=True)
    return answer


def get_number_of_subscribers(user_id: int, fields=''):
    url = f'{VK_CONFIG["domain"]}/users.getFollowers?' \
          f'access_token={VK_CONFIG["access_token"]}' \
          f'&user_id={user_id}'
    url += f'&fields={fields}' if fields != '' else ''
    url += f'&v={VK_CONFIG["version"]}'
    response = requests.get(url)
    text = response.json()
    if 'error' in text:
        return -1
    return text['response']['count']


def make_vk_api(method: str, user_id: int, fields=''):
    url = f'{VK_CONFIG["domain"]}/{method}?' \
          f'access_token={VK_CONFIG["access_token"]}' \
          f'&user_id={user_id}'
    url += f'&fields={fields}' if fields != '' else      ''
    url += f'&v={VK_CONFIG["version"]}'
    response = requests.get(url)
    text = response.json()
    if 'error' in text:
        raise Exception(text['error']['error_msg'])
    return text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("user_id", help="Vk user id;", type=int)
    args = parser.parse_args()

    try:
        information = get_friend(user_id=args.user_id)
        for e in information:
            print(f'Id: {e[0]} Name: {e[1]} Followers:{e[2]}')
    except Exception as e:
        print(str(e))
