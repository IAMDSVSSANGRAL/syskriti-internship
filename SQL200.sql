-- Q1 — Film prices
-- Get films where rental_rate is 9.99 or 4.99

SELECT film_id, title, rental_rate
FROM film
WHERE rental_rate IN (9.99, 4.99);



-- Q2 — Film length + rating
-- Films 90–120 minutes (inclusive) and rating PG or PG-13

SELECT title, length, rating
FROM film
WHERE length BETWEEN 90 AND 120
AND rating IN ('PG', 'PG-13');



-- Q3 — Actor last names
-- Last name starts with S OR ends with N

SELECT actor_id, first_name, last_name
FROM actor
WHERE last_name LIKE 'S%'
OR last_name LIKE '%N';



-- Q4 — Active customers + email filter
-- Active customers whose email contains ".org" OR ".net"

SELECT customer_id, first_name, last_name, email
FROM customer
WHERE active = 1
AND (
    email LIKE '%.org%'
    OR email LIKE '%.net%'
);



-- Q5 — Inactive customers in store 1
-- Customers from store 1 who are not active

SELECT customer_id, store_id, active
FROM customer
WHERE store_id = 1
AND active = 0;



-- Q6 — Payment amount + date range
-- Amount between 2.00 and 5.00 and made in February 2007

SELECT payment_id, customer_id, amount, payment_date
FROM payment
WHERE amount BETWEEN 2.00 AND 5.00
AND payment_date >= '2007-02-01'
AND payment_date < '2007-03-01';



-- Q7 — Rentals not returned
-- return_date is NULL

SELECT rental_id, rental_date, return_date, customer_id
FROM rental
WHERE return_date IS NULL;



-- Q8 — Address district + postal code present
-- District Texas or California AND postal_code not NULL

SELECT address_id, address, district, postal_code
FROM address
WHERE district IN ('Texas', 'California')
AND postal_code IS NOT NULL;



-- Q9 — Replacement cost + exclude titles
-- replacement_cost 12.99, 16.99, 28.99
-- title does NOT contain letter A

SELECT film_id, title, replacement_cost
FROM film
WHERE replacement_cost IN (12.99, 16.99, 28.99)
AND title NOT LIKE '%A%';



-- Q10 — Inventory logic challenge
-- (store 1 AND film_id 1–50)
-- OR
-- (store 2 AND film_id 51–100)

SELECT inventory_id, film_id, store_id
FROM inventory
WHERE 
    (store_id = 1 AND film_id BETWEEN 1 AND 50)
    OR
    (store_id = 2 AND film_id BETWEEN 51 AND 100);
