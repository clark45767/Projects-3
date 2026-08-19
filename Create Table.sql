-- Create the employee table
CREATE TABLE employees (
    employee_id INT,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

-- Insert employee data
INSERT INTO employees VALUES
(1, 'John', 'Finance', 50000),
(2, 'Sarah', 'HR', 45000),
(3, 'Mike', 'IT', 60000),
(4, 'David', 'Finance', 55000),
(5, 'Anna', 'IT', 65000);

-- Display all employees
SELECT * FROM employees;

-- Get details of employees from the Finance department
SELECT *
FROM employees
WHERE department = 'Finance';