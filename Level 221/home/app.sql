
SELECT 
    title,
    film_actor.film_id,
    film_actor.actor_id,
    category.category_id,
    inventory.inventory_id,
    inventory.store_id,
    customer.customer_id,
    staff.staff_id,
    rental.rental_id,
    rental.customer_id,
    customer.address_id,
    CONCAT(actor.first_name, ' ', actor.last_name) AS actor_fullName,
    CONCAT(staff.first_name, ' ', staff.last_name) AS staff_fullName,
    CONCAT(customer.first_name, ' ', customer.last_name) AS curtomer_fullname,
    staff.email,
    staff.password,
    address.address,
    address.city_id,
    address.postal_code,
    address.phone,
    city.city,
    country.country,
    store.store_id,
    payment.customer_id,
    payment.payment_id,
    payment.amount
FROM film_actor

JOIN film
    ON film.film_id = film_actor.film_id

JOIN actor
    ON actor.actor_id = film_actor.actor_id

JOIN film_category
    ON film_category.film_id = film_actor.actor_id

JOIN category
    ON film_category.category_id = category.category_id

JOIN inventory
    ON inventory.inventory_id = film_actor.actor_id

JOIN rental
    ON rental.inventory_id = inventory.inventory_id

JOIN staff
    ON rental.staff_id = staff.staff_id

JOIN customer
    ON rental.customer_id = customer.customer_id
    
JOIN address
    ON address.address_id = customer.address_id

JOIN city
    ON address.city_id = city.city_id

JOIN country
    ON city.country_id = country.country_id

JOIN store
    ON store.store_id = inventory.store_id

JOIN payment
    ON customer.customer_id = payment.customer_id
