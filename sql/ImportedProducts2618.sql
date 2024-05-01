--Our company's import sector needs a report on the import of products from our Sansul providers.

--Your task is to display the name of the products, the name of the supplier and the name 
--of the category, for the products supplied by the supplier 'Sansul SA' and whose category
-- name is 'Imported'.


SELECT prod.name, prov.name, cat.name 
FROM products prod 
INNER JOIN providers prov ON prod.id_providers  = prov.id
INNER JOIN categories cat ON prod.id_categories = cat.id
WHERE prov.name = 'Sansul SA' AND cat.name = 'Imported'
