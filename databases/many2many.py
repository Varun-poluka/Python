import json
import sqlite3

conn = sqlite3.connect("rosterdb.sqlite")
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
    
CREATE TABLE Course(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);
                  
CREATE TABLE Member(
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY(user_id , course_id)
)
''')

with open("roster_data.json" , "r") as file:
    data = file.read()
    info = json.loads(data)
    for i in info:
        name = i[0]
        title = i[1]    
        role = i[2]

        cur.execute("INSERT OR IGNORE INTO User(name) VALUES(?)",(name,))
        cur.execute("SELECT id FROM User WHERE name = ?",(name,))
        user_id = cur.fetchone()[0]
        
        cur.execute("INSERT OR IGNORE INTO Course(title) VALUES(?)",(title,))
        cur.execute("SELECT id FROM Course WHERE title = ?", (title,))
        course_id = cur.fetchone()[0]

        cur.execute("INSERT OR REPLACE INTO Member(user_id , course_id , role) VALUES(?,?,?)",(user_id, course_id, role))

        conn.commit()