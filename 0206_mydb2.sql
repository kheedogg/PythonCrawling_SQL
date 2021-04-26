SHOW DATABASES ;

CREATE DATABASE testdb ;	# show databases ;를 통해 testdb라는 data base가 추가되어 있는 것을 확인할 수 있다.
USE testdb ;

SHOW TABLES ;

CREATE TABLE codes (
	fullcd  CHAR(07) PRIMARY KEY ,
	kornm VARCHAR(20) NOT NULL,
	engnm VARCHAR(20)
)

# https://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do
# 공통코드 조회의 xml

### 자료 확인
SELECT * FROM codes ;	# table안에 넣은 data가 존재하지 않는다.

### 부분 자료 확인
SELECT * FROM codes
WHERE kornm LIKE '%광역시' ;	# 광역시인 자료행 확인

SELECT kornm FROM codes
WHERE kornm LIKE '%광역시' ; # 광역시가 있는 kornm만 확인

SELECT kornm FROM codes
WHERE kornm LIKE '%광역시' ORDER BY kornm DESC ;	# data 정렬

SELECT SUBSTRING(fullcd, 1, 2) AS c1,
	SUBSTRING(fullcd, 3, 2) AS c2,
	SUBSTRING(fullcd, 5, 3) AS c3,
FROM codes ;

SELECT SUBSTRING(fullcd, 6, 1) AS c3,
	SUBSTRING(fullcd, 7, 1) AS c4
FROM codes ;

SELECT SUBSTRING(fullcd, 6, 1) AS c3,
	COUNT(*)
FROM codes GROUP BY c3 ;

SELECT SUBSTRING(fullcd, 6, 1) AS c3,
	COUNT(*) AS cnt
FROM codes GROUP BY c3 HAVING cnt >= 9;




### 자료 추가
INSERT INTO codes (fullcd, kornm, engnm)
VALUES ('0105001', '서울시', '') ;
# select * from codes ; 를 통해 codes table 안에 값이 저장되어 있는 것을 확인할 수 있다.
INSERT INTO codes (fullcd, kornm) 	# 넣고싶은 column명만 지정가능
VALUES ('0105002', '경기도') ;	# engnm 에 공백이 아닌 NULL로 값이 지정된다.
INSERT INTO codes # (fullcd, kornm, engnm) 생략가능!
VALUES ('0105003', ' 강원도', '') ;	
# 하나의 데이터를 넣을 때마다 하나의 insert구문 필요
INSERT INTO codes VALUES('0105004', '충청북도', NULL);
INSERT INTO codes VALUES('0105005', '충청남도', NULL);
INSERT INTO codes VALUES('0105006', '경상북도', NULL);
INSERT INTO codes VALUES('0105007', '경상남도', NULL);
INSERT INTO codes VALUES('0105008', '전라북도', NULL);
INSERT INTO codes VALUES('0105009', '전라남도', NULL);
INSERT INTO codes VALUES('0105010', '제주도', NULL);
INSERT INTO codes VALUES('0105011', '부산시', NULL);
INSERT INTO codes VALUES('0105012', '대구시', NULL);
INSERT INTO codes VALUES('0105013', '대전시', NULL);
INSERT INTO codes VALUES('0105014', '울산시', NULL);
INSERT INTO codes VALUES('0105015', '인천시', NULL);
INSERT INTO codes VALUES('0105016', '광주시', NULL);
INSERT INTO codes VALUES('0105017', '세종시', NULL);


### 자료수정 !!위험!!
UPDATE codes
SET kornm = '광역시';

UPDATE codes
SET kornm = REPLACE(kornm, '시', '광역시') ;

UPDATE codes
SET kornm = '서울특별시' WHERE fullcd = '0105001' ;
# where절 추가

UPDATE codes
SET kornm = '세종시' WHERE fullcd = '0105017' ;


### 자료값 모두 삭제 !!위험!!
DELETE FROM codes ;









