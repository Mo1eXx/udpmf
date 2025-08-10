# СПРАВОЧНИК
***

## Для запуска проекта:
- клонировать репозиторий на боевой сервер
- запустить докер композ командой ```sudo docker compose -f docker-compose.production.yml pull```
- запустить контейнер ```sudo docker compose -f docker-compose.production.yml up -d```
- выполнить миграции ```sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate```
- создать суперпользователя ```sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser```

***

Проект создан при использовании python Django, csrf, nginx, docker, docker-compose, html5, java script, postgresql
