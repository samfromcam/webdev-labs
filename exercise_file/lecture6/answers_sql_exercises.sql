-- 1. Display the first_name, last_name, and email 
--    for all the users in the "users" table
--    sort by last_name descending

SELECT first_name, last_name, email
FROM users
ORDER BY last_name desc;


-- 2. Count all of the users in the users table
SELECT count(*)
FROM users;


-- 3. Display the first_name, last_name, and email 
--    for all the users whose first name is Kristy
SELECT first_name, last_name, email
FROM users
WHERE first_name = 'Kristy';

-- 4. Display the id, first_name, last_name, and email 
--    for users whose ids are either 2, 5, 7, 9, 11, or 33.
SELECT id, first_name, last_name, email
FROM users
WHERE id in (2, 5, 7, 9, 11, 33);


-- 5. Display the first_name, last_name, and email 
--    for all the users whose use gmail for email.
SELECT first_name, last_name, email
FROM users
WHERE email like '%gmail%';


-- 6. Write a query that joins the posts and users table. The results
-- should display the id and pub_date from the posts table, and 
-- the author's username, first_name, and last_name from the users table
SELECT posts.id, posts.pub_date,
	users.username, users.first_name, users.last_name  
FROM posts
INNER JOIN users
    ON users.id = posts.user_id;


-- 7. Display all of the usernames that user id=5 is following.
--    You'll need to join the users table to the following table.
SELECT following.user_id, following.following_id, users.username
FROM following
INNER JOIN users
    ON users.id = following.following_id
WHERE following.user_id=5;




