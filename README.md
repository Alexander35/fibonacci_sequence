# Генератор последовательности Фибоначчи

для запуска нужно:
установить redis 
переименовать файл .config.json в config.json и назначить все переменные
запустить сервер 

```
python http_server.py
```
запустить юнит-тесты
в файлах *_tests.py содержатся юнит тесты

для работы с приложением нужно отправить GET  запрос 
```
http://localhost:8000/fibonachi?from=1&to=30
http://localhost:8000/get-sequence?from=1&to=30
```
первый генерирует последовательнсоть, второй показывают существующую в хранилище.

## Для развёртывания в docker

создать image 
```
docker build -t alexander/fibonacci_secuence .
```

запустить docker-compose

```
docker-compose up
```

при этом будут запущены два контейнера (один с redis, второй с alexander/fibonacci_secuence)

при этом сервис будет доступен на 80 порту сервера.