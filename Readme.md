## Проект Python Bootcamp Day 05

### Способы запуска

#### 00: Скачивание

1 Клонируем репозиторий:

```git clone ssh://git@repos-ssh.21-school.ru:2289/students/Python_Bootcamp._Day_05.ID_877053/jleslee_student.21_school.ru/Python_Bootcamp.Day_05-1.git```

2. Переходим в директорию задания:

``cd Python_Bootcamp.Day_05-1/src/01``

#### 01: Docker

Оптимальный способ: запуск в Docker

1. Собираем проекта:

``make``

2. Переходим в браузере на сайт:

`` http://127.0.0.1:8008/``

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

`` http://127.0.0.1:8000/``
