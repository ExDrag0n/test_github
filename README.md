# Проект тестирования GitHub API

Этот проект демонстрирует автоматическое тестирование работы с GitHub API на языке Python. Тест способен создавать, проверять наличие и удалять репозиторий на GitHub.

## Установка

1. Склонируйте репозиторий:

    git clone https://github.com/ExDrag0n/test_github cd github-api-test
2. Установите зависимости:

    pip install -r requirements.txt
3. Скопируйте пример файл конфигурации окружения:
    cp .env .env
4. Отредактируйте файл `.env`, заполнив следующие переменные:
   - `GITHUB_USERNAME`: Ваш логин GitHub
   - `GITHUB_TOKEN`: Ваш персональный токен доступа GitHub
   - `REPO_NAME`: Имя нового репозитория (например, "test-repo")

## Запуск тестов
Для запуска тестов просто выполните команду:

    python test_api.py


Скрипт создаст новый публичный репозиторий, проверит его наличие и затем удалит его.

## Проверка результатов

После запуска теста вы можете проверить результаты на вашем аккаунте GitHub:
1. Перейдите в раздел "Repositories" (Репозитории)
2. Найдите созданный тестовый репозиторий по имени, указанному в переменной REPO_NAME
3. Убедитесь, что репозиторий был создан и успешно удален

## Требования к проекту

- Python 3.8+
- Библиотеки: requests, python-dotenv

## Примечания

- Используйте персональный токен доступа GitHub с необходимыми разрешениями для создания и удаления репозиториев.
- Созданный репозиторий будет иметь имя, указанное в переменной REPO_NAME из файла .env.
- После запуска теста убедитесь, что у вас есть доступ к интернету для выполнения запросов к API GitHub.

## Диагностика

Если вы столкнетесь с какими-либо трудностями:
1. Убедитесь, что ваш токен GitHub имеет необходимые разрешения.
2. Проверьте, что имя репозитория не повторяет имя уже существующего репозитория на вашем аккаунте.
