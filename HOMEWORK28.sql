-- შექმენით ახალი ბაზა და დაიწყეთ მუშაობა
-- უნდა შექმნათ ცხრილები, გაითვალისწინეთ, ყველა ცხრილს უნდა ჰქონდეს აიდები და სათითაოდ აღარ ჩამოვწერ ყველა ცხრილისთვის

-- შექმენით ცხრილი customers რომელსაც ექნება შემდეგი ველები:
-- სახელი, არ უნდა იყოს განუსაზღვრელი
-- ემაილი, არ უნდა იყოს განუსაზღვრელი და უნდა იყოს უნიკალური

CREATE TABLE customers(
	customer_id SERIAL PRIMARY KEY,
	customer_name VARCHAR(30) NOT NULL,
	email VARCHAR(60) NOT NULL UNIQUE
);

-- შექმენით ცხრილი customer_profiles, რომელსაც ექნება one-to-one კავშირი customers ცხრილთან
-- დამატებით ექნება ველი ტელეფონის ნომერი და მისამართი

CREATE TABLE customer_profiles(
	profile_id SERIAL PRIMARY KEY,
	customer_id INT NOT NULL UNIQUE, 
	phone_number VARCHAR(20), 
	address TEXT,
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- შექმენით ცხრილი suppliers(მომწოდებელი) შემდეგი ველებით:
-- სახელი, არ უნდა იყოს განუსაზღვრელი
-- საკონტაქტო ემაილი, არ უნდა იყოს განუსაზღვრელი და უნდა იყოს უნიკალური

CREATE TABLE suppliers(
	supplier_id SERIAL PRIMARY KEY,
	supplier_name VARCHAR(50) NOT NULL,
	contact_email VARCHAR(60) NOT NULL UNIQUE
);

-- შექმენით ცხრილი products, ველებით:
-- დასახელება, არ უნდა იყოს განუსაზღვრელი
-- ფასი, არ უნდა იყოს განუსაზღვრელი
-- მომწოდებელი(დაკავშირებული უნდა იყოს suppliers ცხრილთან, ერთი მომწოდებელი - მრავალი პროდუქტი)

CREATE TABLE products(
	product_id SERIAL PRIMARY KEY,
	product_name VARCHAR(100) NOT NULL,
	price DECIMAL(10, 2) NOT NULL,
	supplier_id INT,
	FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE SET NULL
);

-- many-to-many კავშირისთვის გამოიყენეთ ქვემოთ მოცემული სქემა
-- შეკვეთები უნდა დაუკავშიროთ პროდუქტებს, ანუ თითო შეკვეთა შეიძლება მოიცავდეს ბევრ პროდუქტს და ასევე ერთი პროდუქტი შეიძლება 
-- იყოს ბევრ შეკვეთაში, ანუ უნდა შექმნათ orders ცხრილი და ე.წ. შუამავალი ცხრილი, შუამავალ ცხრილს დაუმატეთ პროდუქტის რაოდენობა

-- orders ცხრილს უნდა ჰქონდეს შეკვეთის თარიღი და ასევე უნდა იყოს მიბმული მომხმარებელთან(ერთი მომხმარებელი - მრავალი შეკვეთა)

CREATE TABLE orders(
	order_id SERIAL PRIMARY KEY,
	order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	customer_id INT NOT NULL,
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE order_items(
	order_id INT NOT NULL,
	product_id INT NOT NULL,
	quantity INT NOT NULL CHECK (quantity > 0),
	PRIMARY KEY (order_id, product_id),
	FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
	FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);


