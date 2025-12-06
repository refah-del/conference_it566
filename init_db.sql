CREATE TABLE session (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    location TEXT,
    time TEXT
);

CREATE TABLE speaker (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    bio TEXT
);

CREATE TABLE session_speaker_xref (
    session_id INTEGER,
    speaker_id INTEGER,
    PRIMARY KEY (session_id, speaker_id),
    FOREIGN KEY (session_id) REFERENCES session(id),
    FOREIGN KEY (speaker_id) REFERENCES speaker(id)
);