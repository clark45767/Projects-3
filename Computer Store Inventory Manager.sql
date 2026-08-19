CREATE TABLE PRODUCT (
    product_id INT,
    product_name VARCHAR(50),
    price INT,
    company_name VARCHAR(50)
);

INSERT INTO PRODUCT VALUES
(1, 'Laptop', 2500, 'Dell'),
(2, 'Speaker', 300, 'Sony'),
(3, 'ZIP DRIVE', 150, 'SanDisk'),
(4, 'Keyboard', 200, 'Logitech');

-- Show products
SELECT * FROM PRODUCT;

-- Condition
SELECT * FROM PRODUCT WHERE price > 200;

-- Search by name
SELECT * FROM PRODUCT WHERE product_name LIKE '%Speaker%';

-- Minimum and maximum price
SELECT MIN(price), MAX(price) FROM PRODUCT;

-- Update Speaker price
UPDATE PRODUCT SET price = 350
WHERE product_name = 'Speaker';

-- Delete ZIP DRIVE
DELETE FROM PRODUCT
WHERE product_name = 'ZIP DRIVE';