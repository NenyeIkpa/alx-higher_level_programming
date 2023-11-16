-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT ts.title, tsg.genre_id
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
WHERE tsg.genre_id IS NULL
ORDER BY ts.title ASC, tsg.genre_id;
