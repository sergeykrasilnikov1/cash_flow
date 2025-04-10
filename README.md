# Cash Flow Management System

Система управления движением денежных средств (ДДС).

## Возможности

- Создание, редактирование и удаление записей о движении денежных средств
- Фильтрация записей по дате, статусу, типу, категории и подкатегории
- Управление справочниками (статусы, типы, категории, подкатегории)
- Валидация данных на стороне клиента и сервера

## Требования

- Python 3.10+
- Docker и Docker Compose (для запуска через Docker)

## Установка и запуск

### Локальная установка

0. Склонируйте репозиторий:
 ```bash
 git clone https://github.com/sergeykrasilnikov1/cash_flow.git
cd cash_flow
```
2. Создайте виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate  # для Linux/Mac
# или
.venv\Scripts\activate  # для Windows
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Примените миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

5. Запустите сервер разработки:
```bash
python manage.py runserver
```

### Запуск через Docker

1. Скопируйте файл .env.example в .env:
```bash
cp .env.example .env
```

2. Отредактируйте файл .env:
```bash
# Django settings
DEBUG=1  # Установите 0 для production
SECRET_KEY=your-secret-key-here  # Замените на ваш секретный ключ

# Database settings
DATABASE_URL=sqlite:///db.sqlite3

```

3. Соберите и запустите контейнеры:
```bash
docker-compose up --build
```

4. Создайте суперпользователя:
```bash
docker-compose exec web python manage.py createsuperuser
```

Приложение будет доступно по адресу: http://localhost:8000

