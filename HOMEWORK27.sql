-- CREATE Table cars(
-- 	car_id SERIAL PRIMARY KEY,
-- 	brand VARCHAR(50) NOT NULL,
-- 	model VARCHAR(50) NOT NULL,
-- 	release_year INT NOT NULL,
-- 	vin VARCHAR(17) NOT NULL UNIQUE CHECK (LENGTH(vin) = 17),
-- 	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
-- 	engine_capacity DECIMAL(3, 1) NOT NULL CHECK (engine_capacity > 0.5),
-- 	mileage_km INT NOT NULL DEFAULT 0 CHECK (mileage_km >= 0),
-- 	is_customs_cleared BOOLEAN NOT NULL DEFAULT FALSE,
--     price DECIMAL(10, 2) NOT NULL CHECK (price >= 0.00),
--     description TEXT,
--     is_sold BOOLEAN NOT NULL DEFAULT FALSE
-- );

-- INSERT INTO cars (
--     brand, model, release_year, vin, engine_capacity, 
--     mileage_km, is_customs_cleared, price, description, is_sold
-- ) VALUES 
-- ('Toyota', 'Camry', 2021, '4T1B11HK5MU123456', 2.5, 45000, TRUE, 18500.00, 'სრული ქარხნული კომპლექტაცია, დაუზიანებელი ძარა.', FALSE),
-- ('BMW', '330i', 2020, 'WBA5R1C58LAH65432', 2.0, 62000, TRUE, 22000.00, 'სპორტული კომპლექტაცია, შავი სალონი, ლუქი.', FALSE),
-- ('Mercedes-Benz', 'E350', 2019, 'W1KZF8EB3KA987654', 2.0, 78000, FALSE, 26500.00, 'საჭიროებს საბაჟო პროცედურების გავლას.', FALSE),
-- ('Honda', 'Civic', 2022, '19XFC2F59NE112233', 1.5, 28000, TRUE, 16800.00, 'ტურბო ძრავი, ადაპტური კრუიზ-კონტროლი.', TRUE),
-- ('Ford', 'Mustang', 2018, '1FA6P8CF8J5445566', 5.0, 95000, TRUE, 24000.00, 'V8 ატმოსფერული ძრავი, მექანიკური გადაცემათა კოლოფი.', FALSE),
-- ('Hyundai', 'Tucson', 2023, 'KM8J33A48PU778899', 2.5, 15000, TRUE, 28500.00, 'სადილერო მომსახურების ისტორიით.', FALSE),
-- ('Audi', 'A6', 2017, 'WAUZZZF27HA998877', 3.0, 120000, FALSE, 19200.00, 'შავი ტყავის სალონი, ლუქი, კლიმატკონტროლი.', FALSE),
-- ('Volkswagen', 'Golf', 2019, 'WVWZZZAUZKP334455', 1.4, 85000, TRUE, 13500.00, 'TSI ძრავი, Start-Stop სისტემა.', TRUE),
-- ('Subaru', 'Forester', 2021, 'JF2SKAFC5MH556677', 2.5, 52000, TRUE, 21000.00, 'ოთხი წამყვანი თვალი.', FALSE),
-- ('Lexus', 'RX 350', 2022, '2T2HZMCA0NC123456', 3.5, 35000, TRUE, 34500.00, 'პრემიუმ აუდიო სისტემა, წრიული ხედვის კამერები.', FALSE);


-- გააგრძელეთ წინა დავალებაში არსებულ ცხრილზე მუშაობა:

-- მონაცემთა გამოტანა:
-- გამოიტანეთ ყველა მონაცემის ყველა სვეტი
-- გამოიტანეთ ყველა ავტომანქანა შემდეგი სვეტებით: ბრენდი, მოდელი, წელი, ფასი
-- გამოიტანეთ ყველა ავტომანქანა კონკრეტული ბრენდის მიხედვით
-- გამოიტანეთ ყველა ავტომანქანა რომლის ფასი არის 2000 და 5000 შორის
-- გამოიტანეთ ყველა ავტომანქანა რომლის გამოშვების წელი არის 2010-ზე ზევით და განბაჟებულია

-- SELECT * FROM cars;
-- SELECT brand, model, release_year, price FROM cars;
-- SELECT * FROM cars WHERE brand = 'BMW';
-- SELECT * FROM cars 	WHERE PRICE BETWEEN 2000.00 AND 5000.00;
-- SELECT * FROM cars WHERE is_customs_cleared AND release_year > 2010;

-- სურვილისამებრ შეგიძლიათ გამოიტანოთ დამატებითი ფილტრებით

-- მონაცემთა შეცვლა:
-- წინა დავალებაში არსებულ მონაცემებში შეცვალეთ:
-- ყველა ჩანაწერის რომელიმე სვეტის მნიშვნელობა
-- ერთი ჩანაწერის რომელიმე სვეტის მნიშვნელობა
-- რამდენიმე ჩანაწერის რომელიმე სვეტის მნიშვნელობა

-- UPDATE cars SET is_sold = false RETURNING *;
-- UPDATE cars SET mileage_km = 50000 WHERE car_id = 1 RETURNING *;
-- UPDATE cars SET is_sold = true WHERE engine_capacity BETWEEN 1.5 AND 2.0 RETURNING *;

