-- lists all shows contained in hbtn_0d_tvshows
-- Displays NULL for shows without genre
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT ts.title, tsg.genre_id
FROM tv_shows AS ts
LEFT JOIN tv_show_genres as tsg
ON ts.id = tsg.show_id
ORDER BY ts.title, tsg.genre_id;
