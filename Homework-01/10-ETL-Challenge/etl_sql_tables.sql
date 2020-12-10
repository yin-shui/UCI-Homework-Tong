-- CREATE blockbuster TABLE
---------------------------
CREATE TABLE blockbuster (
    title TEXT PRIMARY KEY, 
    genre TEXT,
    rating TEXT,
    release_year INT,
    studio TEXT,
    worldwide_gross FLOAT
);
SELECT *
FROM blockbuster
LIMIT 10;
-- CREATE imdb TABLE
--------------------
CREATE TABLE imdb (
    "title" TEXT PRIMARY KEY,
    "director" TEXT,
    "actors" TEXT,
    "rating" FLOAT,
    "votes" INT,
    "revenue_millions" FLOAT,
    "metascore" FLOAT
);
SELECT title, revenue_millions
FROM imdb
LIMIT 10;
-- CREATE tmdb TABLE
--------------------
CREATE TABLE tmdb (
    "title" TEXT PRIMARY KEY,
    "budget" INT,
    "runtime" FLOAT
);
SELECT *
FROM tmdb
LIMIT 10;

-- Combine tables for an overall view
--------------------
SELECT b.title, b.genre, i.director, t.budget,
    b.release_year, b.worldwide_gross, (b.worldwide_gross / t.budget) AS "Return"
FROM blockbuster b
INNER JOIN imdb i 
ON b.title = i.title
INNER JOIN tmdb t
ON i.title = t.title
ORDER BY b.worldwide_gross DESC
LIMIT 10;

-- Drop table commands
--------------------
drop table imdb;
drop table tmdb;
drop table blockbuster;