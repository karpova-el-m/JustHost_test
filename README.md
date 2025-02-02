# Управление VPS (VPS API)

## Задача:

Разработайте REST-сервис для управления виртуальными серверами (VPS) с использованием Django Rest Framework (DRF).

### Объект VPS должен включать следующие параметры:

* uid — уникальный идентификатор сервера.
* cpu — количество процессорных ядер.
* ram — объем оперативной памяти.
* hdd — объем дискового пространства.
* status — текущий статус сервера (например, started, blocked, stopped).

### API должно предоставлять следующие возможности:

* Создание нового виртуального сервера.
* Получение данных о конкретном сервере по его uid.
* Вывод списка всех серверов с поддержкой фильтрации по заданным параметрам.
* Изменение статуса сервера (например, перевод в состояния started, blocked, stopped).

## Обзор:
Этот проект представляет собой RESTful API для управления виртуальными серверами (VPS) с использованием Django Rest Framework (DRF) и JWT-аутентификации.

## Функционал
- Создание нового VPS
- Получение информации о конкретном VPS
- Вывод списка всех VPS с возможностью фильтрации, сортировки и поиска
- Изменение статуса VPS (`started`, `blocked`, `stopped`)
- Аутентификация на основе JWT для защиты API

### Стек:
- Python 3.8+
- Django 4+
- Django Rest Framework
- Django SimpleJWT

## Установка

### Инструкции по установке
1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/karpova-el-m/JustHost_test
   cd JustHost_test
   ```
2. Создайте и активируйте виртуальное окружение:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Установите зависимости:
   ```sh
   cd justhost
   pip install -r requirements.txt
   ```
4. Выполните миграции базы данных:
   ```sh
   python3 manage.py migrate
   ```
5. Создайте суперпользователя:
   ```sh
   python3 manage.py createsuperuser
   ```
6. Запустите сервер разработки:
   ```sh
   python3 manage.py runserver
   ```

## API Эндпоинты

### Аутентификация

- Создание нового пользователя:
  ```
  POST /api/auth/users/
  {
      "username": "admin",
      "password": "password"
  }
  ```
- Получение JWT-токена:
  ```
  POST /api/auth/jwt/create/
  {
      "username": "admin",
      "password": "password"
  }
  ```
- Обновление JWT-токена:
  ```
  POST /api/auth/jwt/refresh/
  {
      "refresh": "your_refresh_token"
  }
  ```

### Управление VPS
- Получение списка всех VPS:
  ```
  GET /api/vps/
  ```
- Фильтрация по параметрам (CPU, RAM, HDD, статус):
  ```
  GET /api/vps/?cpu=4&ram=8192&status=started
  ```
- Сортировка по параметрам:
  ```
  GET /api/vps/?ordering=cpu  # по возрастанию CPU
  GET /api/vps/?ordering=-ram  # по убыванию RAM
  ```
- Поиск по UID:
  ```
  GET /api/vps/?search=12345
  ```
- Получение информации о конкретном VPS:
  ```
  GET /api/vps/{uid}/
  ```
- Создание нового VPS:
  ```
  POST /api/vps/
  {
      "cpu": 4,
      "ram": 8192,
      "hdd": 200,
      "status": "stopped"
  }
  ```
- Изменение статуса VPS:
  ```
  PATCH /api/vps/{uid}/change_status/
  {
      "status": "started"
  }
  ```

## Запуск тестов
Для запуска тестов выполните команду:
```sh
python3 manage.py test
```

### Проект разработала:

Карпова Е.М. - https://github.com/karpova-el-m
