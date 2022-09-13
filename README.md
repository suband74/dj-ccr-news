# Реализован REST backend с использование DRF (Django Rest Framework) новостного приложения:
1. `api/v1/types/` - Create, Read типов новостей;
2. `api/v1/types/<id_of_news>` - Update, Delete типов новостей;
3. `api/v1/news/` - Create, Read новостей;
4. `api/v1/news/<id_of_news>` - Update, Delete новостей;
3. `api/v1/allnews/` - GET-запрос, получить список всех новостей (имя, краткое описание, имя типа, цвет типа);
4. `api/v1/getnews/<type_of_news>/` - GET-запрос, получить список новостей определенного типа.


## Установка проекта на локальный компьютер:

4. Клонировать репозиторий:

```
https://github.com/suband74/dj-ccr-news.git
```

7. Установить docker и docker-compose. Инструкции по установке доступны в официальной документации.

8. В папке с проектом выполнить команду:

```
docker-compose up
```