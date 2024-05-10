--The financial sector of the company needs a report that shows the ID and
-- the name of the products whose price is less than 10 or greater than 100.

SELECT id, name
FROM products
WHERE price < 10 OR price > 100