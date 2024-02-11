# Проект Python Bootcamp Day 05
## Задание 1. Веб-интерфейс
### Способы запуска

#### 00: Скачивание

1 Клонируем репозиторий:

```git clone https://github.com/codesshaman/django_music_website.git```

2. Переходим в директорию задания:

``cd django_music_website``

#### 01: Docker

Оптимальный способ: запуск в Docker

1. Собираем проекта:

``make``

2. Переходим в браузере на сайт:

`` http://127.0.0.1:8888/``

#### 02: Python

Если есть python и нет докера, способ запуска следующий:

1. Переходим в директорию проекта:

``cd app/project/``

2. Создаём виртуальное окружение:

``make venv``

3. Устанавливаем зависимости:

``make req``

4. Запускаем проект:

``make``

5. Переходим в браузере на сайт:

`` http://127.0.0.1:8888/``

## Задание 2. API-интерфейс

Скрипт для тестирования API:

``screwdriver.py``

Не требует сторонних библиотек, работает на чистом python.

Вывести список всех имеющихся композиций:

``python3 screwdriver.py list``

Загрузить файл на сервер:

``python3 screwdriver.py upload 'File Name.mp3'``

После перезагрузки сайта файл появляется на странице.

В ряде случаев для воспроизведения может потребоваться
ещё одна перезагрузка страницы.

### Для тех, кому не повезло

Если вы айтишник, но по какому-то недоразумению

вынуждены запускать проект на windows, примите

мои соболезнования и не отчайвайтесь! Выход есть.

Следующие команды позволят запустить конфигурацию 

под системой мелкомягких:

#### Клонирование:

```git clone ssh://git@repos-ssh.21-school.ru:2289/students/Python_Bootcamp._Day_05.ID_877053/jleslee_student.21_school.ru/Python_Bootcamp.Day_05-1.git```

``cd Python_Bootcamp.Day_05-1/src/01``

#### Docker под wsl:

``docker-compose up -d --build``

#### Запуск через python:

``cd app/project/``

``python -m venv .venv``

``.\.venv\Scripts\activate``

``pip install -r ../requirements.txt``

``python.exe .\manage.py runserver 8888``

Дальше сайт можно открыть в браузере:

``http://127.0.0.1:8888/``
