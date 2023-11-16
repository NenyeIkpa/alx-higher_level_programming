-- Lists all shows and genres linked to the show from the
-- database hbtn_0d_tvshows.
-- Records are ordered by ascending show title and genre name.
SELECT ts.title, tg.name
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id

LEFT JOIN tv_genres AS tg
ON tsg.genre_id = tg.id
ORDER BY ts.title, tg.name;
