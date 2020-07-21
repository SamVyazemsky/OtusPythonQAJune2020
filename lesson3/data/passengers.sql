CREATE TABLE passenger_info(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    surname VARCHAR NOT NULL,
    patronymic VARCHAR,
    phone VARCHAR NOT NULL,
    flight_num INTEGER NOT NULL,
    registration_date DATE  DEFAULT CURRENT_TIMESTAMP
);
