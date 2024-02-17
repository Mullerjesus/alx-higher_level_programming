-- a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_genres.name 
FROM tv_genres 
WHERE id NOT IN 
(SELECT genre_id FROM tv_shows JOIN tv_genres WHERE title = 'Dexter') 
ORDER BY tv_genres.name ASC;
