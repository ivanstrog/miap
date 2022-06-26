# miap
Мониторинг инновационной активности предприятий Оренбургской области



***Инструкция по запуску***

1) Cклонировать репозиторий, перейти в корневую директорию, далее продолжить в ветке main.
 
2) Необязательно (для корректной работы рекомендуется удалить sqlite-базу данных ```miap/backend/app.db```). Без этого пунтка storage пополняется не совсем корректно (не будет html доказательств для некоторых новостей)

3) Установить python зависимости из файла ```miap/backend/requirements.txt``` в используемое виртуальное окружение, при необходимости докачать необходимые
```pip install -r requirements.txt```

4) Запуск  backend-сервера просиходит из корневой директории прроекта miap
```python3 backend/main.py```

сервер работает на 8000 порту по адресу http://127.0.0.1:8000 , развернутое графическое апи находится по адресу http://127.0.0.1:8000/docs

5) Запуск фронтенд-сервера, происходит из папки ```miap/frontend```:
установить необходимые модули (нужно дополнительно доустановить модуль date-fns) 
```npm install```
```npm install --save date-fns```

запустить фрониенд-сервер 
```npm start``` , сайт запустится по адресу http://localhost:3000/  

6) Нажать кнопку "запустить парсеры" для обновление контента ресурса 
7) Приятного пользования! Команда NMBITS.
