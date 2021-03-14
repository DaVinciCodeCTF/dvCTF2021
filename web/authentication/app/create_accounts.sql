CREATE TABLE accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_admin INTEGER DEFAULT 0 NOT NULL
);

INSERT INTO accounts(username, password, is_admin) VALUES ('admin', 'r34lly_s3cur3!!1337', 1);
INSERT INTO accounts(username, password) VALUES ('jean-claude', '1_h4t3_my_p455w0rdsZzZ');
