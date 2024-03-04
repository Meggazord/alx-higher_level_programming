-- Retrieve all Comedy shows from the hbtn_0d_tvshows database
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.id = (SELECT tv_genres.id FROM tv_genres WHERE name = 'Comedy')
ORDER BY tv_shows.title ASC;
