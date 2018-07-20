-- INSERT INTO person VALUES(1,'Anna','Perry',6,'12/12/12','21','None');


-- CREATE TABLE courses(
--    course_id SERIAL PRIMARY KEY,
--    code VARCHAR(255) NOT NULL,
--    title VARCHAR(255) NOT NULL,
--    institution_id INTEGER NOT NULL,
--    FOREIGN KEY(institution_id)
--    REFERENCES institution(institution_id)
-- );


-- CREATE TABLE institution(
--    institution_id SERIAL PRIMARY KEY,
--    name VARCHAR(255) NOT NULL,
--    members INTEGER NOT NULL,
--    date_created DATE NOT NULL
-- );


DROP TABLE  users CASCADE;
DROP TABLE thought;