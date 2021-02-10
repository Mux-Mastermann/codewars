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


-- SQL Bug Fixing: Fix the QUERY - Totaling
SELECT 
  CAST(s.transaction_date AS date) as day,
  d.name AS department,
  COUNT(s.id) AS sale_count
FROM department d
JOIN sale s on d.id = s.department_id
GROUP BY CAST(s.transaction_date AS date), d.name
ORDER BY day ASC;


-- SQL Basics: Simple table totaling
SELECT
  RANK() OVER(
    ORDER BY SUM(points) DESC
  ),
  CASE
    WHEN clan = '' THEN '[no clan specified]'
    ELSE clan
  END AS clan,
  SUM(points) AS total_points,
  COUNT(name) AS total_people
FROM people
GROUP BY clan
ORDER BY SUM(points) DESC;


-- Relational division: Find all movies two actors cast in together
SELECT f.title
FROM film f
WHERE f.film_id IN (
  SELECT film_id FROM film_actor WHERE actor_id = 105 AND film_id IN (
    SELECT film_id FROM film_actor WHERE actor_id = 122
  )
)
ORDER BY f.title;


-- SQL Basics: Simple PIVOTING data WITHOUT CROSSTAB
SELECT
  p.name, 
  COUNT(CASE WHEN d.detail = 'good' THEN d.id END) AS good,
  COUNT(CASE WHEN d.detail = 'ok' THEN d.id END) AS ok,
  COUNT(CASE WHEN d.detail = 'bad' THEN d.id END) AS bad
FROM products p
LEFT JOIN details d ON p.id = d.product_id 
GROUP BY p.name
ORDER BY p.name;


-- Calculating Batting Average
SELECT
  player_name,
  games,
  CAST(ROUND(CAST(CAST(hits AS float) / CAST(at_bats AS float) AS numeric), 3) AS text) AS batting_average
FROM yankees
WHERE NOT at_bats < 100
ORDER BY batting_average DESC;


-- Present JSON data the SQL way
SELECT
  data ->> 'first_name' AS first_name,
  data ->> 'last_name' AS last_name,
  date_part('year', age(NOW()::timestamp, (data ->> 'date_of_birth')::date))::int AS age,
  CASE 
    WHEN data ->> 'private' = 'true' THEN 'Hidden'
    WHEN data ->> 'email_addresses' = '[]' THEN 'None'
    ELSE data#>>'{email_addresses, 0}'
  END AS email_address 
FROM users
ORDER BY first_name, last_name;


-- SQL Basics: Simple GROUP BY
SELECT age, COUNT(id) AS people_count
FROM people
GROUP BY age;


-- SQL: Regex Replace
SELECT
  project,
  commits,
  contributors,
  REGEXP_REPLACE(address, '[0-9]' , '!', 'g') AS address
FROM repositories