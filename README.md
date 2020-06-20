# Rest-Api-Python
Rest Api (python)

Example:
User with name and surname

Source:
    .json file

### Routes:

| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |


| URL | Параметры | Описание |
| ------ | ------ |
| / | нет | возвращает всех пользователей в виде json |
| /user/<int:user_id> | id | возвращает конкретного пользователя по id
| /user/update | id, name, surname | изменяет пользователя
| /user/delete | id | удаляет пользователя
| /user/add | name, surname | добавляет пользователя
