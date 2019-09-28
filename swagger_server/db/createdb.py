import sqlite3
from swagger_server import config


def dict_factory(cursor, row):
    """Для удобного вывода словаря из базы"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn = sqlite3.connect(config.database)
conn.row_factory = dict_factory
cursor = conn.cursor()

cursor.execute(f"""
CREATE TABLE achievement (
    id            INTEGER NOT NULL PRIMARY KEY,
    "name"        VARCHAR(100) NOT NULL,
    description   VARCHAR(100) NOT NULL,
    goal          INTEGER NOT NULL
);
""")

cursor.execute(f"""
CREATE TABLE article (
    id        INTEGER NOT NULL PRIMARY KEY,
    text      VARCHAR(100) NOT NULL,
    author   INTEGER NOT NULL,
    likes     INTEGER,
    numberViews INTEGER,
    date VARCHAR(100),
    FOREIGN KEY ( author ) REFERENCES "user" ( id )
);
""")

cursor.execute(f"""
CREATE TABLE category (
    id       INTEGER NOT NULL PRIMARY KEY,
    "name"   VARCHAR(100)
);
""")

cursor.execute(f"""
CREATE TABLE competition (
    id            INTEGER NOT NULL PRIMARY KEY,
    "name"        VARCHAR(100),
    description   varchar
);
""")

cursor.execute(f"""
CREATE TABLE event (
    id                     INTEGER NOT NULL PRIMARY KEY,
    head                   VARCHAR(100) NOT NULL,
    describe               VARCHAR(100) NOT NULL,
    location               VARCHAR(100) NOT NULL,
    datestart              VARCHAR(100) NOT NULL,
    duration               VARCHAR(100) NOT NULL,
    volunteersrequired     INTEGER,
    volunteersalready      INTEGER,
    volunteersvalidating   INTEGER,
    category_id            INTEGER NOT NULL,
    FOREIGN KEY ( category_id )
        REFERENCES category ( id )
);
""")

cursor.execute(f"""
CREATE TABLE progress (
    progress         INTEGER NOT NULL,
    achievement_id   INTEGER NOT NULL PRIMARY KEY,
    user_id          INTEGER NOT NULL,
    FOREIGN KEY ( achievement_id )
        REFERENCES achievement ( id ),
     FOREIGN KEY ( user_id )
        REFERENCES "user" ( id )
);
""")

cursor.execute(f"""
CREATE TABLE subscribe (
    user_id    INTEGER NOT NULL,
    user_id1   INTEGER NOT NULL,
     FOREIGN KEY ( user_id )
        REFERENCES "user" ( id ),
        FOREIGN KEY ( user_id1 )
        REFERENCES "user" ( id )
);
""")

cursor.execute(f"""
CREATE TABLE "user" (
    id             INTEGER NOT NULL PRIMARY KEY,
    login          VARCHAR(100) NOT NULL,
    password       VARCHAR(100) NOT NULL,
    firstname      VARCHAR(100),
    lastname       VARCHAR(100),
    email          VARCHAR(100),
    location       VARCHAR(100),
    region_id      INTEGER NOT NULL,
    dobrobonuses   INTEGER NOT NULL,
    FOREIGN KEY ( region_id )
        REFERENCES region ( id )
);
""")



