from flask import Flask
from flask import request
import json

app = Flask(__name__)

def save_data(data, filename="restApi.json"):  # Функция сохранения базы в txt файле
    with open(filename, "w") as file:  # Открываем файл на запись
        # json.dump(data, file)
        data = json.dumps(data, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        file.write(data)

def read_data():
    with open('restApi.json') as json_file:
        return json.load(json_file)

# всю эту хуйню можно записывать и читат из файла.
class Users:
    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname

    #  советуют также искользовать jsonpickle - более удобный инструмент сериализации в JSON
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def findUserById (id):
    users = read_data()['users']
    for user in users:
        if user['id'] == int(id):
            return user

# чисто для демонстрации добавил эти строки...
usersList = {}
usersList["users"] = []
usersList["users"].append(Users(0, "Misha", "Pidor"))
usersList["users"].append(Users(1, "Fedor", "Krasauchik"))

save_data(usersList)
read_data()


@app.route('/')
def hello_world():
    return read_data()

# http://127.0.0.1:5000/post/2 - на экране выведет значение Post 2... получая id как параметр можно более детально настроить выборку элементов/удаление
@app.route('/user/<int:user_id>')
def show_post(user_id):
    # вывести сообщение с данным
    for user in read_data()["users"]:
        if user['id'] == int(user_id):
            return user
    return f"No user with {user_id} found"


@app.route('/user/update', methods=['POST'])
def login():
    if request.method == 'POST':
        print(request.get_json())
        id = request.args.get('id')
        name = request.args.get('name')
        surname = request.args.get('surname')

        if not id:
            return "error, no id sended"

        filedata = read_data()
        users = filedata['users']
        for user in users:
            if user['id'] == int(id):
                if name:
                    user['name'] = name
                if surname:
                    user['surname'] = surname

        save_data(filedata)
        return f"User #{id} was updated"


# не претендую на "гениальность" но сук простой ремув не сработал, я не ебал мозг, подправь плиз
@app.route('/user/delete', methods=['POST'])
def delete_user():
    user_id = request.args.get('id')
    filedata = read_data()

    for user in filedata["users"]:
        if user['id'] == int(user_id):
            filedata['users'].remove(user)
            save_data(filedata)
            return f'User {user_id} was deleted.'

    return f"No user with {user_id} found"


@app.route('/user/add', methods=['POST'])
def user_add():
    if request.method == 'POST':
        name = request.args.get('name')
        surname = request.args.get('surname')

        filedata = read_data()
        filedata["users"].append(Users(len(filedata["users"]), name, surname))
        save_data(filedata)

        return f"User {name} {surname} [{len(filedata['users']) - 1}] was added"


if __name__ == '__main__':
    app.run()

