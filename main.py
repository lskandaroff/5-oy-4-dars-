import psycopg2
from collections import namedtuple

db = psycopg2.connect(
    database="amaliyot",
    user="postgres",
    host="localhost",
    password="1"
)

cursor = db.cursor()

# cursor.execute(
#     '''
#     drop table if exists cars
#     '''
# )
#
# cursor.execute('''
#     create table if not exists cars(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(150) NOT NULL,
#     model TEXT,
#     year INTEGER,
#     price NUMERIC(12, 2),
#     existent BOOL DEFAULT TRUE
#     );
# ''')


# cursor.execute('''
#     insert into cars(name, model, year, price) values
#     ('x7', 'BMW', '2022', 5000),
#     ('w200', 'Mers', '2023', 6000);
# ''')

# cursor.execute('''select * from cars''')
#
# cars = cursor.fetchall()
# print(cars)



#
# cursor.execute(
#     '''
#     drop table if exists clients
#     '''
# )
#
# cursor.execute('''
#     create table if not exists clients(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50) NOT NULL,
#     surname VARCHAR(50),
#     phone_number CHAR(13),
#     address TEXT
#     );
# ''')
#
#
# cursor.execute('''
#     insert into clients(name, surname, phone_number, address) values
#     ('Ali', 'Aliyev', 998945252, 'Quvasoy'),
#     ('Baxrom', 'Rozmatov', 899892023, 'Fergana');
# ''')
#
# cursor.execute('''select * from clients''')
#
# clients = cursor.fetchall()
# print(clients)


#
# cursor.execute(
#     '''
#     drop table if exists orders
#     '''
# )
#
# cursor.execute('''
#     create table if not exists orders(
#     id SERIAL PRIMARY KEY,
#     car_id INTEGER REFERENCES cars(id),
#     client_id INTEGER REFERENCES clients(id),
#     order_date DATE NOT NULL,
#     total_price NUMERIC(12, 2)
#     );
# ''')

# cursor.execute('''
#     insert into orders(order_date, total_price) values
#     (to_date('02.02.2024', 'dd.mm.yyyy'), 580000),
#     (to_date('03.02.2024', 'dd.mm.yyyy'), 600000);
# ''')
#
# cursor.execute('''select * from orders''')
#
# orders = cursor.fetchall()
# print(orders)

#
# cursor.execute(
#     '''
#     drop table if exists employees
#     '''
# )
#
# cursor.execute('''
#     create table if not exists employees(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50) NOT NULL,
#     position VARCHAR(50),
#     salary NUMERIC(12, 2)
#     );
# ''')

# cursor.execute('''
#     insert into employees(name, position, salary) values
#     ('vali', 'washer', 5000),
#     ('ali', 'manager', 10000);
# ''')

# cursor.execute('''
#     update employees set name = 'jalil' where id = 1;
#
# ''')
#
# cursor.execute('''
#     update employees set name = 'toxir' where id = 2;
#
# ''')
# #
# cursor.execute('''
#     delete from employees where id = 1;
# ''')
#
# cursor.execute('''select * from employees''')
#
# employees = cursor.fetchall()
# print(employees)



#
# cursor.execute('''
#     alter table clients
#     add column email VARCHAR(100)
# ''')

# cursor.execute('''
#     alter table clients
#     rename column name to ism;
# ''')

# cursor.execute('''
#     alter table clients
#     rename to kilentlar;
# ''')





db.commit()
db.close()










