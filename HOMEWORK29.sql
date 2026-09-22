-- შექმენით ორი ნებისმიერი ცხრილი, ერთმანეთთან რომ ჰქონდეთ კავშირი

-- CREATE TABLE departments (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(100) NOT NULL
-- );

-- CREATE TABLE employees (
--     id SERIAL PRIMARY KEY,
--     first_name VARCHAR(50) NOT NULL,
--     last_name VARCHAR(50) NOT NULL,
--     department_id INT REFERENCES departments(id),
--     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- შექმენით ვიუ, რომელიც ერთ-ერთი ცხრილიდან ყველა მონაცემის წამოღებას ემსახურება

-- CREATE VIEW all_departments AS
-- SELECT * FROM departments;

-- შექმენით ვიუ, რომელიც ერთ-ერთი ცხრილიდან წამოიღებს მონაცემებს რაიმეს ფილტრაციით

-- CREATE VIEW filtered_employees AS
-- SELECT * FROM employees
-- WHERE department_id = 1;

-- შექმენით ვიუ, რომელიც ორივე ცხრილიდან წამოიღებს ყველა ველს

-- CREATE VIEW employee_details AS
-- SELECT 
--     e.id AS emp_id, 
--     e.first_name, 
--     e.last_name, 
--     d.id AS dep_id, 
--     d.name AS department_name, 
--     e.updated_at
-- FROM employees e
-- JOIN departments d ON e.department_id = d.id;


-- დააფდეიტეთ ვიუ(შეცვალეთ ფილტრაცია)
-- CREATE OR REPLACE VIEW filtered_employees AS
-- SELECT * FROM employees
-- WHERE department_id = 2;

-- დააფდეიტეთ ვიუ(დაამატეთ სვეტი)

-- CREATE OR REPLACE VIEW all_departments AS
-- SELECT 
--     id, 
--     name, 
--     'Active' AS status
-- FROM departments;

-- შექმენით ტრიგერი და შესაბამისად ფუნქცია, რომელიც ობიექტს დაუსეტავს ცვლილების დროს, ანუ ობიექტის
-- დააფდეიტების მომენტში დაისეტება დრო, რა დროსაც მოხდა ამ ობიექტის ცვლილება

-- CREATE OR REPLACE FUNCTION update_modified_column()
-- RETURNS TRIGGER
-- LANGUAGE plpgsql AS
-- $$
-- BEGIN
--     NEW.updated_at = CURRENT_TIMESTAMP;
--     RETURN NEW;
-- END;
-- $$;

-- CREATE TRIGGER set_timestamp
-- BEFORE UPDATE ON employees
-- FOR EACH ROW
-- EXECUTE FUNCTION update_modified_column();


-- INSERT INTO departments (name) VALUES ('IT Department');

-- INSERT INTO employees (first_name, last_name, department_id)
-- VALUES ('Anri', 'Tsetskhlashvili', 1);

-- SELECT * FROM employees WHERE id = 1;

-- UPDATE employees 
-- SET first_name = 'anri' 
-- WHERE id = 1;

-- SELECT * FROM employees WHERE id = 1;


-- წაშალეთ ვიუები 
-- DROP VIEW IF EXISTS all_departments, filtered_employees, employee_details;
-- DROP TRIGGER IF EXISTS set_timestamp ON employees;
-- DROP FUNCTION IF EXISTS update_modified_column();
-- DROP TABLE IF EXISTS employees, departments;