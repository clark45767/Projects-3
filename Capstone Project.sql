CREATE TABLE Employees (
    id INT,
    name VARCHAR(50),
    salary INT
);

SELECT * FROM Employees;

SELECT * FROM Employees
WHERE salary > 50000;

SELECT * FROM Employees
ORDER BY salary DESC;