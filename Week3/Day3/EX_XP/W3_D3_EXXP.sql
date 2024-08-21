-- 🌟 Exercise 1: DVD Rental
-- Instructions
-- Get a list of all the languages, from the language table.
SELECT * FROM language;

-- Get a list of all films joined with their languages – select the following details : film title, description, and language name.
SELECT film.title, film.description, language.name AS language_name FROM film JOIN language ON film.language_id = language.language_id;
-- Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.
SELECT film.title, film.description, language.name AS language_name FROM language LEFT JOIN film ON language.language_id = film.language_id;
-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.
CREATE TABLE new_film (id SERIAL PRIMARY KEY,name VARCHAR(50) NOT NULL);
INSERT INTO new_film (name) VALUES ('Despicable Me 4'), ('Dune 2'), ('Deadpool and Wolverine');
-- Create a new table called customer_review, which will contain film reviews that customers will make.CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR(50) NOT NULL,
    score INT,
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.

-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO customer_review (film_id, language_id, title, score, review_text) VALUES
(1, 1, 'Must thing to see!', 9, 'I really enjoyed this movie with my family, feels like a high-speed ride.'),
(2, 1, 'Good one', 7, 'The movie was nice, but in a book everything was better!.');
-- Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film WHERE id = 1;
-- due to delete cascade all reviews will be automatically deleted from this movie

-- 🌟 Exercise 2 : DVD Rental
-- Instructions
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film SET language_id = 2 WHERE film_id = 3;
-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?

-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
DROP TABLE customer_review;
÷-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT COUNT(*) FROM rental WHERE return_date IS NULL
-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT film.title, rental.rental_date, inventory.inventory_id, film.replacement_cost
FROM rental
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id
WHERE rental.return_date IS NULL
ORDER BY film.replacement_cost DESC
LIMIT 30;
-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT film.title 
FROM film 
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.first_name = 'Penelope' AND actor.last_name = 'Monroe'
AND film.description LIKE '%sumo%';
-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT title
FROM film
WHERE rating = 'R' AND length < 60 AND description LIKE '%documentary%';
-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
SELECT film.title
FROM rental
JOIN payment ON rental.rental_id = payment.rental_id
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id
JOIN customer ON rental.customer_id = customer.customer_id
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
AND payment.amount > 4.00
AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01';
-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
SELECT title
FROM film
WHERE (title LIKE '%boat%' OR description LIKE '%boat%') 
AND replacement_cost > 20.00;