1-qadam: 
CREATE TABLE airports (id SERIAL PRIMARY KEY, name VARCHAR(100), city VARCHAR(60));

CREATE TABLE flights (id SERIAL PRIMARY KEY,flight_number VARCHAR(20),departure_airport_id INT REFERENCES airports(id),arrival_airports_id INT REFERENCES airports(id),departure_time TIMESTAMP,price NUMERIC(10,2),seats_available INT);

CREATE TABLE passengers (id SERIAL PRIMARY KEY, full_name VARCHAR(100), phone VARCHAR(20));

CREATE TABLE bookings ( id SERIAL PRIMARY KEY, flight_id INT REFERENCES flights(id), passenger_id INT REFERENCES passengers(id), booking_date DATE DEFAULT CURRENT_DATE, seats_booked INT
);


2-Qadam
INSERT INTO airports (name, city) VALUES ('Toshkent xalqaro aeroporti', 'Toshkent'),('Lissabon xalqaro aeroporti', 'Lissabon'),('Kinshasa xalqaro aeroporti', 'Kinshasa'),('Bagota xalqaro aeroporti', 'Bagota');

INSERT INTO flights (flight_number, departure_airport_id, arrival_airports_id, departure_time, price, seats_available) VALUES ('HY101', 1, 2, '2025-07-01 08:00:00', 850.00, 120),('HY202', 1, 3, '2025-07-02 10:30:00', 920.00, 90),('HY303', 1, 4, '2025-07-03 14:00:00', 880.00, 200),('HY404', 2, 3, '2025-07-04 06:45:00', 600.00, 150),('HY505', 4, 1, '2025-07-05 19:00:00', 870.00, 180);

INSERT INTO passengers (full_name, phone) VALUES('Eldor Shomurodov', '+998901234567'),('Cristiano Ronaldo', '+351901234568'),('Cedric Bakambu', '+243901234569'),('James Rodriguez', '+571901234570'),('Abbosbek Fayzullayev', '+998901234571');

INSERT INTO bookings (flight_id, passenger_id, seats_booked) VALUES(1, 1, 2),(2, 2, 1),(3, 4, 3),(4, 5, 1);

UPDATE flights SET price = 950.00 WHERE flight_number = 'HY101';

DELETE FROM passengers WHERE id = 5;


3-qadam:
ALTER TABLE flights ADD COLUMN status VARCHAR(20) DEFAULT 'rejalashtirilgan';


4-Qadam

SELECT f.flight_number,a.name,a.city,A1.name,A1.city FROM flights f INNER JOIN airports a ON f.departure_airport_id=a.id INNER JOIN ai
rports A1 ON f.arrival_airports_id=A1.id;

SELECT f.flight_number,p.full_name, b.booking_date, b.seats_booked FROM bookings b INNER JOIN passengers p ON b.passenger_id=p.id INNE
R JOIN flights f ON b.flight_id=f.id;


5-qadam:
CREATE USER booking_agent WITH PASSWORD 'kuchli_parol123';
GRANT SELECT, INSERT ON flights, bookings TO booking_agent;


