#HT_20


## Запуск Redis

1. Встановіть залежності, які вказані в файлі `requirements.txt`:
    ```shell
    pip install -r requirements.txt
    ```

2. Створіть файл docker-compose.yml з таким змістом:
    ```shell
    version: '3'

    services:
      redis:
        image: "redis:latest"
        ports:
          - "6379:6379"
        volumes:
          - ./redis-data:/data
        command: ["redis-server", "--appendonly", "yes"]
    ```
    У вас він вже має бути створеним

3. Відкрийте термінал та перейдіть до папки в якій міститься файл `manage.py`.
4. Виконайте наступні команди, щоб запустити ваш додаток в Docker:
    ```shell
    docker-compose build
    ```
    Далі
    ```shell
    docker-compose up
    ```
    Ви побачите вивід, що додаток запущено і доступний за адресою http://localhost:6379.
5. Далі створіть файл `.env` зразок доступний в `.env.sample`
    Зазвичай REDIS_HOST це `localhost` а REDIS_PORT це `6379` але якщо ви щось змінили то також змініть і в .env
6. Щоб зупинити додаток та контейнер, виконайте команду:
    ```shell
    docker-compose stop
    ```
    Це зупинить додаток та контейнер.

## Запуск Celery
1. Для того, щоб запустити `Celery` введіть команду
    ```shell
    celery -A your_project worker -l info
    ```
    Де `your_project` це назва проекту в цьому випаду `scrapingsite`


## Запуск Django
1. Для запуска Django просто пропишіть команду
    ```shell
    python manage.py runserver
    ```
    При цьому ви маєте знаходитись в потрібній дерикторії вона наведена вище