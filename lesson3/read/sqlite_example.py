import sqlite3
connect = sqlite3.connect('passengers.sqlite')

# with open('../data/passengers.sql', 'r') as file:
#     connect.execute(file.read())

# -----------------------------------------
# data = ('Иван', 'Тестовый', '9031456783', '12557')
# ins_str = f"INSERT INTO 'passenger_info' (name, surname,phone, flight_num) VALUES {data}"
# connect.execute(ins_str)
# connect.commit()


query = "SELECT * from passenger_info"
result = connect.execute(query)
headers = [i[0] for i in result.description]
for item in result.fetchall():
    print(dict(zip(headers, item)))


