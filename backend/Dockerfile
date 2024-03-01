# Выберите базовый образ
FROM python:3.11.7-slim

# Установите рабочий каталог внутри контейнера
WORKDIR /app

# Копируйте файлы зависимостей в рабочий каталог
COPY pyproject.toml poetry.lock* /app/

# Установите зависимости с помощью Poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-ansi

# Копируйте оставшиеся файлы проекта
COPY ./backend /app/
