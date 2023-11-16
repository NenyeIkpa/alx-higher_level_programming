-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT
ts.title AS tv_shows,
tsg.genre_id AS tv_show_genres
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg ON ts.id = tsg.show_id
ORDER BY ts.title ASC, tsg.genre_id;
