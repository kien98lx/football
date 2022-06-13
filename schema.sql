CREATE TABLE if not exists leagues (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
)


CREATE TABLE if not exists clubs (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    leagues_id INT NOT NULL,
    image TEXT,
    stadium TEXT NOT NULL

)

CREATE TABLE if not exists matches (
    id SERIAL PRIMARY KEY,
    home_id INT NOT NULL,
    away_id INT NOT NULL,
    home_goal INT NOT NULL,
    away_goal INT NOT NULL,
    start_time DATE,
    place TEXT NOT NULL
)