-- მონაცემთა წაშლა:
-- წაშალეთ პირველი ორი მონაცემი აიდის მიხედვით(ერთ ქვერიში უნდა იყოს მოქცეული)
-- წაშალეთ ყველა ავტომანქანა რომელიც გაყიდულია
-- წაშალეთ ყველა მონაცემი
-- გაასუფთავეთ ცხრილი

-- DELETE FROM cars WHERE car_id IN (1,2);
-- DELETE FROM cars WHERE is_sold = true RETURNING *;
-- DELETE FROM cars;
-- TRUNCATE TABLE cars;

-- არსებულ ცხრილს:
-- დაამატეთ რომელიმე სვეტი
-- წაშალეთ რომელიმე სვეტი
-- შეცვალეთ სვეტის სახელი
-- შეცვალეთ სვეტის მონაცემთა ტიპი

-- ALTER TABLE cars ADD COLUMN owner_name VARCHAR(50);
-- ALTER TABLE cars DROP COLUMN owner_name;
-- ALTER TABLE cars RENAME COLUMN release_year TO production_year;
-- ALTER TABLE cars ALTER COLUMN production_year TYPE TEXT USING production_year::TEXT;

-- წაშალეთ ცხრილი

-- DROP TABLE IF EXISTS cars;

-- დავალება 27

-- განაგრძეთ წინა დავალებებში არსებულ მონაცემებზე მუშაობა:
-- დათვალეთ ყველა ჩანაწერის რაოდენობა
-- გამოიტანეთ ყველა ავტომობილის ბრენდი(დუბლირებების გარეშე)
-- დათვალეთ ისეთი ჩანაწერების რაოდენობა, რომლებსაც შეტანილი აქვს ვინ კოდი
-- გამოთვალეთ ყველა ავტომობილის საშუალო ფასი
-- გამოთვალეთ ყველა ავტომობილის საშუალო ფასი ავტომობილის ბრენდის მიხედვით
-- გამოთვალეთ ყველა ავტომობილის საშუალო ფასი ავტომობილის ბრენდის და მოდელის მიხედვით
-- გამოიტანეთ ყველა ავტომობილი, რომლის ფასი მეტია ყველა ავტომობილის საშუალო ფასზე
-- გამოიტანეთ მაქსიმალური ღირებულების ავტომობილის ინფორმაცია
-- გამოიტანეთ მაქსიმალური ღირებულების ავტომობილის ინფორმაცია ავტომობილის ბრენდის მიხედვით
-- გამოიტანეთ მინიმალური ღირებულების ავტომობილის ინფორმაცია
-- გამოიტანეთ მინიმალური ღირებულების ავტომობილის ინფორმაცია ავტომობილის ბრენდის მიხედვით

-- SELECT COUNT(*) AS total_cars FROM cars;

-- SELECT DISTINCT brand FROM cars;

-- SELECT COUNT(vin) AS cars_with_vin FROM cars;

-- SELECT ROUND(AVG(price), 2) AS average_price FROM cars;

-- SELECT brand, ROUND(AVG(price), 2) AS avg_price_by_brand FROM cars GROUP BY brand;

-- SELECT brand, model, ROUND(AVG(price), 2) AS avg_price_by_brand_model FROM cars GROUP BY brand, model;

-- SELECT * FROM cars WHERE price > (SELECT AVG(price) FROM cars);

-- SELECT * FROM cars WHERE price = (SELECT MAX(price) FROM cars);

-- SELECT c.* FROM cars c WHERE c.price = (
--     SELECT MAX(sub.price) 
--     FROM cars sub 
--     WHERE sub.brand = c.brand
-- );

-- SELECT * FROM cars WHERE price = (SELECT MIN(price) FROM cars);

-- SELECT c.* FROM cars c WHERE c.price = (
--     SELECT MIN(sub.price) 
--     FROM cars sub 
--     WHERE sub.brand = c.brand
-- );

-- დაამატეთ ახალი სვეტი, რომელშიც შეინახავთ ავტომობილის რაოდენობას(quantity), default იყოს 1 და შეამოწმეთ რომ შეყვანილი
-- მნიშვნელობა იყოს 0-ზე მეტი

-- ALTER TABLE cars ADD COLUMN quantity INT NOT NULL DEFAULT 1 CHECK (quantity > 0);

-- რამდენიმე ავტომობილზე შეცვალეთ რაოდენობა
-- დათვალეთ ყველა ავტომობილის რაოდენობა
-- დათვალეთ ყველა ავტომობილის რაოდენობა ბრენდის მიხედვით
-- გამოიტანეთ ყველა ავტომობილის ბრენდი, მოდელი და მთლიანი ფასი(ფასი * რაოდენობაზე)
-- გამოთვალეთ ყველა ავტომობილის საერთო ფასის ჯამი(გაითვალისწინეთ ავტომობილის რაოდენობაც)

-- UPDATE cars SET quantity = 3 WHERE brand IN ('Toyota', 'Honda');

-- SELECT SUM(quantity) AS total_inventory_count FROM cars;

-- SELECT brand, SUM(quantity) AS total_quantity_by_brand FROM cars GROUP BY brand;

-- SELECT brand, model, price, quantity, (price * quantity) AS total_value FROM cars;

-- SELECT SUM(price * quantity) AS grand_total_inventory_value FROM cars;




