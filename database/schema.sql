CREATE TABLE users(
   user_id SERIAL PRIMARY KEY,
   first_name VARCHAR(255) NOT NULL,
   last_name VARCHAR(255) NOT NULL,
   number_of_thoughts INTEGER NOT NULL,
   date_joined DATE NOT NULL,
   status VARCHAR(255),
   password VARCHAR(255) NOT NULL
   );

CREATE TABLE thought(
   text VARCHAR(255) NOT NULL,
   date_published DATE NOT NULL,
   type VARCHAR(255) NOT NULL,
   votes INTEGER NOT NULL,
   user_id INTEGER NOT NULL,
   FOREIGN KEY(user_id)
   REFERENCES users(user_id)
);
