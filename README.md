# http-api

Задача из курса Протоколы интернет Http-api 
10) Топ друзей по числу подписчиков 

### Перед запуском 
Надо заполнить config.py
1) app_id - id моего приложения (будет в сообщении)
2) access_token - токен доступа.

для получения токена дступа 
 1) Запуск скрипта:
      ```
      python access_token.py
      ```
 2) Далее появиться окно, где нужно будет разрешить приложению получать информацию о друзьях.
 3) Там же надо будет скопировать токен доступа в конфиг

### Установка требований для работы прогресс бара и вк апи
```
pip install -r requirements.txt
```

### Работа
```
(venv) C:\Users\Loliconshik\PycharmProjects\http-api>python http-api.py 236664271
100%|█████████████████████████████████████████████████████████████| 125/125 [00:22<00:00,  5.62it/s]
Id: 137000201 Name: Кирилл Ширяев Followers:684
Id: 114111669 Name: Назар Горкунов Followers:611
Id: 241959796 Name: Ольга Субачева Followers:565
....
```


