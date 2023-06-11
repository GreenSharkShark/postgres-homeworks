import psycopg2
import csv


def insert_values_in_table_customers():
    conn = psycopg2.connect(host='localhost', port='5433', database='north', user='ZhorikZeniuk', password='cucumber1l')
    try:
        with conn:
            with conn.cursor() as cur:
                with open('north_data/customers_data.csv') as file:
                    content = csv.DictReader(file)
                    for row in content:
                        try:
                            cur.execute('INSERT INTO customers VALUES (%s, %s, %s)',
                                        (row['customer_id'], row['company_name'], row['contact_name']))
                        except psycopg2.errors.UniqueViolation:
                            print('Ошибка транзакции, транзакция отменена.')
                            conn.rollback()
                            continue
    finally:
        conn.close()


def insert_values_in_table_employees():
    conn = psycopg2.connect(host='localhost', port='5433', database='north', user='ZhorikZeniuk', password='cucumber1l')
    try:
        with conn:
            with conn.cursor() as cur:
                with open('north_data/employees_data.csv') as file:
                    content = csv.DictReader(file)
                    for row in content:
                        try:
                            cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                                        (row['employee_id'], row['first_name'], row['last_name'],
                                         row['title'], row['birth_date'], row['notes']))
                        except psycopg2.errors.UniqueViolation:
                            print('Ошибка транзакции, транзакция отменена.')
                            conn.rollback()
                            continue
    finally:
        conn.close()


def insert_values_in_table_orders():
    conn = psycopg2.connect(host='localhost', port='5433', database='north', user='ZhorikZeniuk', password='cucumber1l')
    try:
        with conn:
            with conn.cursor() as cur:
                with open('north_data/orders_data.csv') as file:
                    content = csv.DictReader(file)
                    for row in content:
                        try:
                            cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                                        (row['order_id'], row['customer_id'], row['employee_id'],
                                         row['order_date'], row['ship_city']))
                        except psycopg2.errors.UniqueViolation:
                            print('Ошибка транзакции, транзакция отменена.')
                            conn.rollback()
                            continue
    finally:
        conn.close()


if __name__ == '__main__':
    insert_values_in_table_customers()
    insert_values_in_table_employees()
    insert_values_in_table_orders()
