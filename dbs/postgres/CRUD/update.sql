
UPDATE student
SET marks = 0
WHERE marks IS NULL;


UPDATE student
SET email = 'johndoe@gmail.com'
WHERE TRIM(LOWER(email)) = 'johon@gmail.com';
