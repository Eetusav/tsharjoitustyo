## Taulujen create-lauseet

CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        PRIMARY KEY (id)
)

CREATE TABLE conversation (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
)

CREATE TABLE comment (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        account_id INTEGER NOT NULL,
        conversation_id INTEGER,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id),
        FOREIGN KEY(conversation_id) REFERENCES conversation (id)
)

CREATE TABLE subs (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        conversation_id INTEGER,
        account_id INTEGER,
        PRIMARY KEY (id),
        FOREIGN KEY(conversation_id) REFERENCES conversation (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
)

