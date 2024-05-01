--In the past the studio has made an event where several movies were on sale, 
--we want to know what movies these were.

--Your job to help us is to select the ID and name of movies whose price is less than 2.00.

SELECT m.id, m.name FROM movies m 
INNER JOIN  prices p ON m.id_prices = p.id 
WHERE p.value  < 2;

