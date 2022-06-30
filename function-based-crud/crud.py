# CRUD
# Create
# Read
# Update
# Delete

from utils import validate_id, read_db, write_to_db

database = { #read_db(db.json)
    "Бекзат": "скала",
    "Эртай": "пароль",
    "Оомат": "Кыргызстан",
    "Имран": "12345",
    "Жийде": "return",
    "Манас": "Маке",
    "Арафат": "54321",
    "Элжаз": "парол",
    "Гулсана": "312",
    "Эркайым": "Айдин",
    "Бекназ": "Арёль",
    "Эдиль": "ьлорап",
    "Айгул": "май",
    "Закир": "@@@",
    "Бегайым": "makers",
    "Мырзайым": "Bootcamp2221",
    "Даниэл": "covid19",
    "Жибек": "1404",
    "Калысбек": "стол",
    "Ырыс": "suuuuuuuuiiiiiiiiiiii",
    "Айканыш": "qwerty",
    "Арген": "11172332",
    "Нурмухамед": "Не верный",
    "Бектур": "0101",
    "Алан": "душу питона",
    "Жаангер": "ох блин",
    "Богдан": "Кудайберген",
    "Айгерим": "синий маркер",
    "Настя": "Python21"
}
import random
ids = []
for key, value in database.copy().items():
    id_ = random.randint(100,999)
    while id_ in ids:
        id_ = random.randint(100,999)
    ids.append(id_)
    database[id_] = {
        'name':key,
        'password':value,
        'info':'...'

    }
    del database[key]
print(database)

def read(u_id):
    """
    Принимает id юзера
    Выводит его имя  и информацию
    Если такого нет вызывается exeption
    """

    if u_id not in database:
        raise Exception("Такого юзера нет")
    name = database[u_id]['name']
    info = database[u_id]['info']
    print(f"""
    ========={u_id}======
    Name: {name}
    Info: {info}
    =====================
    """)
def create():
    from utils import generate_id, validate_passwords
    name = input("Введите имя: ")
    password = input('Введите пароль: ')
    password2 = input('Введите подтверждение пароля: ')
    validate_passwords(passwords,password2)
    info = input('Введите инфу о вас: ')
    id_= generate_id(database.keys())
    database[id_] = {
        "name":name,
        "password":password,
        "info":info
    }
    print("Вы были добавлены в Python21")

def delete(u_id):
    validate_id(database.keys(), u_id)
    name = database[u_id]["name"]

    del database[u_id]
    print(f"{name} был успешно удален")

def update(u_id):
    validate_id(database.keys(), u_id)
    read(u_id)
    name = input("Введите имя: ")
    info = input('Введите инфу о вас: ')
    database[u_id]["name"] = name
    database[u_id]["info"] = info
    read(u_id)