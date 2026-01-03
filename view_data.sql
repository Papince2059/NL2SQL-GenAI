-- View all movies data
SELECT * FROM movies;

-- View top 10 movies by IMDb rating
SELECT Title, IMDb_Rating, Box_Office_Millions FROM movies ORDER BY IMDb_Rating DESC LIMIT 10;

-- Count total movies
SELECT COUNT(*) as Total_Movies FROM movies;
