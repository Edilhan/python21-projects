def generate_id(ids):
    """
    Принимает список сущ id_
    Возвращ нов id_ в диап 100 до 1000
    """
    import random
    id_ = random.randint(100,1000)
    while id_ in ids:
        id_ = random.randint(100,1000)
    return id_

def validate_passwords(p1,p2):
    """
    Принимает 2 пароля если они не совпадают выдает ошибку
    """
    if p1 != p2:
        raise Exception('Пароли не совпадают')

def validate_id(ids,u_id):
    """
    Принамает список существующих id и id, которое нужно проверить
    Если такого нет вызывает Exception
    """
        
    if u_id not in database:
        raise Exception("Такого юзера нет")

def read_db(name):
    """
    Принимает название файла
    Возвращает данные из бд в виде python обьектов
    """
    import json
    with open(name, "r") as file:
        db = json.load(file)
    return db

def write_to_db(name, data):
    """
    Принимает название файла и данные для записи
    Записывает эти данные в файл
    """
    import json
    with open(name, "w") as file:
        json.dump(data, file)
