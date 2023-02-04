--The financial sector has encountered some problems in the delivery of one 
--of our providers, the delivery of the products does not match the invoice.

--Your job is to display the name of the products and the name of the provider,
-- for the products supplied by the provider 'Ajax SA'.


SELECT prod.name, prov.name FROM providers prov  
INNER JOIN products prod 
ON prov.id = prod.id_providers 
WHERE prov.name = 'Ajax SA'
