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
      