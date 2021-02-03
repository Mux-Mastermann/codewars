-- Kata: SQL Basics: Simple JOIN and RANK
SELECT 
  p.id, p.name, COUNT(s.sale) AS "sale_count", RANK() OVER (ORDER BY COUNT(s.sale) DESC) AS "sale_rank"
FROM 
  people AS p 
JOIN 
  sales AS s ON p.id = s.people_id
GROUP BY
  p.id, p.name;


-- Kata: SQL Basics: Simple IN
SELECT
  id, name
FROM
  departments AS d
WHERE
  d.id IN (
    SELECT
      department_id
    FROM
      sales AS s
    WHERE
      s.price > 98
  );


-- Kata: SQL Basics: Up and Down
SELECT 
  CASE
    WHEN SUM(number1) % 2 = 0 THEN MAX(number1)
    ELSE MIN(number1)
  END AS number1,
  CASE
    WHEN SUM(number2) % 2 = 0 THEN MAX(number2)
    ELSE MIN(number2)
  END AS number2
FROM
  numbers;


-- SQL Basics: Create a FUNCTION (DATES)
-- NOT SOLVED YET
CREATE FUNCTION agecalculator(birthday date)
RETURNS int AS
DECLARE Age int;
BEGIN
  SET Age = DATEDIFF(yy, birthday, NOW()) 
  RETURN Age
END;


-- SQL Basics: Simple EXISTS
SELECT
  id,
  name
FROM
  departments d
WHERE EXISTS
  (SELECT department_id FROM sales s WHERE d.id=s.department_id AND price > 98)
;


-- SQL Basics: Simple WITH
WITH special_sales AS (
  SELECT * FROM sales WHERE price > 90
)

SELECT * FROM departments WHERE id IN (SELECT department_id FROM special_sales);


-- SQL Basics: Simple VIEW
CREATE VIEW members_approved_for_voucher AS
-- Total sales by members
SELECT s.member_id, SUM(p.price) AS total_spending
FROM sales s
LEFT JOIN products p ON s.product_id = p.id
WHERE s.department_id IN(
  -- Total sales by department  
  SELECT s.department_id 
  FROM sales s 
  LEFT JOIN products p ON s.product_id = p.id 
  GROUP BY s.department_id 
  HAVING SUM(p.price) > 10000)
GROUP BY s.member_id
HAVING SUM(p.price) > 1000;

SELECT member_id AS id, m.name, m.email, total_spending 
FROM members_approved_for_voucher
JOIN members m ON members_approved_for_voucher.member_id = m.id
ORDER BY id; 


-- SQL Statistics: MIN, MEDIAN, MAX
-- NOT SOLVED YET
SELECT 
  MIN(score),
  CASE
    WHEN COUNT(id) % 2 = 1 THEN (SELECT score FROM result ORDER BY score LIMIT (COUNT(id) + 1) / 2 OFFSET (COUNT(id) - 1) / 2)
    ELSE (SELECT AVG(score) FROM result ORDER BY score LIMIT (COUNT(id) / 2) + 1 OFFSET (COUNT(id) / 2) - 1)
  END AS median, 
  MAX(score)
FROM result;