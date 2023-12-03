# Блог-платформа #

Блог-платформа - это социальная сеть для публикации личных дневников, созданная для обмена записями между пользователями. <br>
Мой проект представляет API для платформы создания постов, общения и обмена мнениями. Поддерживает создание личных дневников, публикацию постов, комментирование их, подписку на других авторов, управление своими записями и профилем.

## Стек технологий ##
+ Python 3.10.10
+ Django 3.2
+ Django REST Framework 3.12
+ Pillow
+ JWT
+ Postman

## Установка
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Mary8jk/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
