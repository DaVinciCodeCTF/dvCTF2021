CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    admin INT NOT NULL DEFAULT 0);

CREATE TABLE login_attempts (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    ip VARCHAR(255),
    time VARCHAR(255));

INSERT INTO users(username, password, admin) VALUES ('admin', 'SUkmmW&4iTHuH!', 1);
INSERT INTO users(username, password) VALUES ('mickey', '^vzuS*6cn8NsZ2');
INSERT INTO users(username, password) VALUES ('eric', 'K3yroen4zLd%bz');
INSERT INTO users(username, password) VALUES ('tony', '@Zdsxug*zLA35Q');
