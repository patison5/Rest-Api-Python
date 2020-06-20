# Rest-Api-Python
Rest Api (python)

Example:
User with name and surname

Source:
    .json file

Routes:
/ - list all users

/user/<int:user_id> - list user with special id

/user/update - update user with special id (param: id, name, surname)

/user/delete - delete with special id (param: id)

/user/add - add new user (param: name, surname)