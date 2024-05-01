--The company's financial audit is asking us for a report for the first half of 2016. 
--Then display the customers name and order number for customers who placed orders
-- in the first half of 2016.

SELECT cust.name, ords.id FROM customers cust 
INNER JOIN orders ords ON cust.id = ords.id_customers
WHERE ords.orders_date  BETWEEN '2016-01-01' AND '2016-06-30'
