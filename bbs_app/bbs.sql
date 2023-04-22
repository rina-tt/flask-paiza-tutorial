CREATE TABLE posts (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255),
  content TEXT
);

INSERT INTO posts(username,content)
  VALUES
  ("world","hello world"),
  ("Python","hello Python"),
  ("Flask","hello Flask"),
  ("mysql","hello mysql");