--Every month the company asks for a report from the cities that providers are registered.
-- So, do a query that returns all the cities of the providers, but in alphabetical order.

--OBS: You must not show repeated cities.

SELECT city FROM providers
 ORDER BY city ASC 
 