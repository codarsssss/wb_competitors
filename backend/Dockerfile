# Используем базовый образ Python
FROM python:3.11.7-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем poetry
RUN pip install poetry

# Копируем файлы проекта в контейнер из текущей директории, где находится Dockerfile
COPY . .

# Устанавливаем зависимости через poetry без создания виртуального окружения
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Открываем порт 8001 для внешних подключений к серверу
EXPOSE 8001

# Запускаем Daphne с нашим ASGI приложением
CMD ["poetry", "run", "daphne", "-p", "8001", "-b", "0.0.0.0", "backend.asgi:application"]
