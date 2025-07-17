import sqlite3

conn = sqlite3.connect("tracksdb.sqlite")
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
                  
CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    artist_id INTEGER
);
                  
CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER, 
    rating INTEGER, count INTEGER, len INTEGER
);
''')

with open("tracks.csv" , "r") as file:
    next(file)
    for line in file:
        line = line.rstrip()
        words = line.split(",")
        if len(words) != 7:
            continue
        track = words[0]
        artist = words[1]
        album = words[2]
        count = words[3]
        rating = words[4]
        lenght = words[5]
        genre = words[6]

        cur.execute("INSERT OR IGNORE INTO Artist(name) VALUES(?)" , (artist,))
        cur.execute("SELECT id FROM Artist WHERE name = (?)", (artist,))
        artist_id = cur.fetchone()[0]

        cur.execute("INSERT OR IGNORE INTO Genre(name) VALUES(?)", (genre,))
        cur.execute("SELECT id FROM Genre WHERE name = (?)", (genre,))
        genre_id = cur.fetchone()[0]

        cur.execute("INSERT OR REPLACE INTO Album(title , artist_id) VALUES(? , ?)", (album,artist_id))
        cur.execute("SELECT id FROM Album WHERE title = (?)", (album,))
        album_id = cur.fetchone()[0]

        cur.execute("INSERT OR REPLACE INTO Track(title, album_id, genre_id, rating, count, len) VALUES(?,?,?,?,?,?)",(track,album_id,genre_id,rating,count,lenght))

        conn.commit()