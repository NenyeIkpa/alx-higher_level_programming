-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
-- Records are ordered by ascending genre name.
SELECT tg.name
FROM tv_genres AS tg
INNER JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id

INNER JOIN tv_shows AS ts
ON ts.id = tsg.show_id
WHERE ts.title = "Dexter"
ORDER BY tg.name;
