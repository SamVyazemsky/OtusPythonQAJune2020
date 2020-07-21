from json import dumps

j = {
    "users": [
        {
            "first_name": "Ivan",
            "last_name": "Ivanov",
            "email": "ivanov@mail.ru",
            "city": "Moscow",
            "zip_code": 12345,
            "phone": None
        },
        {
            "first_name": "Artem",
            "last_name": "Efimov",
            "email": "test@ya.ru",
            "city": "Tver",
            "zip_code": 234564,
            "phone": None
        },
        {
            "first_name": "Maria",
            "last_name": "Bug",
            "email": "test100500@mail.ru",
            "city": "Sochi",
            "zip_code": 23537,
            "phone": None
        }
    ]
}

with open('new_json.json', 'w') as file:
    s = dumps(j, indent=4)
    file.write(s)
