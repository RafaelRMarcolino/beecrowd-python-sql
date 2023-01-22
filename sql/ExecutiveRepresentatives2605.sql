--The financial sector needs a report on the providers of the products we sell.
-- The reports include all categories, but for some reason, providers of products
-- whose category is the executive, are not in the report.

--Your job is to return the names of the products and providers whose category ID is 6.

SELECT p.name, f.name
FROM products P INNER JOIN providers f 
ON p.id_providers = f.id 
WHERE p.id_categories = 6
