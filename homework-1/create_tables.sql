CREATE TABLE customers (
    customer_id varchar(10) PRIMARY KEY NOT NULL,
    company_name varchar(50),
    contact_name varchar(50)
);
CREATE TABLE employees(
  emploee_id int PRIMARY KEY NOT NULL,
  first_name varchar(50),
  last_name varchar(50),
  title varchar(150),
  birth_date date,
  notes text
);
CREATE TABLE orders(
    order_id int PRIMARY KEY,
    customer_id  varchar(10) REFERENCES customers(customer_id) NOT NULL,
    employee_id  int REFERENCES employees(emploee_id) NOT NULL,
    order_date date,
    ship_sity varchar(255)
);
