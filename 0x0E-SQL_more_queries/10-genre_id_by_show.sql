-- This script lists all shows in the hbtn_0d_tvshows database that have at least one linked genre.
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.


SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.genre_id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
