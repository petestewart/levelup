python manage.py loaddata users
python manage.py loaddata tokens
python manage.py loaddata gamers;

SELECT
    e.organizer_id,
    u.first_name || ' ' || u.last_name AS full_name,
    e.id,
    e.date,
    e.time,
    g.title
FROM
    levelupapi_event e
JOIN
    levelupapi_game g ON e.game_id = g.id
JOIN
    auth_user u ON e.organizer_id = u.id