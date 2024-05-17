-- 크롤링 데이터 저장용 테이블 생성 스크립트
-- table.sql
-- 네이버 영화상영 정보 제공 페이지 크롤링 결과 저장용 테이블
-- 테이블명 : movie
-- 파이썬의 Movie 클래스 필드명과 테이블 컬럼명 일치시킴 => 필드명의 '__' 제외함
-- rank : pk, 나머지 컬럼은 not null
-- 컬럼 comment 도 지정
DROP table MOVIE CASCADE CONSTRAINTS;

CREATE TABLE MOVIE (
    RANK NUMBER CONSTRAINT PK_MOVIE PRIMARY KEY,
    TITLE VARCHAR2(100) NOT NULL,
    STAR_POINT NUMBER(7, 2) NOT NULL,
    RELEASE_DATE VARCHAR2(20),
    GENRE VARCHAR2(30),
    LINK VARCHAR2(2000)
);

COMMENT ON COLUMN MOVIE.RANK IS '상영순위';
COMMENT ON COLUMN MOVIE.TITLE IS '영화제목';
COMMENT ON COLUMN MOVIE.STAR_POINT IS '영화별점';
COMMENT ON COLUMN MOVIE.RELEASE_DATE IS '개봉일';
COMMENT ON COLUMN MOVIE.GENRE IS '장르';
COMMENT ON COLUMN MOVIE.LINK IS '링크';

COMMIT;