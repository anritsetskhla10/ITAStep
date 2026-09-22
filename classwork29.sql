-- შექმენით პროდუქტების ცხრილი შესაბამისი ველებით (აიდი, დასახელება, ფასი, რაოდენობა, სტატუსი)
-- ჯერ არ შეავსოთ ცხრილი

-- 1. შექმენით პროცედურა, რომელსაც გადაეცემა ორი არგუმენტი: პროდუქტის აიდი და რაოდენობა
-- აღნიშნული პროცედურის გამოძახების შემდეგ გადაცემული პროდუქტის აიდის და რაოდენობის მიხედვით 
-- კონკრეტული პროდუქტის რაოდენობას(ცხრილში) უნდა მოაკლდეს გადაცემული რაოდენობა.



-- CREATE TABLE products(
-- 	product_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(50),
-- 	price INT,
-- 	quantity INT,
-- 	status VARCHAR(30)
-- )

-- SELECT * FROM products

-- CREATE PROCEDURE change_stock(id INT, sold_quantity INT)
-- LANGUAGE plpgsql AS
-- $$
-- BEGIN
-- 	UPDATE products SET quantity = quantity - sold_quantity WHERE product_id = id ; 
-- END
-- $$
 
-- CALL change_stock(1,2);

-- 2. შექმენით ტრიგერი, რომელიც პროდუქტების შევსების ან განახლების დროს გააკეთებს შემდეგ რამეს:
-- თუ პროდუქტის რაოდენობა იქნება 0, სტატუსს დაუსეტავს out of stock, 
-- თუ იქნება 1-10 შუალედში დაუსეტავს low stock
-- 10-ზე მეტის შემთხვევაში დაუსეტავს in stock.



-- CREATE OR REPLACE FUNCTION check_stock()
-- RETURNS TRIGGER
-- LANGUAGE plpgsql AS
-- $$
-- BEGIN
-- 	IF NEW.quantity <= 0 THEN
-- 		NEW.status := 'out of stock';
-- 	ELSIF NEW.quantity BETWEEN 1 AND 10 THEN
-- 		NEW.status := 'low stock';
-- 	ELSE
-- 		NEW.status := 'in stock';
-- 	END IF;
-- 	RETURN NEW;
-- END;
-- $$
 
-- CREATE TRIGGER set_status
-- BEFORE INSERT OR UPDATE
-- ON products
-- FOR EACH ROW
-- EXECUTE FUNCTION check_stock();

-- ახლა შეავსეთ ცხრილი(სტატუსი ხელით არ შეიყვანოთ)!

-- გამოიძახეთ შექმნილი პროცედურა
 
INSERT INTO products(name, price, quantity) VALUES
	('Laptop', 500 , 4),
	('PC', 1500, 0),
	('PS6', 2500, 11),
	('TV', 1200, 1);
 







