SHOW DATABASES ;

CREATE DATABASE testdb ;
USE testdb ;

DROP TABLE moviestar ;	# database내에서 table 삭제

CREATE TABLE IF NOT EXISTS moviestar (
	id INT AUTO_INCREMENT PRIMARY KEY,	# 자동으로 id 부여
	writename VARCHAR(20),
	mvname VARCHAR(100),
	star int,
	content TEXT,
	writedate CHAR(10)
);

SELECT * FROM moviestar ;

DESC moviestar ;

SHOW TABLES ;

SELECT mvname, COUNT(*) AS cnt FROM moviestar ;
SELECT mvname, COUNT(*) AS cnt FROM moviestar GROUP BY mvname;
SELECT mvname, COUNT(*) AS cnt FROM moviestar GROUP BY mvname ORDER BY cnt;
SELECT mvname, COUNT(*) AS cnt FROM moviestar GROUP BY mvname ORDER BY cnt desc;
SELECT mvname, COUNT(*) AS cnt FROM moviestar GROUP BY mvname ORDER BY COUNT(*) desc;
SELECT * FROM moviestar WHERE mvname = '클로젯' ;
SELECT mvname, COUNT(*) AS cnt, AVG(star) AS avge FROM moviestar GROUP BY mvname ORDER BY COUNT(*) desc;
SELECT mvname, COUNT(*) AS cnt, AVG(star) AS avge FROM moviestar GROUP BY mvname HAVING cnt >10 ORDER BY COUNT(*) DESC;
SELECT mvname, COUNT(*) AS cnt, AVG(star) AS avge FROM moviestar GROUP BY mvname HAVING cnt >10 AND avge >=8 ORDER BY COUNT(*) DESC;

DELETE FROM moviestar ;



