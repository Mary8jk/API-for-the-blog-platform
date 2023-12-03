# Блог-платформа #

<p>Блог-платформа - это социальная сеть для публикации личных дневников, созданная для обмена записями между пользователями. <br>
<p>Мой проект представляет API для платформы создания постов, общения и обмена мнениями. Поддерживает создание личных дневников, публикацию постов, комментирование их, подписку на других авторов, управление своими записями и профилем.

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
git clone git@github.com:Mary8jk/API-for-the-blog-platform.git
```

```
cd API-for-the-blog-platform
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
