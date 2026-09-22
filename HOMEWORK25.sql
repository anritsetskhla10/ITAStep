CREATE Table cars(
	car_id SERIAL PRIMARY KEY,
	brand VARCHAR(50) NOT NULL,
	model VARCHAR(50) NOT NULL,
	release_year INT NOT NULL,
	vin VARCHAR(17) NOT NULL UNIQUE CHECK (LENGTH(vin) = 17),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	engine_capacity DECIMAL(3, 1) NOT NULL CHECK (engine_capacity > 0.5),
	mileage_km INT NOT NULL DEFAULT 0 CHECK (mileage_km >= 0),
	is_customs_cleared BOOLEAN NOT NULL DEFAULT FALSE,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0.00),
    description TEXT,
    is_sold BOOLEAN NOT NULL DEFAULT FALSE
);

INSERT INTO cars (
    brand, model, release_year, vin, engine_capacity, 
    mileage_km, is_customs_cleared, price, description, is_sold
) VALUES 
('Toyota', 'Camry', 2021, '4T1B11HK5MU123456', 2.5, 45000, TRUE, 18500.00, 'სრული ქარხნული კომპლექტაცია, დაუზიანებელი ძარა.', FALSE),
('BMW', '330i', 2020, 'WBA5R1C58LAH65432', 2.0, 62000, TRUE, 22000.00, 'სპორტული კომპლექტაცია, შავი სალონი, ლუქი.', FALSE),
('Mercedes-Benz', 'E350', 2019, 'W1KZF8EB3KA987654', 2.0, 78000, FALSE, 26500.00, 'საჭიროებს საბაჟო პროცედურების გავლას.', FALSE),
('Honda', 'Civic', 2022, '19XFC2F59NE112233', 1.5, 28000, TRUE, 16800.00, 'ტურბო ძრავი, ადაპტური კრუიზ-კონტროლი.', TRUE),
('Ford', 'Mustang', 2018, '1FA6P8CF8J5445566', 5.0, 95000, TRUE, 24000.00, 'V8 ატმოსფერული ძრავი, მექანიკური გადაცემათა კოლოფი.', FALSE),
('Hyundai', 'Tucson', 2023, 'KM8J33A48PU778899', 2.5, 15000, TRUE, 28500.00, 'სადილერო მომსახურების ისტორიით.', FALSE),
('Audi', 'A6', 2017, 'WAUZZZF27HA998877', 3.0, 120000, FALSE, 19200.00, 'შავი ტყავის სალონი, ლუქი, კლიმატკონტროლი.', FALSE),
('Volkswagen', 'Golf', 2019, 'WVWZZZAUZKP334455', 1.4, 85000, TRUE, 13500.00, 'TSI ძრავი, Start-Stop სისტემა.', TRUE),
('Subaru', 'Forester', 2021, 'JF2SKAFC5MH556677', 2.5, 52000, TRUE, 21000.00, 'ოთხი წამყვანი თვალი.', FALSE),
('Lexus', 'RX 350', 2022, '2T2HZMCA0NC123456', 3.5, 35000, TRUE, 34500.00, 'პრემიუმ აუდიო სისტემა, წრიული ხედვის კამერები.', FALSE);


