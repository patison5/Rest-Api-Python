# Rest-Api-Python
Rest Api (python)

### Example:

source file: restApi.json

```sh
{
    "users": [
        {
            "id": 0,
            "name": "Misha",
            "surname": "Pidor"
        },
        {
            "id": 1,
            "name": "Fedor",
            "surname": "Krasauchik"
        }
    ]
}
```

### Routes:

| URL | Параметры | Описание |
| :---         | :---         | :---         |
| /   | нет     |  возвращает всех пользователей в виде json    |
| /user/\<int:user_id\>     | id       | возвращает конкретного пользователя по id      |
| /user/update   | id, name, surname     | изменяет пользователя    |
| /user/delete   | id     | удаляет пользователя    |
| /user/add   | name, surname     | добавляет пользователя    |
